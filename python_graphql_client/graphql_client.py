"""Module containing graphQL client."""
import json
import logging
from typing import Any, Callable

import aiohttp
import requests
import websockets


class GraphqlClient:
    """Class which represents the interface to make graphQL requests through."""

    def __init__(self, endpoint: str, headers: dict = {}, **kwargs: Any):
        """Insantiate the client."""
        self.logger = logging.getLogger(__name__)
        self.endpoint = endpoint
        self.headers = headers
        self.options = kwargs

    def __request_body(
        self, query: str, variables: dict = None, operation_name: str = None
    ) -> dict:
        json = {"query": query}

        if variables:
            json["variables"] = variables

        if operation_name:
            json["operationName"] = operation_name

        return json

    def execute(
        self,
        query: str,
        variables: dict = None,
        operation_name: str = None,
        headers: dict = {},
        **kwargs: Any,
    ):
        """Make synchronous request to graphQL server."""
        request_body = self.__request_body(
            query=query, variables=variables, operation_name=operation_name
        )

        result = requests.post(
            self.endpoint,
            json=request_body,
            headers={**self.headers, **headers},
            **{**self.options, **kwargs},
        )

        result.raise_for_status()
        return result.json()

    async def execute_async(
        self,
        query: str,
        variables: dict = None,
        operation_name: str = None,
        headers: dict = {},
    ):
        """Make asynchronous request to graphQL server."""
        request_body = self.__request_body(
            query=query, variables=variables, operation_name=operation_name
        )

        async with aiohttp.ClientSession() as session:
            async with session.post(
                self.endpoint,
                json=request_body,
                headers={**self.headers, **headers},
            ) as response:
                return await response.json()

    async def subscribe(
        self,
        query: str,
        handle: Callable,
        variables: dict = None,
        operation_name: str = None,
        headers: dict = {},
        init_payload: dict = {},
    ):
        """Make asynchronous request for GraphQL subscription."""
        connection_init_message = json.dumps(
            {"type": "connection_init", "payload": init_payload}
        )

        request_body = self.__request_body(
            query=query, variables=variables, operation_name=operation_name
        )
        request_message = json.dumps(
            {"type": "start", "id": "1", "payload": request_body}
        )

        async with websockets.connect(
            self.endpoint,
            subprotocols=["graphql-ws"],
            extra_headers={**self.headers, **headers},
        ) as websocket:
            await websocket.send(connection_init_message)
            await websocket.send(request_message)
            async for response_message in websocket:
                response_body = json.loads(response_message)
                if response_body["type"] == "connection_ack":
                    self.logger.info("the server accepted the connection")
                elif response_body["type"] == "ka":
                    self.logger.info("the server sent a keep alive message")
                else:
                    handle(response_body["payload"])
