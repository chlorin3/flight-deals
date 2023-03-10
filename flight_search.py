import requests
import os
from flight_data import FlightData

ENDPOINT = "https://api.tequila.kiwi.com"
HEADERS = {
    "apikey": os.environ.get("TEQUILA_API_KEY")
}


class FlightSearch:

    def get_code(self, city):
        parameters = {
            "term": city,
            "location_types": "airport",
            "limit": 1,
        }
        response = requests.get(url=f"{ENDPOINT}/locations/query", headers=HEADERS, params=parameters)
        iata_code = response.json()["locations"][0]["city"]["code"]
        return iata_code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        parameters = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        response = requests.get(url=f"{ENDPOINT}/v2/search", headers=HEADERS, params=parameters)

        try:
            data = response.json()["data"][0]

        except IndexError:

            parameters["max_stopovers"] = 1
            response = requests.get(url=f"{ENDPOINT}/v2/search", headers=HEADERS, params=parameters)

            try:
                data = response.json()["data"][0]
            except IndexError:
                return None
            else:
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport=data["route"][1]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][2]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )
                return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )

            print(f"{flight_data.destination_city}: ??{flight_data.price}")

            return flight_data
