from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routers.health import health_router
from routers.mtcars import data_output
import uvicorn

app = FastAPI()


@app.get("/")
async def redirect():
    response = RedirectResponse(url="/docs")
    return response


app.include_router(health_router)
app.include_router(data_output)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")
