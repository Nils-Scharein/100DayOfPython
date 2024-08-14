"""
import csv

weather_data = []
day_list = []
temp_list = []
condition_list = []

with open("weather_data.csv", newline="") as data:
    reader = csv.reader(data)
    for row in reader:
        weather_data.append(row)

for item in weather_data:
    if item == weather_data[0]:
        continue
    day, temp, condition = item
    day_list.append(str(day))
    temp_list.append(int(temp))
    condition_list.append(str(condition))


print(weather_data)
print(temp_list)
print(day_list)
print(condition_list)

"""

import pandas as pd

data = pd.read_csv("weather_data.csv")
temp = data["temp"]
day = data["day"]
condition = data["condition"]

avr_temp = round(temp.mean(), 2)
print(avr_temp)

print(temp)
print(day)
print(condition)

print(temp.idxmax())
print(data.iloc[temp.idxmax()])
print(data[data.temp == temp.max()])


def umrechnung(temp: int):
    return (temp * 1.8 + 32)


print(umrechnung(20))

monday = data[data.day == "Monday"]

print("Test")
print(monday.temp.apply(lambda x: umrechnung(x)))

