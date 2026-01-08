import os
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
import requests
from datetime import datetime
load_dotenv()

SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_API_AUTH = os.getenv("SHEETY_API_AUTH")

basic = HTTPBasicAuth(SHEETY_USERNAME, SHEETY_API_AUTH)

GENDER = "male"
WEIGHT_KG = 84
HEIGHT_CM = 185
AGE = 31

now = datetime.now()
today = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M")
print(today)
print(time)

query_api_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

sheety_api_endpoint = os.getenv("SHEETY_API_ENDPOINT")


query_text = input("What exercise have you done today?")

exercise_params = {
    "query": query_text,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
    "gender": GENDER
}

API_KEY = os.getenv("API_KEY")
APP_ID = os.getenv("APP_ID")


query_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = requests.post(url=query_api_endpoint, json=exercise_params, headers= query_headers)
print(response.json())
exercise_data = response.json()
exercise_data_list = [value for (key, value) in exercise_data.items()]
exercise_done =  exercise_data_list[0][0]["name"]
duration_achieved = exercise_data_list[0][0]["duration_min"]
calories_burned = exercise_data_list[0][0]["nf_calories"]


"""             ******              POSTING TO SHEETY             ******                  """

sheet_posting_params = {
    "workout": {
        "date": f"{today}",
        "time": f"{time}",
        "exercise": f"{exercise_done.title()}",
        "duration": f"{duration_achieved}",
        "calories": f"{calories_burned}",
    }
}

response = requests.post(url=sheety_api_endpoint, json=sheet_posting_params, auth=basic)
print(response.text)
