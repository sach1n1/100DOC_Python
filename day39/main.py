from day39.config import MY_IATA
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

dm = DataManager()
city_list = dm.get_flight_data()

for city in city_list:
    flight = FlightSearch(MY_IATA, city)
    low_prices, flight_price = flight.search_flights()
    if low_prices:
        send = NotificationManager()
        send.send_details(flight_price, MY_IATA, city)

