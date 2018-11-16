from twilio.rest import Client
from urllib.parse import urlencode

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACa7895c59a8482877ce1777ca90057d50'
auth_token = '1eba21cccd071e621ab1eb2413409982'

# To do: Check behavior on moving message body to the constructor of the function.
def sendMessage():
    client = Client(account_sid, auth_token)

    message_body = input("Enter message: \n")
    message = client.messages.create(
                                  body=message_body,
                                  from_='7315954188',
                                  to='7313078629')

    return message.sid

def outgoingCall():

    # The number of the phone initiating the call
    # This should either be a Twilio number or a number that you've verified
    from_number = "7315954188"

    # The number of the phone receiving the call.
    to_number = "7313078629"

    # Use the Twilio-provided site for hte TwiML response.
    url = "http://twimlets.com/message?"

    # The phone message text.
    #message = "Can you hear this abdu"
    message = input("Enter message: \n")

    # Initialize the Twilio client
    client = Client(account_sid, auth_token)

    # Make the call.
    call = client.calls.create(to=to_number,
                               from_=from_number,
                               url = url + urlencode({'Message': message}))
    return call.sid
