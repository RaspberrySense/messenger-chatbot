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
				'''value1 = light_script()
				if value1 < 10 and value1 > 5:
					bot.send_text_message(sender_id, value1)'''

				##############################################

				# FROM HERE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
				if messaging_event.get('message'):

					# Extracting text message

					if 'text' in messaging_event['message']:
						messaging_text = messaging_event['message']['text']
						entity_list, intent = wit_response(messaging_text)
						bot.send_text_message(sender_id, messaging_event['message']['nlp']['entities'])
						# selecting action to be done

						if intent == "get_temp":							#T
							temp_value = 'temp_script()'
							response = 'temp_value'							#E
						elif intent == "check_temp_low":
							if value == "cold":								#M
								response = 'check_temp_low()'
							else:											#P
								response = None
						elif intent == "check_temp_high":					#E
							if value == "hot":
								response = 'check_temp_high()'
							else:
								response = None
						elif intent == "get_humidity":
							response = 'humidity_script()'
						elif intent == "check_humidity_low":
							if value == "dry":
								response = 'check_humidity_low()'
							else:
								response = None
						elif intent == "check_humidity_high":
							if value == "humid":
								response = 'check_humidity_high()'
							else:
								response = None
						elif intent == "check_light_on_or_off":
							#if is_light_on():
							response = "lights on"
							#else:
								#response "lights off"
						elif intent == "check_light_off":
							if value == "dark":
								response = 'check_light_off()'
							else:
								response = None
						elif intent == "check_light_on":
							if value == "bright":
								response = 'check_light_on()'
							else:
								response = None
						elif intent == "get_image":
							if value == "image":
								response = 'get_image()'
							elif value == "images":
								#for img in wit/number:
								response = 'get_image()'
									#bot.send_text_message(sender_id, response)
									#time.sleep(60)
								#flag_status = "Sent"
						else:
							response = intent
								



				
					bot.send_text_message(sender_id, response)

					# TILL HERE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

	return "ok", 200


def log(message):
	print(message)
	sys.stdout.flush()


if __name__ == "__main__":
	app.run(debug = True, port = 80)