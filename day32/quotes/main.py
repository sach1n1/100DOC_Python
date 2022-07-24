import random
import smtplib
import day32.config as config
from datetime import datetime

with open("quotes.txt", "r") as quotes_file:
    quotes = quotes_file.readlines()

day = datetime.now().weekday()

if day == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=config.gmail_user, password=config.gmail_special_pass)
        connection.sendmail(from_addr=config.gmail_user,
                            to_addrs=config.yahoo_user,
                            msg=f"Subject:Hello\n\n"
                                f"{quotes[random.randint(0, len(quotes))]}")
