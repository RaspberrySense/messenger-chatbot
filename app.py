import os, sys
import random
from flask import Flask, request
from wit import Wit
from utils import wit_response
from pymessenger import Bot

app = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAAa4SLDVfmYBAMWZAK6RkTRrE52AsWOI6lZCl50QVfOltUv7OuFvZBb9pyH5ltojwjlFUvEDN69IpAX9nsZA7c9mgE8ZAz6Ho7lIDcdkbkGEtZA8hGWZBqbytrXUbrPrTYEZCBuqssKDuZBwJIhY3OhrwXrJv2145T8wTohN3OpjE9Kn6p4mZAYEjyscxBkiyCRfEZD"

bot = Bot(PAGE_ACCESS_TOKEN)

#greeting_list = ['hi','hey','hello','whats up']


@app.route('/', methods=['GET'])
def verify():
	#Webhook verification
	if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
		if not request.args.get("hub.verify_token") == "hello":
			return "Verification token mismatch", 403
		return request.args["hub.challenge"], 200
	return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():
	data = request.get_json()
	log(data)

	if data['object'] == 'page':
		for entry in data['entry']:
			for messaging_event in entry['messaging']:

				# IDs
				sender_id = messaging_event['sender']['id']
				recipient_id = messaging_event['recipient']['id']

				if messaging_event.get('message'):
					# Extracting text message
					if 'text' in messaging_event['message']:
						messaging_text = messaging_event['message']['text']
					else:
						messaging_text = 'nothing'
					
					response = None

					entity, value = wit_response(messaging_text)

					if entity == 'light_keyword':
						response = "I will run LDR script"
					elif entity == "temp_keyword":
						response == "I will run Tempscript"

					if response == None:
						response = "Sorry"

					bot.send_text_message(sender_id, response)

	return "ok", 200


def log(message):
	print(message)
	sys.stdout.flush()


if __name__ == "__main__":
	app.run(debug = True, port = 80)