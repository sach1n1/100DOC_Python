from datetime import datetime
import smtplib
import day32.config as config
from config import *
import requests

data = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={LAT}&lon={LONG}&appid={API_KEY}")
data.raise_for_status()
weather = data.json()

current_hour = datetime.now().hour

rain = False

for _ in range(0, 12):
    code = weather["hourly"][current_hour]["weather"][0]["id"]
    if code < 700:
        rain = True
    current_hour += 1
    current_hour %= 24

if rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=config.gmail_user,
                         password=config.gmail_special_pass)
        connection.sendmail(from_addr=config.gmail_user,
                            to_addrs=config.yahoo_user,
                            msg="Subject:IT WILL RAIN!!\n\n"
                                "Take an Umbrella!")

