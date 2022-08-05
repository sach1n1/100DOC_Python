import smtplib
import day32.config as config


class NotificationManager:
    def __init__(self, low_price, iata, city):
        self.price = low_price
        self.city = city
        self.iata = iata

    def send_details(self):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=config.gmail_user, password=config.gmail_special_pass)
            connection.sendmail(from_addr=config.gmail_user,
                                to_addrs=config.yahoo_user,
                                msg=f"Subject:LOW PRICES!!!!\n\n"
                                    f"Flight from Berlin-{self.origin_iata} to {self.city['city']}-{self.city['iataCode']}"
                                    f"is now available for {self.price} euros.")
