import requests
import os

os.environ["APP_ID"] = "b0fcd0ea"
os.environ["API_KEY"] = "f5b51cc048a7e294674a7bb9a5b33dc2"

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

header = {
    "x-app-id": APP_ID,
    "x=app-key": API_KEY
}

exercise_stats = "Ran 2 miles and walked for 3km."
response = requests.post(url="https://v2/natural/exercise", data=exercise_stats, json="json", headers=header)
response.raise_for_status()
print(response.text)