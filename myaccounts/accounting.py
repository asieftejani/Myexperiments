import requests

url = "https://nrkfgubozcjiujdusruu.supabase.co/rest/v1/coa"
data = {
  "account_name": "Cash",
  "account_type": "Asset",
  "parent_id": 1,
  "is_group": 0
}

headers = {
  "Authorization": f"Bearer {key}",
  "Content-Type": "application/json",
  "Prefer": "return=representation"
}

try:
  response = requests.post(url, json=data, headers = headers)
  response.raise_for_status()
  print("Status: ", response.status_code)
  print("Response: ", response.text)
  
except requests.exceptions.HTTPError as e:
  print("HTTP Error: ", e.response.status_code)
  print(e.response.text)
except requests.exceptions.RequestException as e:
  print("Request failed: ", e)