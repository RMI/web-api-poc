from fastapi import FastAPI
from routers.health import health_router
from routers.mtcars import data_output
from docs.documentation import description
import uvicorn

app = FastAPI(
    # This info goes directly into /docs
    title="RMI Web API poc",
    # Description of API defined in docs/documentation.py for ease of reading
    description=description,
    summary="This project is a proof-of-concept (POC) web API built using the FastAPI library.",
    version="0.0.1",
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
def root():
    return {"Hello": "World"}


app.include_router(health_router)
app.include_router(data_output)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")
