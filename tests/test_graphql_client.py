"""Tests for main graphql client module."""

from unittest import TestCase, IsolatedAsyncioTestCase
from unittest.mock import patch, MagicMock, AsyncMock

from aiohttp import web
from requests.exceptions import HTTPError

from python_graphql_client import GraphqlClient


class TestGraphqlClientConstructor(TestCase):
    """Test cases for the __init__ function in the client class."""

    def test_init_client_no_endpoint(self):
        """Throws an error if no endpoint is provided to the client."""
        with self.assertRaises(TypeError):
            GraphqlClient()

    def test_init_client_endpoint(self):
        """Saves the endpoint url as an instance attribute."""
        endpoint = "http://www.test-api.com/"
        client = GraphqlClient(endpoint)

        self.assertEqual(client.endpoint, endpoint)

    def test_init_client_headers(self):
        """Saves a dictionary of HTTP headers to the instance."""
        headers = {"Content-Type": "application/json"}
        client = GraphqlClient(endpoint="", headers=headers)

        self.assertEqual(client.headers, headers)


class TestGraphqlClientExecute(TestCase):
    """Test cases for the synchronous graphql request function."""

    @patch("python_graphql_client.graphql_client.requests")
    def test_execute_basic_query(self, requests_mock):
        """Sends a graphql POST request to an endpoint."""
        client = GraphqlClient(endpoint="http://www.test-api.com/")
        query = """
        {
            tests {
                status
            }
        }
        """
        client.execute(query)

        requests_mock.post.assert_called_once_with(
            "http://www.test-api.com/", json={"query": query}, headers={}
        )

    @patch("python_graphql_client.graphql_client.requests")
    def test_execute_query_with_variables(self, requests_mock):
        """Sends a graphql POST request with variables."""
        client = GraphqlClient(endpoint="http://www.test-api.com/")
        query = ""
        variables = {"id": 123}
        client.execute(query, variables)

        requests_mock.post.assert_called_once_with(
            "http://www.test-api.com/",
            json={"query": query, "variables": variables},
            headers={},
        )

    @patch("python_graphql_client.graphql_client.requests.post")
    def test_raises_http_errors_as_exceptions(self, post_mock):
        """Raises an exception if an http error code is returned in the response."""
        response_mock = MagicMock()
        response_mock.raise_for_status.side_effect = HTTPError()
        post_mock.return_value = response_mock

        client = GraphqlClient(endpoint="http://www.test-api.com/")

        with self.assertRaises(HTTPError):
            client.execute(query="")

    @patch("python_graphql_client.graphql_client.requests.post")
    def test_execute_query_with_headers(self, post_mock):
        """Sends a graphql POST request with headers."""
        client = GraphqlClient(
            endpoint="http://www.test-api.com/",
            headers={"Content-Type": "application/json", "Existing": "123"},
        )
        query = ""
        client.execute(query=query, headers={"Existing": "456", "New": "foo"})

        post_mock.assert_called_once_with(
            "http://www.test-api.com/",
            json={"query": query},
            headers={
                "Content-Type": "application/json",
                "Existing": "456",
                "New": "foo",
            },
        )

    @patch("python_graphql_client.graphql_client.requests.post")
    def test_execute_query_with_operation_name(self, post_mock):
        """Sends a graphql POST request with the operationName key set."""
        client = GraphqlClient(endpoint="http://www.test-api.com/")
        query = """
            query firstQuery {
                test {
                    status
                }
            }

            query secondQuery {
                test {
                    status
                }
            }
        """
        operation_name = "firstQuery"
        client.execute(query, operation_name=operation_name)

        post_mock.assert_called_once_with(
            "http://www.test-api.com/",
            json={"query": query, "operationName": operation_name},
            headers={},
        )


class TestGraphqlClientExecuteAsync(IsolatedAsyncioTestCase):
    """Test cases for the asynchronous graphQL request function."""

    async def get_application(self):
        """Override base class method to properly use async tests."""
        return web.Application()

    @patch("aiohttp.ClientSession.post")
    async def test_execute_basic_query(self, mock_post):
        """Sends a graphql POST request to an endpoint."""
        mock_post.return_value.__aenter__.return_value.json = AsyncMock()
        client = GraphqlClient(endpoint="http://www.test-api.com/")
        query = """
        {
            tests {
                status
            }
        }
        """

        await client.execute_async(query)

        mock_post.assert_called_once_with(
            "http://www.test-api.com/", json={"query": query}, headers={}
        )

    @patch("aiohttp.ClientSession.post")
    async def test_execute_query_with_variables(self, mock_post):
        """Sends a graphql POST request with variables."""
        mock_post.return_value.__aenter__.return_value.json = AsyncMock()
        client = GraphqlClient(endpoint="http://www.test-api.com/")
        query = ""
        variables = {"id": 123}

        await client.execute_async(query, variables)

        mock_post.assert_called_once_with(
            "http://www.test-api.com/",
            json={"query": query, "variables": variables},
            headers={},
        )

    @patch("aiohttp.ClientSession.post")
    async def test_execute_query_with_headers(self, mock_post):
        """Sends a graphql POST request with headers."""
        mock_post.return_value.__aenter__.return_value.json = AsyncMock()
        client = GraphqlClient(
            endpoint="http://www.test-api.com/",
            headers={"Content-Type": "application/json", "Existing": "123"},
        )
        query = ""

        await client.execute_async("", headers={"Existing": "456", "New": "foo"})

        mock_post.assert_called_once_with(
            "http://www.test-api.com/",
            json={"query": query},
            headers={
                "Content-Type": "application/json",
                "Existing": "456",
                "New": "foo",
            },
        )

    @patch("aiohttp.ClientSession.post")
    async def test_execute_query_with_operation_name(self, mock_post):
        """Sends a graphql POST request with the operationName key set."""
        mock_post.return_value.__aenter__.return_value.json = AsyncMock()
        client = GraphqlClient(endpoint="http://www.test-api.com/")
        query = """
            query firstQuery {
                test {
                    status
                }
            }

            query secondQuery {
                test {
                    status
                }
            }
        """
        operation_name = "firstQuery"

        await client.execute_async(query, operation_name=operation_name)

        mock_post.assert_called_once_with(
            "http://www.test-api.com/",
            json={"query": query, "operationName": operation_name},
            headers={},
        )
