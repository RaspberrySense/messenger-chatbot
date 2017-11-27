import os
import pickle
import random
import sys
from time import sleep
from threading import Thread

from flask import Flask, request
from gpiozero import LED
from pymessenger2.bot import Bot

from sensors import camera, humidity, light, temperature
import replies
import secrets


green = LED(9)
green.on()

# Globals ---------------------------------------------------------------------
app = Flask(__name__)
bot = Bot(secrets.PAGE_ACCESS_TOKEN)


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

    data = request.get_json()
    log(data)

    if data['object'] == 'page':
        messaging_event = data['entry'][0]['messaging'][0]
        sender_id = messaging_event['sender']['id']
        with open('data.pickle', 'wb') as file:
            pickle.dump(sender_id, file)

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
        temp = '{:.1f}'.format(temperature.get_temperature())
        response = replies.get_sensor_reply('temperature', intent, value=temp)

    elif intent == 'check_temp_low':
        if temperature.is_cold():
            result = 'cold'
        elif temperature.is_hot():
            result = 'hot'
        else:
            result = 'warm'
        response = replies.get_sensor_reply('temperature', intent, result)

    elif intent == 'check_temp_high':
        if temperature.is_hot():
            result = 'hot'
        elif temperature.is_cold():
            result = 'cold'
        else:
            result = 'warm'
        response = replies.get_sensor_reply('temperature', intent, result)

    elif intent == 'check_temp_value_below':
        if value:
            if temperature.get_temperature() < value:
                result = 'yes'
            else:
                result = 'no'
            response = replies.get_sensor_reply('temperature', intent, result,
                                                value)
        else:
            response = 'Can you phrase that more clearly, please'

    elif intent == 'check_temp_value_above':
        if value:
            if temperature.get_temperature() > value:
                result = 'yes'
            else:
                result = 'no'
            response = replies.get_sensor_reply('temperature', intent, result,
                                                value)
        else:
            response = 'Can you phrase that more clearly, please'

    # Humidity:
    elif intent == 'get_humidity':
        hum = '{:.1f}'.format(humidity.get_humidity())
        response = replies.get_sensor_reply('humidity', intent, value=hum)

    elif intent == 'check_humidity_low':
        if humidity.is_dry():
            result = 'dry'
        elif humidity.is_humid():
            result = 'humid'
        else:
            result = 'pleasant'
        response = replies.get_sensor_reply('humidity', intent, result)

    elif intent == 'check_humidity_high':
        if humidity.is_humid():
            result = 'humid'
        elif humidity.is_dry():
            result = 'dry'
        else:
            result = 'pleasant'
        response = replies.get_sensor_reply('humidity', intent, result)

    elif intent == 'check_humidity_value_below':
        if value:
            if humidity.get_humidity() < value:
                result = 'yes'
            else:
                result = 'no'
            response = replies.get_sensor_reply('humidity', intent, result,
                                                value)
        else:
            response = replies.get_did_not_understand_reply()

    elif intent == 'check_humidity_value_above':
        if value:
            if humidity.get_humidity() > value:
                result = 'yes'
            else:
                result = 'no'
            response = replies.get_sensor_reply('humidity', intent, result,
                                                value)
        else:
            response = replies.get_did_not_understand_reply()

    # Light:
    elif intent == 'check_light_on_or_off':
        if light.is_light_on():
            result = 'on'
        else:
            result = 'off'
        response = replies.get_sensor_reply('light', intent, result)

    elif intent == 'check_light_off':
        if not light.is_light_on():
            result = 'yes'
        else:
            result = 'no'
        response = replies.get_sensor_reply('light', intent, result)

    elif intent == 'check_light_on':
        if light.is_light_on():
            result = 'yes'
        else:
            result = 'no'
        response = replies.get_sensor_reply('light', intent, result)

    # Camera:
    elif intent == 'get_image':
        response = replies.get_sensor_reply('camera', 'hold_on')
        t = Thread(target=send_images, args=(sender_id,))
        t.start()

    elif intent == 'get_images':
        response = replies.get_sensor_reply('camera', 'hold_on')
        num_images = value if value else 3
        t = Thread(target=send_images, args=(sender_id, num_images))
        t.start()

    elif intent == 'get_video':
        response = replies.get_sensor_reply('camera', 'hold_on')
        t = Thread(target=send_video, args=(sender_id,))
        t.start()

    # Other:
    elif intent == 'get_greeting':
        response = replies.get_hello()

    elif intent == 'get_thank_reply':
        response = replies.get_thank_reply()

    elif intent == 'get_thank':
        response = replies.get_thank()

    elif intent == 'get_talk':
        response = replies.get_fine_reply()

    else:
        response = replies.get_did_not_understand_reply()

    bot.send_text_message(sender_id, response)


def send_images(sender_id, num_images=1):
    for i in range(num_images):
        sleep(1)
        image_path = camera.capture_image()
        log(image_path)
        bot.send_image(sender_id, image_path)


def send_video(sender_id):
    video_path = camera.capture_video()
    log(video_path)
    bot.send_video(sender_id, video_path)
