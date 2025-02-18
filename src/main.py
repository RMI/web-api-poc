from fastapi import FastAPI
from routers.health import health_router
import uvicorn

app = FastAPI()


@app.get("/")
def root():
    return {"Hello": "World"}

app.include_router(health_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")
    