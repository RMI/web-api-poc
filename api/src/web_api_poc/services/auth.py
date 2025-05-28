import os
from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

POC_API_KEY = os.getenv("POC_API_KEY")
POC_API_KEY_NAME = "X-API-Key"

api_key_header = APIKeyHeader(name=POC_API_KEY_NAME, auto_error=True)


def get_api_key(POC_API_KEY: str = Security(api_key_header)):
    if POC_API_KEY == POC_API_KEY:
        return POC_API_KEY
    raise HTTPException(status_code=403, detail="Invalid API Key")
