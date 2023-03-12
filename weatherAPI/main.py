import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "ACae2d67240047d1c0c6d20db79efb30f8"
auth_token = "907bbda32f3d1d0af206b74c2f9d6f10"
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='kolchi khdam a3zi',
                              from_='+18155221703',
                              to='+212651452063'
                          )

print(message.sid)