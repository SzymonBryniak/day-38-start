import requests
import os
import json
from datetime import datetime


today = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")

    # Nutri api
os.environ["APP_ID"] = "b0fcd0ea"
os.environ["API_KEY"] = "f5b51cc048a7e294674a7bb9a5b33dc2"

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

header = {
    'Content-Type': 'application/json',
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

nutri_json = {
    # "query": input("Tell me which exercises you did: ")
    "query": input("Tell me which exercises you did: ")
}


print(time)
def nutri_api():
    response_nutri = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=nutri_json, headers=header)
    response_nutri.raise_for_status()
    exercise = response_nutri.json()["exercises"][0]["name"]
    duration = response_nutri.json()["exercises"][0]["duration_min"]
    calories = response_nutri.json()["exercises"][0]["nf_calories"]
    print(exercise, duration, calories)
    return exercise, duration, calories
    # Sheety api (https://api.sheety.co/username/projectName/sheetName)

def sheety_get():
    endpoint = "https://api.sheety.co/fd51c961a3d2d10dee2bd6c572ed4d91/myWorkouts/workouts"
    response_sheety = requests.get(url=endpoint)
    response_sheety.raise_for_status()
    print(response_sheety.text)


def sheety_post(exercise, duration, calories):
    sheety_json = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories
        }
    }
    endpoint = "https://api.sheety.co/fd51c961a3d2d10dee2bd6c572ed4d91/myWorkouts/workouts"
    response_sheety = requests.post(url=endpoint, json=sheety_json)
    response_sheety.raise_for_status()
    print(response_sheety.text)

def sheety_delete(row):
    endpoint = f"https://api.sheety.co/fd51c961a3d2d10dee2bd6c572ed4d91/myWorkouts/workouts/{row}"
    response_sheety = requests.delete(url=endpoint)
    response_sheety.raise_for_status()
    print(response_sheety.text)


# Exercise, Duration, Calories = nutri_api()
# sheety_delete(2)
# sheety_post(Exercise,Duration,Calories)