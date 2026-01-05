import requests
from datetime import datetime
import smtplib
import time

#we set out lat and long as global variables
MY_LAT = 54.803331 # Your latitude
MY_LONG = -1.349354 # Your longitude

#we make a request to the ISS location API using the requests.get() function
response = requests.get(url="http://api.open-notify.org/iss-now.json")
#we check the HTTP status code of a response and raise an exception if the status code indicates an error.
response.raise_for_status()
#we save the API response in json form to the data variable
iss_data = response.json()

#we create iss lat and long variables by accessing the ISS position > latituude keys and converting the string to a float
iss_latitude = float(iss_data["iss_position"]["latitude"])
iss_longitude = float(iss_data["iss_position"]["longitude"])

#Write a function to check if our position is within +5 or -5 degrees of the ISS position, returning true if so
def check_iss_overhead(my_latitude, my_longitude, iss_lat, iss_long):
    if my_longitude - 5 <= iss_long <= my_longitude + 5 and my_latitude - 5 <= iss_lat <= my_latitude + 5:
        return True
    else:
        return False

#function to send email telling recipient to look up
def send_email():
    my_email =
    pw =
    # need to provide location of server
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # add transport layer security, which secures our connection to the server
        connection.starttls()
        # provide username and password to login
        connection.login(user=my_email, password=pw)
        # add sender and recipient info
        connection.sendmail(from_addr=my_email,
                            to_addrs="",
                            msg="Subject:ISS Overhead"
                                "\n\nLook Up!")



#create the parameters needed for the sunrise/sunset api request in dictionary format
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

#make request to sunrise-sunset website for api, adding the parameters dictionary as the parameter
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
#we check the HTTP status code of a response and raise an exception if the status code indicates an error.
response.raise_for_status()
#save the sunrise/sunset data as a json
sun_data = response.json()
#access the hour of sunrise and sunset by splitting the result, eg, 2025-12-08T08:13:16+00:00,
# firstly using T, then accessing the time using [1], then splitting the time using ":" and accessing the hour using [0]
sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

#get the current time of the day by getting thre current time using the datetime.now() function
time_now = datetime.now()
#access the current hour of the day using the .hour method
current_hour = time_now.hour


#Run the ISS overhead checker function, and also check if the current hour is greater than or equal to the hour of sunset (ie, is nighttime).
# If so, send the email!
#To run this code every 60 seconds, place it inside a while loop and use the time.sleep function
while True:
    time.sleep(5)
    if (check_iss_overhead(my_latitude=MY_LAT, my_longitude=MY_LONG, iss_lat=iss_latitude, iss_long=iss_longitude)
            and current_hour >= sunset):
        send_email()
    else:
        (print("Not quite yet!"))



# BONUS: run the code every 60 seconds.



