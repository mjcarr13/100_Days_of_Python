
# with open("weather_data.csv") as weather_data:
#     stripped_data = weather_data.strip()
#     print(stripped_data)
#
# import csv
#
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
#

# create a new list called termpeatures containing the temps in the csv file as an integer.

import pandas
data = pandas.read_csv("weather_data.csv")
#we turn our table into a dictionary
dict_data = data.to_dict()
print(dict_data)
#we access a specific column and turn this into a list .
temp_list = data.temp.to_list()
print(temp_list)


#get max value contained within the data["temp"} column.

#we need to pull out the row of data where temp was at its max
#access data. print the row data.temp which is equal to the data.temp max.
print(data[data.temp == data.temp.max()])

#getting data in a column
print(data.condition)

#get data in a row
#specifiy the column initially (data.day) then specifiy which element within that column leads the row
print(data[data.day == "Monday"])
#which row in our column of temperature is equal to the one contianing the maximum temperature?
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

# get monday's temp and convert to farenheit '

converted_temp = ((monday.temp)*9/5)+32
print(converted_temp)

#converting a dictionary to a DataFrame in Pandas
our_dict = {
    "Students": ["Amy", "James", "Angela"],
     "Scores": [76, 56, 65]
            }

student_info = pandas.DataFrame(our_dict)
print(student_info)

#We can also save it to a CSV file to your project:

student_info.to_csv("new_data.csv")
