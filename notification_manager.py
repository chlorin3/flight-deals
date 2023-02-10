import os
from twilio.rest import Client
import smtplib

ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")
MY_NUMBER = os.environ.get("MY_NUMBER")
MY_EMAIL = os.environ.get("MY_EMAIL")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_NUMBER,
            to=MY_NUMBER,
        )

        print(message.sid)

    def send_emails(self, message, customer):
        with smtplib.SMTP("smtp.poczta.onet.pl") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=customer,
                msg=message,
            )
