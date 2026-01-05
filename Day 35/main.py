import requests
from twilio.rest import Client
import os

#this is the endpoint for the openweathermap api
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
#our api key for this specific website
api_key = os.environ.get("API_KEY")
print(api_key)

#twilio account details
account_sid = ""
auth_token = ""

#paramaters for the weather api request
weather_params = {
    "lat": 56.4620,
    "lon": 2.9707,
    "appid": api_key,
    "cnt": 4,
}

#make the request using the requests.get method
response = requests.get(OWM_Endpoint, params=weather_params)
#check the response to the request - 200 means success
print(response.status_code)
#this will give us more information if the request fails
response.raise_for_status()
#save the data in json format using the .json method
weather_data = response.json()


#manual code gathering:
# code_1 = weather_data["list"][0]["weather"][0]["id"]
# code_2 = weather_data["list"][1]["weather"][0]["id"]
# code_3 = weather_data["list"][2]["weather"][0]["id"]
# code_4 = weather_data["list"][3]["weather"][0]["id"]
# code_list = [code_1, code_2, code_3, code_4]
# print(code_list)
#
# if any (code < 700 for code in code_list):
#         print("Bring an Umbrella")
# else:
#     print("No need for an umbrella today!")


#pythonic code gathering:
will_rain = False                                       #assign will_rain variable as False bool
for hour_data in weather_data["list"]:                  #assign hour_data variable to each item in the list at weather_data["list"]
    condition_code = hour_data["weather"][0]["id"]      #assign condition_code variable to found when looping through that location at each list element
    if int(condition_code) < 700:                       #check if condition code, converted to int, is less than 700
        will_rain = True                                #if so, change will_rain to True
if will_rain:                                           #after completing loop, print appropriate response
    client = Client(account_sid, auth_token)
    message = client.messages.create(
      from_="whatsapp",
      body="It's going to rain today. Remember to bring an umbrella",
      to="whatsapp"
    )
else:
    print("No rain today!")



