import csv

import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data(1).csv")
print(data.columns.values.tolist())
colors = data["Primary Fur Color"].value_counts()
new_Dataframe = pd.DataFrame(colors)
print(new_Dataframe)
new_Dataframe.to_csv("Colors")

