import csv
import json
import pandas as pd
import requests


Apikey_df = pd.read_csv("Api.txt")
api_key = Apikey_df.loc[0, 'Key']

coordinates = pd.read_csv("coordinates.txt")
coordinates.columns = coordinates.columns.str.strip()

lat = coordinates.loc[0, 'lat']
long = coordinates.loc[0, 'long']

weather_params = {
    "lat": 52.520008,
    "lon": 13.404954,
    "appid": api_key,
    "cnt": 4
}

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

# Making the GET request to the OpenWeatherMap API
response = requests.get(OWM_Endpoint, params=weather_params)

# Open the file in write mode and dump the JSON data into it
with open("data.json", "w") as data_file:
    json.dump(response.json(), data_file, indent=4)

# Optionally print the JSON response
print(response.json())

# Parse the JSON data into a dictionary
weather_data = response.json()

will_rain = False

# Now you can safely iterate over the list in the response
def check_weather_12_hours():
    for hour_data in weather_data["list"]:
        if hour_data["weather"][0]["id"] < 700:
            return True
        else:
            return False

if check_weather_12_hours() == True:
    print("bring an umbrella")