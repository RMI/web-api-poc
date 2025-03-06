# web-api-poc
[![Test Status](https://github.com/RMI/web-api-poc/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/RMI/web-api-poc/actions/workflows/test.yml) 

This project is a proof-of-concept (POC) web API built using the FastAPI library.

## Set-Up

### Prerequisites

This project uses [uv](https://github.com/astral-sh/uv) for environment and dependency management.

To install, follow the [official installation guide](https://github.com/astral-sh/uv?tab=readme-ov-file#installation).

### Setup

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

## Running the API

### Locally serve the Fast API with:

```
uv run src/main.py
```

### Run Fast API in docker container with: 

```
# build the image
docker compose build

# run the container
docker compose up

# do both
docker compose up --build
```

The API will be accessible at http://localhost.

## Contributing

### Dependency Management

Dependencies are managed using uv. To add a new library, run:

```
uv add <library>
```

### Testing
 
Testing is implemented using the `pytest` library. Run all tests locally with:

```
uv run pytest
```

Or, you can run specific test suites with:
```
uv run pytest tests/test_unit.py        # to only run unit tests
uv run pytest tests/test_integration.py # to only run integration tests
```

For test-only dependencies, add them using:
``` 
uv add --dev <library>
```

### Linting

This project follows the [black](https://github.com/psf/black) code formatting standard. Lint code by running:

```
black path/to/file.py # to lint a single file
black .               # to lint the entire directory
```

Ensure that your code is properly formatted before submitting a pull request.

### Deployment
**TODO**

## License
 This project is licensed under the [MIT License](LICENSE.txt) 
