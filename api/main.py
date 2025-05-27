from web_api_poc import create_app
from uvicorn import run
from importlib.metadata import metadata
from os import getenv
from dotenv import load_dotenv

# import .env settings
load_dotenv()
API_PORT = int(getenv("API_PORT", 8000))
API_LOG_LEVEL = getenv("API_LOG_LEVEL", "info").lower()

# Validate log level
valid_log_levels = ["critical", "error", "warning", "info", "debug", "trace"]
if API_LOG_LEVEL not in valid_log_levels:
    print(f"Warning: Invalid log level '{API_LOG_LEVEL}'. Defaulting to 'info'.")
    API_LOG_LEVEL = "info"

meta = metadata("web_api_poc")

app = create_app(
    title="Web API POC", description=meta["summary"], version=meta["version"]
)

if __name__ == "__main__":
    print(f"Starting API on port {API_PORT} with log level '{API_LOG_LEVEL}'")
    run("main:app", host="0.0.0.0", port=API_PORT, log_level=API_LOG_LEVEL)
