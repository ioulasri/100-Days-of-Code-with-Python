import csv

# temperature = []
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     for i in data:
#         if i[1] != "temp":
#             temperature.append(int(i[1]))
#
#     print(temperature)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# temps = data["temp"].tolist()
#
# print(data["temp"].mean())
# print(data["temp"].max())
# Monday = data[data.day == "Monday"]
# print((Monday.temp * 9/5) + 32)
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
Cinnamon = (len(data[data["Primary Fur Color"] == "Cinnamon"]))
black = (len(data[data["Primary Fur Color"] == "Black"]))
gray = (len(data[data["Primary Fur Color"] == "Gray"]))
dic = {
       "Fur Color": ["Cinnamon", "Black", "Gray"],
       "count": [Cinnamon, black, gray]
       }

p = pandas.DataFrame(dic)
p.to_csv("squirrel_count.csv")
