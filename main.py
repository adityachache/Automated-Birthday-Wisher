##################### Extra Hard Starting Project ######################
import pandas as pd
import random
import smtplib
import datetime as dt
import os

# ENTER YOUR EMAIL HERE
SENDER_EMAIL = "test@email.com"
# ENTER YOUR PASSWORD HERE
SENDER_PASSWORD = "12345"

# 1. Update the birthdays.csv
data = pd.read_csv("birthdays.csv")
birthday_dict = data.to_dict(orient="records")
month_list = data['month'].to_list()
day_list = data['day'].to_list()
name = ""
email = ""

# Getting current day and month
current_date = dt.datetime.now()
current_month = current_date.month
current_day = current_date.day

# Checking if today matches a birthday in the birthdays.csv
# FOR TESTING PURPOSE REPLACE "in month_list" with your current month(number) and same with current_day
if current_month in month_list and current_day in day_list:
    # If step 2 is true, pick a random letter from letter templates and
    # replace the [NAME] with the person's actual name from birthdays.csv
    for record in birthday_dict:
        if record['month'] == current_month and record['day'] == current_day:
            name = record['name']
            email = record['email']

    letter = random.choice(os.listdir("letter_templates"))
    with open(f"letter_templates/{letter}", mode="r") as content:
        message = content.read()
        updated_message = message.replace("[NAME]", name)
        # Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
            connection.sendmail(from_addr=SENDER_EMAIL,
                                to_addrs=email,
                                msg=f"Subject:Happy Birthday\n\n{updated_message}")
