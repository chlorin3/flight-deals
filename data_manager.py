import requests
import os

ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
HEADERS = {"Authorization": f"Bearer {os.environ.get('API_KEY')}"}


class DataManager:

    def __init__(self):
        self.destination_data = self.get_data()
        self.customers_data = self.get_customers()

    def get_data(self):
        response = requests.get(f"{ENDPOINT}/prices", headers=HEADERS)
        return response.json()["prices"]

    def get_customers(self):
        response = requests.get(f"{ENDPOINT}/users", headers=HEADERS)
        return response.json()["users"]

    def update_destination_codes(self, new_data):
        """Google Sheets rows without iataCode are updated only if
           there's a difference between destination_data and provided new_data
        """
        if self.destination_data == new_data:
            return

        for i in range(len(self.destination_data)):
            if not self.destination_data[i]["iataCode"]:
                parameters = {
                    "price": {
                        "iataCode": new_data[i]["iataCode"]
                    }
                }
                response = requests.put(f"{ENDPOINT}/prices/{self.destination_data[i]['id']}", headers=HEADERS,
                                        json=parameters)
                print(response.text)

        self.destination_data = new_data
