from web_api_poc import create_app
from uvicorn import run
from importlib.metadata import metadata
from os import getenv
from dotenv import load_dotenv

# import .env settings
load_dotenv()
POC_API_PORT = int(getenv("POC_API_PORT", 8000))
POC_API_LOG_LEVEL = getenv("POC_API_LOG_LEVEL", "info").lower()

# Validate log level
valid_log_levels = ["critical", "error", "warning", "info", "debug", "trace"]
if POC_API_LOG_LEVEL not in valid_log_levels:
    print(f"Warning: Invalid log level '{POC_API_LOG_LEVEL}'. Defaulting to 'info'.")
    POC_API_LOG_LEVEL = "info"

meta = metadata("web_api_poc")

app = create_app(
    title="POC API", description=meta["summary"], version=meta["version"]
)

if __name__ == "__main__":
    print(f"Starting POC API on port {POC_API_PORT} with log level '{POC_API_LOG_LEVEL}'")
    run("main:app", host="0.0.0.0", port=POC_API_PORT, log_level=POC_API_LOG_LEVEL)
