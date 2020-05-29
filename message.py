#/usr/bin/env python3
from twilio.rest import Client
from config import *

MESSAGE_BODY = "Get out here boys ;)"

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

for name, num in NUMBERS.items():
    print("Sending message to " + name)
    message = client.messages.create(
        body=MESSAGE_BODY,
        from_=FROM_NUMBER,
        to=num
    )
