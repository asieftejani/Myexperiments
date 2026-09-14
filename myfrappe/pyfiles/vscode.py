import os
import requests
from dotenv import load_dotenv
import json

path = os.path.expanduser("~/storage/shared/Documents/website/.env/secrets.txt")

load_dotenv(path)

api_key = os.getenv("github_api_key")

response = requests.get(
    "https://api.github.com/user",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/vnd.github+json"
    }
)

data = {"status_code": response.status_code,
"github data": response.json()}

return data
