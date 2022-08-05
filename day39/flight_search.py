from datetime import datetime
import day39.config as config
import requests


class FlightSearch:

    def __init__(self, iata, city):
        self.origin_iata = iata
        self.dest_iata = city["iataCode"]
        self.currentPrice = city["lowestPrice"]
        self.url = config.SKYSCANNER_API
        self.headers = config.SKYSCANNER_HEADERS

    def search_flights(self):
        query = {"adults": "1",
                 "origin": f"{self.origin_iata}",
                 "destination": f"{self.dest_iata}",
                 "departureDate": f"{datetime.now().strftime('%Y-%m-%d')}",
                 "currency": "EUR"}
        print(query)
        flight = requests.get(url=self.url, params=query, headers=self.headers)
        price = flight.json()["itineraries"].buckets[2].items[0]["price"]["raw"]
        if price < self.currentPrice:
            return True, price
        else:
            return False, price
