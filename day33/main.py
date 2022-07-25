import requests
import smtplib
import day32.config as config
from datetime import datetime

MY_LAT = 52.520008
MY_LONG = 13.404954

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if abs(iss_longitude - MY_LONG) <= 5 and abs(iss_latitude - MY_LAT) <= 5:
        return True
    else:
        return False


def is_night():
    response = requests.get("http://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True
    else:
        False


if is_night() and is_overhead():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(config.gmail_user, config.gmail_special_pass)
        connection.sendmail(from_addr=config.gmail_user,
                            to_addrs=config.yahoo_user,
                            msg="Subject:Look Up!!\n\n"
                                "See the ISS")

