import os, sys
import random
import time
from flask import Flask, request
from utils import wit_response
from pymessenger import Bot

app = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAAa4SLDVfmYBAMWZAK6RkTRrE52AsWOI6lZCl50QVfOltUv7OuFvZBb9pyH5ltojwjlFUvEDN69IpAX9nsZA7c9mgE8ZAz6Ho7lIDcdkbkGEtZA8hGWZBqbytrXUbrPrTYEZCBuqssKDuZBwJIhY3OhrwXrJv2145T8wTohN3OpjE9Kn6p4mZAYEjyscxBkiyCRfEZD"

bot = Bot(PAGE_ACCESS_TOKEN)

greeting_list = ['hi','hey','hello','whats up','Hi','Hello','Hey']
thank_list = ['Thanks','Thank you','Thank you very much','thanks','thank you','thank you very much']
thank_ret_list = ['No problem',"It's my job",'I am happy to help you', "It's my pleasure to serve you",'😇','☺']

############################### Working ##################

def light_script():
	light_value = random.randint(1,20)
	return light_value

def temp_script():
	temp_value = random.randint(16,100)
	return temp_value

##########################################################

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

				############ while script ###################
				value1 = light_script()
				if value1 < 10 and value1 > 5:
					bot.send_text_message(sender_id, value1)

				###############################################

				# FROM HERE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
				if messaging_event.get('message'):

					# Extracting text message

					if 'text' in messaging_event['message']:
						messaging_text = messaging_event['message']['text']
						entity, value = wit_response(messaging_text)

						# selecting action to be done

						if entity == 'greeting_keyword':
							response = random.choice(greeting_list)
						elif entity == 'light_keyword':
							response = "Light script"
						elif entity == "temp_keyword":
							response = "Temp script"
						elif entity == 'camera_keyword':
							response = "I will run Camera script"
						elif entity == 'motion_keyword':
							response = "I will run Infrared motion script"
						elif entity == 'humidity_keyword':
							response = "I will run humidity sensor script"
						elif entity == 'thank_keyword':
							response = random.choice(thank_ret_list)
						elif entity == 'blush_keyword':
							response = random.choice(thank_list)
						else:
							response = "Sorry! I didn't understand."
					else:
						response = '👍'
					
					bot.send_text_message(sender_id, response)

					# TILL HERE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

	return "ok", 200


def log(message):
	print(message)
	sys.stdout.flush()


if __name__ == "__main__":
	app.run(debug = True, port = 80)