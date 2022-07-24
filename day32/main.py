import random
import smtplib
import day32.config as config
from datetime import datetime
import pandas as pd

bday_df = pd.read_csv("birthdays.csv", index_col=0)


def check_bday(month, day):
    now = datetime.now()
    if now.month == month and now.day == day:
        return True
    else:
        return False


for index, row in bday_df.iterrows():
    if check_bday(row.month, row.day):
        with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt") as email_template:
            template = email_template.read()
        email_body = template.replace("[NAME]", index)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=config.gmail_user, password=config.gmail_special_pass)
            connection.sendmail(from_addr=config.gmail_user,
                                to_addrs=row.email,
                                msg=f"Subject:Happy Birthday {row.name}!!\n\n"
                                    f"{email_body}")




