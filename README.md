[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Python GraphQL Client

> Simple package for making requests to a graphql server.

<!-- Badges here. -->

## Installation

```bash
pip install python-graphql-client
```

## Usage

```python
from python_graphql_client import GraphqlClient

# Instantiate the client with an endpoint.
client = GraphqlClient(endpoint="https://countries.trevorblades.com")

# Create the query string and variables required for the request.
query = """
    query countryQuery($countryCode: String) {
        country(code:$countryCode) {
            code
            name
        }
    }
"""
variables = {"countryCode": "CA"}

# Synchronous request
data = client.execute(query=query, variables=variables)
print(data)  # => {'data': {'country': {'code': 'CA', 'name': 'Canada'}}}


# Asynchronous request
import asyncio

data = asyncio.run(client.execute_async(query=query, variables=variables))
print(data)  # => {'data': {'country': {'code': 'CA', 'name': 'Canada'}}}
```

## Roadmap

To start we'll try and use a Github project board for listing current work and updating priorities of upcoming features.

## Contributing

Read the [Contributing](docs/CONTRIBUTING.md) documentation for details on the process for submitting pull requests to the project. Also take a peek at our [Code of Conduct](docs/CODE_OF_CONDUCT.md).

## Authors and Acknowledgement

Kudos to @xkludge, @DaleSeo, and @mattbullock for getting this project started.

## License

[MIT License](LICENSE)
