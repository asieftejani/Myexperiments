import os
import requests
from dotenv import load_dotenv

def github_json():
  path = os.path.expanduser("~/storage/shared/Documents/website/.env/secrets.txt")

  load_dotenv(path)

  api_key = os.getenv("github_api_key")

  headers={
          "Authorization": f"Bearer {api_key}",
          "Accept": "application/vnd.github+json"
  }

  user_response = requests.get(
    "https://api.github.com/user", headers=headers
  )
  
  repo_response = requests.get(
    "https://api.github.com/user/repos", headers=headers
    )
  
  repos = repo_response.json()
  for repo in repos:
    owner = repo["owner"]["login"]
    name = repo["name"]
    cs_response = requests.get(
    f"https://api.github.com/repos/{owner}/{name}/codespaces", headers=headers
    )
    repo["codespaces"] = cs_response.json()

  data = {"status_code": user_response.status_code,
  "github_data": user_response.json(), "repo_data": repos}
  
  return data
