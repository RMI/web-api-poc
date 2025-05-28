# Pathways-based transition assessment repository (pbtar)

[![Test DB service](https://github.com/RMI/pbtar/actions/workflows/db-test.yml/badge.svg?branch=main)](https://github.com/RMI/pbtar/actions/workflows/db-test.yml)

[![Lint API Service](https://github.com/RMI/pbtar/actions/workflows/api-lint.yml/badge.svg?branch=main)](https://github.com/RMI/pbtar/actions/workflows/api-lint.yml)
[![Test API service](https://github.com/RMI/pbtar/actions/workflows/api-test.yml/badge.svg?branch=main)](https://github.com/RMI/pbtar/actions/workflows/api-test.yml)

[![Lint Frontend service](https://github.com/RMI/pbtar/actions/workflows/frontend-lint.yml/badge.svg?branch=main)](https://github.com/RMI/pbtar/actions/workflows/frontend-lint.yml)
[![Test Frontend service](https://github.com/RMI/pbtar/actions/workflows/frontend-test.yml/badge.svg?branch=main)](https://github.com/RMI/pbtar/actions/workflows/frontend-test.yml)

[![Test service integration](https://github.com/RMI/pbtar/actions/workflows/integration-test.yml/badge.svg?branch=main)](https://github.com/RMI/pbtar/actions/workflows/integration-test.yml)
[![Docker](https://github.com/RMI/pbtar/actions/workflows/api-docker-build-and-push.yml/badge.svg?branch=main)](https://github.com/RMI/pbtar/actions/workflows/api-docker-build-and-push.yml)

## Running the application

### Setup

1. Clone the Repo

```sh
git clone https://github.com/RMI/pbtar
cd pbtar
```

2. Create an `.env` file to store the desired API key, (internal) API port, DB port and Frontend port
```sh
cp .env.example .env
```

### Run the services with docker compose

```sh
# build the image
docker compose build

# run the container
docker compose up --detach

# do both
docker compose up --detach --build
```

The primary web service (React) will be accessible at http://localhost.

The API and API documentation (Swagger) will be accessible at http://localhost:8000.

### Make a request from the API

```sh
curl -X 'GET' \
  'http://localhost:8000/scenarios' \
  -H 'accept: application/json' \
  -H 'X-API-Key: abc123'
```

Defaults to the API key "abc123", but an alternate key (matching what is in your `.env` file) can be input and submitted on the page.

### Shutdown the docker container

```sh
docker compose down

# also delete the database volume when shutting down the container
docker compose down --volumes
```

## License
 This project is licensed under the [MIT License](LICENSE.txt) 
