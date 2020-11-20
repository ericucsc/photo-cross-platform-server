# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
import os
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
# To set up environmental variables, see http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
valid_phone_number_from = os.environ['TWILIO_PHONE_NUMBER']

client = Client(account_sid, auth_token)

def send_sms_to(to_phone_number, message):
    response = client.api.account.messages.create(
        to=to_phone_number,
        from_=valid_phone_number_from,
        body=message,
    )
    print(response)
    print("Sent a message: {} to {}".format(message, to_phone_number))