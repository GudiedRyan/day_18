import pandas
import smtplib
import secret
import datetime as dt
import random


my_email = "yesmanvong@gmail.com"
password = secret.password
now = dt.datetime.now()
today = (now.month, now.day)


data_list = pandas.read_csv("birthdays.csv")
bday_dict = {(data_row.month, data_row.day):data_row for (index,data_row) in data_list.iterrows()}


if today in bday_dict:
    templates = ("letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt")
    letter_to_send = random.choice(templates)
    bday_person = bday_dict[today]
    with open(letter_to_send) as letter:
        temp = letter.read()
    final_let = temp.replace("[NAME]", bday_person["name"])
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=bday_person.email, 
            msg=f"Subject:Happy Birthday\n\n{final_let}"
        )