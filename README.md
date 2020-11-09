[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![Python CI Checks](https://github.com/prodigyeducation/python-graphql-client/workflows/Python%20CI%20Checks/badge.svg)
![Upload Python Package](https://github.com/prodigyeducation/python-graphql-client/workflows/Upload%20Python%20Package/badge.svg)

# Python GraphQL Client

> Simple package for making requests to a graphql server.

<!-- Badges here. -->

## Installation

```bash
pip install python-graphql-client
```

## Usage

- Query/Mutation

```py
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

- Subscription

```py
from python_graphql_client import GraphqlClient

# Instantiate the client with a websocket endpoint.
client = GraphqlClient(endpoint="wss://www.your-api.com/graphql")

# Create the query string and variables required for the request.
query = """
    subscription onMessageAdded {
        messageAdded
    }
"""

# Asynchronous request
import asyncio

asyncio.run(client.subscribe(query=query, handle=print))
# => {'data': {'messageAdded': 'Error omnis quis.'}}
# => {'data': {'messageAdded': 'Enim asperiores omnis.'}}
# => {'data': {'messageAdded': 'Unde ullam consequatur quam eius vel.'}}
# ...
```

## Advanced Usage

### Disable SSL verification

Set the keyword argument `verify=False` ether when instantiating the `GraphqlClient` class.

```py
from python_graphql_client import GraphqlClient

client = GraphqlClient(endpoint="wss://www.your-api.com/graphql", verify=False)
```

Alternatively, you can set it when calling the `execute` method.

```py
from python_graphql_client import GraphqlClient

client = GraphqlClient(endpoint="wss://www.your-api.com/graphql"
client.execute(query="<Your Query>", verify=False)
```

### Custom Authentication

```py
from requests.auth import HTTPBasicAuth
from python_graphql_client import GraphqlClient

auth = HTTPBasicAuth('fake@example.com', 'not_a_real_password')
client = GraphqlClient(endpoint="wss://www.your-api.com/graphql", auth=auth)
```

## Roadmap

To start we'll try and use a Github project board for listing current work and updating priorities of upcoming features.

## Contributing

Read the [Contributing](docs/CONTRIBUTING.md) documentation for details on the process for submitting pull requests to the project. Also take a peek at our [Code of Conduct](docs/CODE_OF_CONDUCT.md).

## Authors and Acknowledgement

Kudos to @xkludge, @DaleSeo, and @mattbullock for getting this project started.

## License

[MIT License](LICENSE)
