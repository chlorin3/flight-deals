from data_manager import DataManager
from flight_search import FlightSearch
import copy
import datetime as dt
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

DEPARTURE_CODE = "LON"

sheet_data = copy.deepcopy(data_manager.destination_data)

# Add IATA Codes to Google Sheets
for row in sheet_data:
    if not row["iataCode"]:
        row["iataCode"] = flight_search.get_code(row["city"])

data_manager.update_destination_codes(sheet_data)

date_from = (dt.datetime.now() + dt.timedelta(days=1))
date_to = (dt.datetime.now() + dt.timedelta(days=180))

# Check flights
for row in sheet_data:
    flight = FlightSearch().check_flights(
        origin_city_code=DEPARTURE_CODE,
        destination_city_code=row["iataCode"],
        from_time=date_from,
        to_time=date_to,
    )

    # If there are no flights to destination city, let the for loop to continue to run
    if not flight:
        continue

    if flight.price < int(row["lowestPrice"]):
        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} " \
                  f"to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} " \
                  f"to {flight.return_date}."

        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        print(message)

        for user in data_manager.customers_data:
            notification_manager.send_emails(message.encode("utf-8"), user["email"])

        #notification_manager.send_sms(message)
