from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routers.health import health_router
from routers.mtcars import data_output
import uvicorn
import tomllib

try:
    with open("pyproject.toml", "rb") as f:
        tomldata = tomllib.load(f)
        version = tomldata["project"]["version"]
        description = tomldata["project"]["description"]
except FileNotFoundError:
    print("pyproject.toml not found")

app = FastAPI(
    # This info goes directly into /docs
    title="RMI Web API poc",
    # Description of API defined in docs/documentation.py for ease of reading
    description=description,
    summary="This project is a proof-of-concept (POC) web API built using the FastAPI library.",
    version=version,
    contact={
        "name": "RMI",
        "url": "https://github.com/RMI",
    },
    license_info={
        "name": "MIT",
        "url": "https://github.com/RMI/web-api-poc/blob/main/LICENSE.txt",
    },
)


@app.get("/")
async def redirect():
    response = RedirectResponse(url="/docs")
    return response


app.include_router(health_router)
app.include_router(data_output)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, log_level="info")
