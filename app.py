import os
import sys
import random
from flask import Flask, request
from utils import wit_response
from pymessenger import Bot
import secrets

app = Flask(__name__)

bot = Bot(secrets.PAGE_ACCESS_TOKEN)

greeting_list = ['hi', 'hey', 'hello', "what's up", 'Hi', 'Hello', 'Hey']
thank_list = ['Thanks', 'Thank you', 'Thank you very much',
              'thanks', 'thank you', 'thank you very much']
thank_ret_list = ['No problem', "It's my job",
                  'I am happy to help you', "It's my pleasure to serve you",
                  '😇', '☺']


# Webhook verification
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

                nlp_data = messaging_event['message'].get('nlp')
                if nlp_data:
                    intent_data = nlp_data['entities'].get('intent')
                    if intent_data:
                        intent = intent_data[0]['value']
                        # entity, value_list = nlp_data['entities'].items()
                        # value = value_list[0]['value']

                        if intent == 'get_temp':
                            temp_value = 'temp_script()'
                            response = 'temp_value'
                        elif intent == 'check_temp_low':
                            response = 'check_temp_low()'
                        elif intent == 'check_temp_high':
                            response = 'check_temp_high()'
                        elif intent == 'get_humidity':
                            response = 'humidity_script()'
                        elif intent == 'check_humidity_low':
                            response = 'check_humidity_low()'
                        elif intent == 'check_humidity_high':
                            response = 'check_humidity_high()'
                        elif intent == 'check_light_on_or_off':
                            response = 'lights on'
                        elif intent == 'check_light_off':
                            response = 'check_light_off()'
                        elif intent == 'check_light_on':
                            response = 'check_light_on()'
                        elif intent == 'get_image':
                            response = 'get_image()'
                        elif intent == 'get_greeting':
                            response = random.choice(greeting_list)
                        elif intent == 'get_thank':
                            response = random.choice(
                                thank_ret_list)
                        elif intent == 'return_thank':
                            response = random.choice(thank_list)
                        elif intent == 'get_talk':
                            response = random.choice(talk_list)
                        else:
                            response = "Sorry! I didn't understand"
                            bot.send_text_message(sender_id, response)

    return 'OK', 200


def log(message):
    print(message)
    sys.stdout.flush()


if __name__ == '__main__':
    app.run(debug=True, port=80)
