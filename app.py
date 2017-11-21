import os, sys
import random
import time
from flask import Flask, request
from pymessenger import Bot
import secrets
from sensors.camera import capture_image
from sensors.temperature import is_cold, is_hot, is_warm, get_temperature
from sensors.humidity import is_dry, is_humid, is_pleasant, get_humidity
from sensors.light import is_light_on

app = Flask(__name__)

bot = Bot(secrets.PAGE_ACCESS_TOKEN)

greeting_list = ['hi','hey','hello','Hi','Hello','Hey']
thank_list = ['Thanks','Thank you','thank you']
thank_ret_list = ['No problem ☺',"It's my job",'I am happy to help you', "It's my pleasure to serve you",'😇','☺']
talk_list = ["I'm good"," I'm fine","I'm ok"]

@app.route('/', methods=['GET'])
def verify():
    #Webhook verification
    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    if mode and token:
        if mode == 'subscribe' and token == secrets.FACEBOOK_VERIFY_TOKEN:
            log('webhook verified')
            return challenge, 200
        log('Verification token mismatch')
        return 'Verification token mismatch', 403
    return 'Nothing to do', 200

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    log(data)

    if data['object'] == 'page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:

                # IDs
                sender_id = messaging_event['sender']['id']
                SENDER_ID = sender_id
                recipient_id = messaging_event['recipient']['id']
                message = messaging_event.get('message')
                if message:
                    nlp_data = message.get('nlp')
                    if nlp_data:
                        intent_data = nlp_data['entities'].get('intent')
                        number_data = nlp_data['entities'].get('number')
                        #bot.send_text_message(sender_id, str(number_data))
                        if intent_data:
                            intent = intent_data[0]['value']
                                        #entity, value_list = messaging_event['message']['nlp']['entities'].items()
                                        #value = value_list[0]['value']

                            if intent == "get_temp":                            
                                response = '{:.2f}°C'.format(get_temperature())                   
                            elif intent == "check_temp_low":                                
                                if is_cold():
                                    response = "Yes"
                                elif is_warm():
                                    response = "Temperature is not low, it's normal"
                            elif intent == "check_temp_high":                   
                                if is_hot():
                                    response = "Yes"
                                elif is_warm():
                                    response = "Temperature is not high, it's normal"
                            elif intent == "check_temp_value_below":
                                if number_data:
                                    num = number_data[0]['value']
                                    if get_temperature() < num:
                                        response = "Yes, it's below {}°C".format(num)
                                    else:
                                        response = "No, it's not below {}°C".format(num)
                                else:
                                    response = "below what?"
                            elif intent == "check_temp_value_above":
                                if number_data:
                                    num = number_data[0]['value']
                                    if get_temperature() > num:
                                        response = "Yes, it's above {}°C".format(num)
                                    else:
                                        response = "No, it's not above {}°C".format(num)
                                else:
                                    response = "above what?"
                            elif intent == "get_humidity":
                                response = '{:.1%}'.format(get_humidity())
                            elif intent == "check_humidity_low":
                                if is_dry():
                                    response = "Yes"
                                elif is_pleasant():
                                    response = "Humidity is not low, it's normal"
                            elif intent == "check_humidity_high":
                                if is_humid():
                                    response = "Yes"
                                elif is_pleasant():
                                    response = "Humidity is not high, it's normal"
                            elif intent == "check_humidity_value_below":
                                if number_data:
                                    num = number_data[0]['value']
                                    num = num/100
                                    if get_humidity() < num:
                                        response = "Yes, it's below {}%".format(num)
                                    else:
                                        response = "No, it's not below {}%".format(num)
                                else:
                                    response = "below what?"
                            elif intent == "check_humidity_value_above":
                                if number_data:
                                    num = number_data[0]['value']
                                    num = num/100
                                    if get_humidity() > num:
                                        response = "Yes, it's above {}%".format(num)
                                    else:
                                        response = "No, it's not above {}%".format(num)
                                else:
                                    response = "above what?"
                            elif intent == "check_light_on_or_off":
                                if is_light_on():
                                    response = "Light is on"
                                else:
                                    response = "Light is off"
                            elif intent == "check_light_off":
                                if is_light_on() == False:
                                    response = "Yes"
                                else:
                                    response = "No"
                            elif intent == "check_light_on":
                                if is_light_on():
                                    response = "Yes"
                                else:
                                    response = "No"
                            elif intent == "get_image":
                                response = capture_image()
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



    return "ok", 200


def log(message):
    print(message)
    sys.stdout.flush()


if __name__ == "__main__":
    app.run(debug = True, port = 80)