# web_api_poc

This project is a proof-of-concept (POC) web API using the FastAPI library.

# Set-Up

## Prerequisites

This project uses uv for environment and dependency management.

To install, follow the official installation guide: https://github.com/astral-sh/uv

## Setup

1. Clone the Repo

```
git clone https://github.com/RMI/web-api-poc
cd web-api-poc
```

2. Create and Activate the Virtual Environment
```
uv venv .venv
source .venv/bin/activate # macOS/Linux
```

3. Install Dependencies
```
uv sync
```

# Running the API

Locally serve the Fast API with:

```
uv run main.py
```

The API will be accessible at http://127.0.0.1:5000.

# Contributing

## Dependency Management

Dependencies are managed using uv . New dependencies can be added using:

```
uv add <library>
```

## Testing
 
Testing is implemented using the `pytest` library. All tests can be run locally using:

```
uv run pytest
```

Or, you can individually run unit or integration tests with:
```
uv run pytest tests/test_unit.py # to only run unit tests
uv run pytest tests/test_integration.py # to only run integration tests
```

If dependencies are added that are *only* required by tests, please add them appropriately to `pyproject.toml` using:
``` 
uv add --dev <library>
```

## Linting
**TODO**

## Deployment
**TODO**

# License
 This project is licensed under the [MIT License](LICENSE.txt) 
