# Web API Proof of Concept (web_api_poc)

[![Lint API Service](https://github.com/RMI/pbtar/actions/workflows/api-lint.yml/badge.svg?branch=main)](https://github.com/RMI/pbtar/actions/workflows/api-lint.yml)
[![Test API Service](https://github.com/RMI/pbtar/actions/workflows/api-test.yml/badge.svg?branch=main)](https://github.com/RMI/pbtar/actions/workflows/api-test.yml)
[![Build API Service](https://github.com/RMI/pbtar/actions/workflows/api-docker-build-and-push.yml/badge.svg?branch=main)](https://github.com/RMI/pbtar/actions/workflows/api-docker-build-and-push.yml)

[![Test service integration](https://github.com/RMI/pbtar/actions/workflows/integration-test.yml/badge.svg?branch=main)](https://github.com/RMI/pbtar/actions/workflows/integration-test.yml)

## Running the application

### Setup

1. Clone the Repo

```sh
git clone https://github.com/RMI/web-api-poc
cd web-api-poc
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

The API and API documentation (Swagger) will be accessible at http://localhost:8000.

### Make a request from the API

```sh
curl -X 'GET' \
  'http://localhost:8000/api/tables/film/schema' \
  -H 'accept: application/json'
```

### Shutdown the docker container

```sh
docker compose down

# also delete the database volume when shutting down the container
docker compose down --volumes
```

## License
 This project is licensed under the [MIT License](LICENSE.txt) 
