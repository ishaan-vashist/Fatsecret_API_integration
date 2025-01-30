import requests
import os
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

app = FastAPI()

# FatSecret API credentials
CLIENT_ID = os.getenv("FATSECRET_CLIENT_ID")
CLIENT_SECRET = os.getenv("FATSECRET_CLIENT_SECRET")
TOKEN_URL = "https://oauth.fatsecret.com/connect/token"
API_URL = "https://platform.fatsecret.com/rest/server.api"


def get_access_token():
    """
    Fetch OAuth 2.0 Access Token from FatSecret.
    """
    payload = {
        "grant_type": "client_credentials",
        "scope": "basic"
    }
    headers = {
        "Authorization": f"Basic {get_basic_auth()}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = requests.post(TOKEN_URL, data=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        raise HTTPException(status_code=401, detail="Failed to obtain access token")


def get_basic_auth():
    """
    Encode Client ID and Secret for Basic Authentication.
    """
    import base64
    creds = f"{CLIENT_ID}:{CLIENT_SECRET}"
    return base64.b64encode(creds.encode()).decode()


@app.get("/search_food")
def search_food(query: str, page: int = 1, max_results: int = 10):
    """
    Endpoint to search food items using FatSecret API.
    """
    access_token = get_access_token()

    params = {
        "method": "foods.search",
        "format": "json",
        "search_expression": query,
        "page_number": page,
        "max_results": max_results
    }

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(API_URL, params=params, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch food data")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
