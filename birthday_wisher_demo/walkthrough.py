

from datetime import datetime
import pandas
import random
import smtplib


MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

#get today's date as a datetime object using the now() function
today = datetime.now()
#using this object, create a tuple containing the current month and day, saving as a new variable
today_tuple = (today.month, today.day)

#create a data variable using the pandas read csv function, from our birthday csv
data = pandas.read_csv("birthdays.csv")
#create a dictionary of our birthdays using dictionary comprehension
#syntax follow dict = {(month, day): data_row for (index, data_row) in data.iterrows()}
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
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
#setup the email to send using smtplib
    with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )