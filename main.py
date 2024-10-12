import requests
import os
import json

os.environ["APP_ID"] = "b0fcd0ea"
os.environ["API_KEY"] = "f5b51cc048a7e294674a7bb9a5b33dc2"

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

header = {
    'Content-Type': 'application/json',
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

body = {
    "query": input("Tell me which exercises you did: ")
}


response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=body, headers=header)
response.raise_for_status()
print(response.text)