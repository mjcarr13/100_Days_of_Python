#Email, and how it works

#Behind the scenes
"""

SMTP - Simple Mail Transfer Protocol 

smtplib lets us send emails via python

"""

import smtplib

MY_EMAIL = "michaeljcarr130@gmail.com"
PASSWORD = ""

# need to provide location of server
with smtplib.SMTP("smtp.gmail.com") as connection:
    #add transport layer security, which secures our connection to the server
    connection.starttls()
    #provide username and password to login
    connection.login(user=MY_EMAIL, password=PASSWORD)
    #add sender and recipient info
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs="michaeljcarr13@gmail.com",
                        msg="Subject:Hello"
                            "\n\nThis is the body of the email")

#By default with Gmail for example, we can't just use this.

#We have to go into our security settings and allow

#Manage>Secuirty>Turn on 2fA > App passwords (create other) > copy password and add above
