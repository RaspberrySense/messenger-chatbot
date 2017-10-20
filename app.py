import os, sys
import random
from flask import Flask, request
#from utils import wit_response
from pymessenger import Bot

app = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAAa4SLDVfmYBAMWZAK6RkTRrE52AsWOI6lZCl50QVfOltUv7OuFvZBb9pyH5ltojwjlFUvEDN69IpAX9nsZA7c9mgE8ZAz6Ho7lIDcdkbkGEtZA8hGWZBqbytrXUbrPrTYEZCBuqssKDuZBwJIhY3OhrwXrJv2145T8wTohN3OpjE9Kn6p4mZAYEjyscxBkiyCRfEZD"

bot = Bot(PAGE_ACCESS_TOKEN)

greeting_list = ['hi','hey','hello','whats up','Hi','Hello','Hey']
thank_list = ['Thanks','Thank you','Thank you very much','thanks','thank you','thank you very much']
thank_ret_list = ['No problem',"It's my job",'I am happy to help you', "It's my pleasure to serve you"]

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
					# Extracting text message
					if 'text' in messaging_event['message']:
						word = messaging_event['message']['text']
						if word in greeting_list:
							response = random.choice(greeting_list)
						elif word in thank_list:
							response = random.choice(thank_ret_list)
						else:
							response = word
					else:
						response = '👍'
					
					'''response = None

					entity, value = wit_response(messaging_text)

					if entity == 'light_keyword':
						response = "I will run LDR script"
					elif entity == "temp_keyword":
						response == "I will run Tempscript"

					if response == None:
						response = "Sorry!!!"   '''


					bot.send_text_message(sender_id, response)
					bot.send_text_message(sender_id, response)

					# TILL HERE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

	return "ok", 200


def log(message):
	print(message)
	sys.stdout.flush()


if __name__ == "__main__":
	app.run(debug = True, port = 80)