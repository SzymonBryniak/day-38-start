import pygsheets
import requests
import os
import json
from datetime import datetime
# credentials file must be generated and downloaded from Google cloud
# Pass the path to the credentials file (client_secret.json)
gc = pygsheets.authorize(client_secret=r'../../Documents/client_secret.json')

# Open a Google Sheet
sh = gc.open('My Workouts')

# Access a worksheet
wk1 = sh[0] # Open first worksheet of spreadsheet
# Or
# wks = sh.sheet1 # sheet1 is name of first worksheet
print(wk1, sh.url, wk1.get_value('A1') )


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


def pygsheets_post():
    exercise, duration, calories = nutri_api()
    new_row = [today, time, exercise, duration, calories]
    # Append the new row at the end of the worksheet
    wk1.append_table(values=new_row)

pygsheets_post()
