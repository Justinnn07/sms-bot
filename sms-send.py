import os
from twilio.rest import Client

account_sid = os.environ['your access token']
auth_token = os.environ['your access token']
client = Client(account_sid, auth_token)

message = client.messages.create(
    body='This is a boy',
    from_='+13158193129',
    to='+919319275200'
)

print(message.sid)
