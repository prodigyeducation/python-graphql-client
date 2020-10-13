"""Module containing graphQL client."""
import json
import logging
from typing import Callable

import aiohttp
import requests
import websockets

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")


class GraphqlClient:
    """Class which represents the interface to make graphQL requests through."""

    def __init__(self, endpoint: str, headers: dict = None):
        """Insantiate the client."""
        self.endpoint = endpoint
        self.headers = headers or {}

    def __request_body(
        self, query: str, variables: dict = None, operation_name: str = None
    ) -> dict:
        json = {"query": query}

        if variables:
            json["variables"] = variables

        if operation_name:
            json["operationName"] = operation_name

        return json

    def __request_headers(self, headers: dict = None) -> dict:
        return {**self.headers, **headers} if headers else self.headers

    def execute(
        self,
        query: str,
        variables: dict = None,
        operation_name: str = None,
        headers: dict = None,
    ):
        """Make synchronous request to graphQL server."""
        request_body = self.__request_body(
            query=query, variables=variables, operation_name=operation_name
        )

        result = requests.post(
            self.endpoint,
            json=request_body,
            headers=self.__request_headers(headers),
        )

        result.raise_for_status()
        return result.json()

    async def execute_async(
        self,
        query: str,
        variables: dict = None,
        operation_name: str = None,
        headers: dict = None,
    ):
        """Make asynchronous request to graphQL server."""
        request_body = self.__request_body(
            query=query, variables=variables, operation_name=operation_name
        )

        async with aiohttp.ClientSession() as session:
            async with session.post(
                self.endpoint,
                json=request_body,
                headers=self.__request_headers(headers),
            ) as response:
                return await response.json()

    async def subscribe(
        self,
        query: str,
        handle: Callable,
        variables: dict = None,
        operation_name: str = None,
        headers: dict = None,
    ):
        """Make asynchronous request for GraphQL subscription."""
        connection_init_message = json.dumps({"type": "connection_init", "payload": {}})

        request_body = self.__request_body(
            query=query, variables=variables, operation_name=operation_name
        )
        request_message = json.dumps(
            {"type": "start", "id": "1", "payload": request_body}
        )

        async with websockets.connect(
            self.endpoint,
            subprotocols=["graphql-ws"],
            extra_headers=self.__request_headers(headers),
        ) as websocket:
            await websocket.send(connection_init_message)
            await websocket.send(request_message)
            async for response_message in websocket:
                response_body = json.loads(response_message)
                if response_body["type"] == "connection_ack":
                    logging.info("the server accepted the connection")
                elif response_body["type"] == "ka":
                    logging.info("the server sent a keep alive message")
                else:
                    handle(response_body["payload"])
