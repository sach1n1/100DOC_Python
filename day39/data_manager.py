import day39.config as config
import requests


class DataManager:

    def __init__(self):
        self.sheety_url = config.SHEETY_URL
        self.sheety_header = {"Authorization": f"Bearer {config.SHEETY_API}"}

    def get_flight_data(self):
        sheety_post = requests.get(url=config.SHEETY_URL, headers=self.sheety_header)
        return sheety_post.json()["prices"]
