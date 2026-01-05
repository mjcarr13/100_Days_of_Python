#so we're building a table which takes from the squirrel data
#and counts the grey and red and black squiirels
#and puts these into a dictionary which then gets exported as a dataframe

# import pandas
# #
# #
# # #so we need to access the fur colour column and turn that into a list
# #
# # #read the csv file and save to variable
# squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20251123.csv")
# # #
# # #create a list freaturing the primary fur color column info
# # color_list = squirrel_data["Primary Fur Color"]
# # print(type(color_list))
# #
# # #extract the unique colors from the list as a new list
# # unique_colours = set(color_list)
# #
# # #create a dictionary by looping through this unique list and adding each unique color as a key, with its count as the value
# #
# # squirrel_color_count = {}
# # for color in unique_colours:
# #         squirrel_color_count[color] = color_list.count(color)
# #
# # print(squirrel_color_count)
#
# counts = squirrel_data["Primary Fur Color"].value_counts(dropna=False).to_dict()
# print(counts)
# counts_table = pandas.DataFrame(counts)
# counts_table.to_csv("squirrel_color_counts.cvs")
#
#each individual instance of a colour, we make the key in a dictionary
#the total number of times that colour appears is the value for said colour

# squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20251123.csv")

#Above was a fail, but also much more complicated than her method, which was:

import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20251123.csv")

gray_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])

