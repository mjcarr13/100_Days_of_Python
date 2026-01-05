import smtplib
import datetime as dt
import random

import pandas


MY_EMAIL = "michaeljcarr13@gmail.com"
PASSWORD = ""



#need to check if current day is Monday, and if so, send a random quote

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open ("quotes.txt", "r") as quotes_file:
        all_quotes = quotes_file.readlines()
        random_quote = random.choice(all_quotes)

# need to provide location of server
with smtplib.SMTP("smtp-mail.outlook.com") as connection:
    #add transport layer security, which secures our connection to the server
    connection.starttls()
    #provide username and password to login
    connection.login(user=MY_EMAIL, password="PASSWORD")
    #add sender and recipient info
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs="michaeljcarr13@gmail.com",
                        msg=f"Subject:Monday Motivation"
                            f"\n\n{random_quote}")
