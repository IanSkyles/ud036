from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACe3c05e48aaeee6b2b4e3e205b8797f1f"
auth_token  = "889b02abf086b4b2724f938e4564b083"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="My name is Ian Skyles",
    to="2532374289",    # Replace with your phone number
    from_="+13525759537") # Replace with your Twilio number
print message.sid
