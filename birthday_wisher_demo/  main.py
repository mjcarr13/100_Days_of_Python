#this is going terribly, so here's what we're going to do.

#we're not going to blunder through this. We're going to follow her solution then re-do it ourselves three time later
#and this is the new rule we'll follow going forwards. If we feel despairing and like there's no joy in life, follow the code
#and then redo it to help with some cementing. Otherwise, we can do it ourselves.

from datetime import datetime
import pandas
import random
import smtplib


MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

#get today's date as a datetime object using the now() function
today = datetime.now()
#print(today) #2025-12-04 15:00:37.358238

#using this object, create a tuple containing the current month and day, saving as a new variable
today_tuple = (today.month, today.day)
#print(today_tuple) -->(12, 4)

#create a data variable using the pandas read csv function, from our birthday csv
data = pandas.read_csv("birthdays.csv")
#print(data) --> outputs as table with name, email, year, month, day as column headings

#create a dictionary of our birthdays using dictionary comprehension
#syntax follow dict = {(month, day): data_row for (index, data_row) in data.iterrows()}
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
#print(birthdays_dict) --> honestly barely comprehensible dictionary but containing rows of data for each person in csv

#create an if statement that checks if the previously created tuple of day and month appears in the dictionary
if today_tuple in birthdays_dict:


#create new variable for the birthday person by accessing them in the dictionary using the tuple
    birthday_person = birthdays_dict[today_tuple]

#save the file path for one of the letters, chosen randomly, as a new variable
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

#open the file as new variable
    with open(file_path) as letter_file:

#read the contents of the file, saving as a new variable
        contents = letter_file.read()

#replace the contents of this variable using .replace function, passing in the content to replace "[NAME]", with the person's name as taken from the dictionary
        contents = contents.replace("[NAME]", birthday_person["name"])


