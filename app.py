from twilio.rest import Client
from datetime import datetime
import requests
import time

# Meta info you need to fill out
sid = ""
auth_token = ""

me = ""
you = ""
body = "hey david! so, every hour i'm gonna be sending you a new card from throne of eldraine! hope u enjoy"

# Twilio Account SID and Auth Token
client = Client(sid, auth_token)

# Scryfall API endpoint
eldraine_cards = 'https://api.scryfall.com/cards/search?q=set%3Deld'
headers = {
            'content-type': 'application/json',
            'charset':'utf-8'
        }
response = requests.get(eldraine_cards, headers=headers).json()
# Let david know what we're up to
client.messages.create(to=you, from_=me, body=body)
print("said hello")

for card in response['data']:
    client.messages.create(to=you, from_=me, media_url=[card['image_uris']['normal']])
    print("sent the card {0} to david at {0}".format(card['name'], datetime.now().time()))
    # Wait for an hour
    time.sleep(3600)
