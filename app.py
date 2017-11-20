import os, sys
import random
import time
from flask import Flask, request
from utils import wit_response
from pymessenger import Bot

app = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAAa4SLDVfmYBAMWZAK6RkTRrE52AsWOI6lZCl50QVfOltUv7OuFvZBb9pyH5ltojwjlFUvEDN69IpAX9nsZA7c9mgE8ZAz6Ho7lIDcdkbkGEtZA8hGWZBqbytrXUbrPrTYEZCBuqssKDuZBwJIhY3OhrwXrJv2145T8wTohN3OpjE9Kn6p4mZAYEjyscxBkiyCRfEZD"

bot = Bot(PAGE_ACCESS_TOKEN)

greeting_list = ['hi','hey','hello','Hi','Hello','Hey']
thank_list = ['Thanks','Thank you','thank you']
thank_ret_list = ['No problem',"It's my job",'I am happy to help you', "It's my pleasure to serve you",'😇','☺']
talk_list = ["I'm good"," I'm fine","I'm ok","fine"]

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

				# FROM HERE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
				if messaging_event.get('message'):
					if (messaging_event['message'].get('nlp')):
						if (messaging_event['message']['nlp'].get('entities')):
							if (messaging_event['message']['nlp']['entities'].get('intent')):
								if (messaging_event['message']['nlp']['entities']['intent'][0].get('value')):
									intent = messaging_event['message']['nlp']['entities']['intent'][0]['value']
									#entity, value_list = messaging_event['message']['nlp']['entities'].items()
									#value = value_list[0]['value']

									if intent == "get_temp":							#T
										temp_value = 'temp_script()'
										response = 'temp_value'							#E
									elif intent == "check_temp_low":								#M
										response = 'check_temp_low()'
									elif intent == "check_temp_high":					#E
										response = 'check_temp_high()'
									elif intent == "get_humidity":
										response = 'humidity_script()'
									elif intent == "check_humidity_low":
										response = 'check_humidity_low()'
									elif intent == "check_humidity_high":
										response = 'check_humidity_high()'
									elif intent == "check_light_on_or_off":
										response = "lights on"
									elif intent == "check_light_off":
										response = 'check_light_off()'
									elif intent == "check_light_on":
										response = 'check_light_on()'
									elif intent == "get_image":
										response = 'get_image()'
									elif intent == "get_greeting":
										response = random.choice(greeting_list)
									elif intent == "get_thank":
										response = random.choice(thank_ret_list)
									elif intent == "return_thank":
										response = random.choice(thank_list)
									elif intent == "get_talk":
										response = random.choice(talk_list)
									else:
										response = "???"
								bot.send_text_message(sender_id, response)

						else:
							response = "Sorry! I didn't understand"
							bot.send_text_message(sender_id, response)


	return "ok", 200


def log(message):
	print(message)
	sys.stdout.flush()


if __name__ == "__main__":
	app.run(debug = True, port = 80)