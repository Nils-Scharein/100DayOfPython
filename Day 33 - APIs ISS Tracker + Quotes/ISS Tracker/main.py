import time

import requests
from datetime import datetime

MY_LAT = 52.520008 # Your latitude
MY_LONG = 13.404954 # Your longitude

def get_update_location():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_position = (iss_latitude, iss_longitude)
    return iss_position

#Your position is within +5 or -5 degrees of the ISS position.
def check_coordinates_ISS_our_pos(position):
    lat, long = position
    latDiff = lat - MY_LAT
    longDiff = long - MY_LONG
    if (-5 <= latDiff <= 5) and (-5 <=longDiff <= 5):
        return True
    else:
        return False

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
def get_update_time():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    return (sunrise, sunset)

def check_time(ISS_time):
    sunrise, sunset = ISS_time
    timeNow = time_now.hour()
    if timeNow <= sunset or timeNow <= sunrise:
        return True

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    time.sleep(60000)

    if check_coordinates_ISS_our_pos(get_update_location()) and check_time(get_update_time()):
        print("look up")
    else:
        print("not above")