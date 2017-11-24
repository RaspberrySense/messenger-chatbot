import os
import random
import sys
import time

from flask import Flask, request
from pymessenger import Bot

from sensors import camera, humidity, light, temperature, motion
from replies import get_sensor_reply
import secrets


# Globals ---------------------------------------------------------------------
app = Flask(__name__)
bot = Bot(secrets.PAGE_ACCESS_TOKEN)
sender_id = None


# Helpers ---------------------------------------------------------------------
def get_bot():
    return bot


def get_sender_id():
    return sender_id


def log(message):
    print(message)
    sys.stdout.flush()


# Webhook verification --------------------------------------------------------
@app.route('/', methods=['GET'])
def verify():
    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    if mode and token:
        if mode == 'subscribe' and token == secrets.FACEBOOK_VERIFY_TOKEN:
            log('Webhook verified')
            return challenge, 200
        log('Verification token mismatch')
        return 'Verification token mismatch', 403

    return 'Nothing to do', 200


# -----------------------------------------------------------------------------
@app.route('/', methods=['POST'])
def webhook():
    global sender_id

    data = request.get_json()
    log(data)

    if data['object'] == 'page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:
                sender_id = messaging_event['sender']['id']
                recipient_id = messaging_event['recipient']['id']

                message_data = messaging_event.get('message')
                if message_data:
                    nlp_data = message_data.get('nlp')
                    if nlp_data:
                        intent_data = nlp_data['entities'].get('intent')
                        number_data = nlp_data['entities'].get('number')
                        if intent_data:
                            intent = intent_data[0]['value']
                            value = None
                            if number_data:
                                value = number_data[0]['value']
                            send_response(sender_id, intent, value)

    return 'OK', 200


# Send response ---------------------------------------------------------------
def send_response(sender_id, intent, value):
    # Temperature:
    if intent == 'get_temp':
        temp = temperature.get_temperature()
        response = get_sensor_reply('temperature', intent, value=temp)

    elif intent == 'check_temp_low':
        if temperature.is_cold():
            result = 'yes'
        elif temperature.is_hot():
            result = 'no'
        else:
            result = 'other'
        response = get_sensor_reply('temperature', intent, result)

    elif intent == 'check_temp_high':
        if temperature.is_hot():
            result = 'yes'
        elif temperature.is_cold():
            result = 'no'
        else:
            result = 'other'
        response = get_sensor_reply('temperature', intent, result)

    elif intent == 'check_temp_value_below':
        if value:
            if temperature.get_temperature() < value:
                result = 'yes'
            else:
                result = 'no'
            response = get_sensor_reply('temperature', intent, result, value)
        else:
            response = 'Can you phrase that more clearly, please'

    elif intent == 'check_temp_value_above':
        if value:
            if temperature.get_temperature() > value:
                result = 'yes'
            else:
                result = 'no'
            response = get_sensor_reply('temperature', intent, result, value)
        else:
            response = 'Can you phrase that more clearly, please'

    # Humidity:
    elif intent == 'get_humidity':
        humidity = humidity.get_humidity()
        response = get_sensor_reply('humidity', intent, value=humidity)

    elif intent == 'check_humidity_low':
        if humidity.is_dry():
            result = 'yes'
        elif humidity.is_humid():
            result = 'no'
        else:
            result = 'other'
        response = get_sensor_reply('humidity', intent, result)

    elif intent == 'check_humidity_high':
        if humidity.is_humid():
            result = 'yes'
        elif humidity.is_dry():
            result = 'no'
        else:
            result = 'other'
        response = get_sensor_reply('humidity', intent, result)

    elif intent == 'check_humidity_value_below':
        if value:
            if humidity.get_humidity() < value:
                result = 'yes'
            else:
                result = 'no'
            response = get_sensor_reply('humidity', intent, result, value)
        else:
            response = 'Can you phrase that more clearly, please'

    elif intent == 'check_humidity_value_above':
        if value:
            if humidity.get_humidity() > value:
                result = 'yes'
            else:
                result = 'no'
            response = get_sensor_reply('humidity', intent, result, value)
        else:
            response = 'Can you phrase that more clearly, please'

    # TODO: Light:
    elif intent == 'check_light_on_or_off':
        if light.is_light_on():
            response = 'Light is on'
        else:
            response = 'Light is off'

    elif intent == 'check_light_off':
        if not light.is_light_on():
            response = 'Yes'
        else:
            response = 'No'

    elif intent == 'check_light_on':
        if light.is_light_on():
            response = 'Yes'
        else:
            response = 'No'

    # Camera:
    elif intent == 'get_image':
        response = capture_image()

    # Motion:

    # Other:
    elif intent == 'get_greeting':
        response = random.choice(greeting_list)

    elif intent == 'get_thank':
        response = random.choice(thank_ret_list)

    elif intent == 'return_thank':
        response = random.choice(thank_list)

    elif intent == 'get_talk':
        response = random.choice(talk_list)

    else:
        response = "Sorry, I don't understand"

    bot.send_text_message(sender_id, response)


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True, port=80)
