"""Module containing graphQL client."""

import aiohttp
import requests


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
            self.endpoint, json=request_body, headers=self.__request_headers(headers),
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
