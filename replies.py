from random import choice, randint
from replies_data import *


def randomly_capitalize(text):
    if randint(0, 2):   # randomly decide whether to capitalize
        return text.capitalize()
    return text


def random_smiley(can_be_empty=True):
    # NOTE: `☺` is more probable if smiley cannot be empty
    return choice([':)', '☺', '😇', '' if can_be_empty else '☺'])


def random_exclamation(can_be_empty=True):
    # NOTE: `!` is more probable if exclamation cannot be empty
    return choice(['!', '.', '' if can_be_empty else '!'])


def get_hello():
    return randomly_capitalize(choice(hello))


def get_thank():
    return randomly_capitalize(choice(thanks)) + ' ' + random_smiley()


def get_thank_reply():
    return randomly_capitalize(choice(thank_replies)) + random_exclamation()


def get_fine_reply():
    return randomly_capitalize(choice(fine_replies)) + random_exclamation()


def get_did_not_understand_reply():
    return randomly_capitalize(choice(did_not_understand))


def get_sensor_reply(sensor_type, intent, result='default', value=None):
    reply = choice(sensor_replies[sensor_type][intent][result])

    kwargs = {}
    if '{value}' in reply:
        kwargs['value'] = value
    if '{yes}' in reply:
        kwargs['yes'] = choice(yes)
    if '{no}' in reply:
        kwargs['no'] = choice(no)
    reply = reply.format_map(kwargs)

    return randomly_capitalize(reply)
