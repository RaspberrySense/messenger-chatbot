from random import choice, randint


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


hello = [
    'hello',
    'hey there',
    'hey',
    'hi',
]


def get_hello():
    return randomly_capitalize(choice(hello))


thanks = [
    'thank you',
    'thanks',
]


def get_thank():
    return randomly_capitalize(choice(thanks)) + ' ' + random_smiley()


thank_replies = [
    "you're welcome",
    'happy to help',
    'my pleasure'
    'no problem',
    'no probs',
]


def get_thank_reply():
    return randomly_capitalize(choice(thank_replies)) + random_exclamation()


fine_replies = [
    "i'm good",
    "i'm fine",
    "i'm OK"
]


def get_fine_reply():
    return randomly_capitalize(choice(fine_replies)) + random_exclamation()


did_not_understand = [
    "i didn't get that",
    "i don't get what you're saying :/",
    "i don't understand :/",
    "sorry I don't understand",
    "sorry, I don't get what you're saying",
    'say what?',
    'this does not mean anything to me',
]


def get_did_not_understand_reply():
    return randomly_capitalize(choice(did_not_understand))


yes = [
    'yes',
    'yeah',
    'yep'
]


def get_yes():
    return choice(yes)


no = [
    'no',
    'nah',
    'nope'
]


def get_no():
    return choice(no)


sensor_replies = {
    'temperature': {
        'get_temp': {
            'default': [
                "It is {value}° in here",
                "It's {value}°",
                "The temperature is {value}° in here",
                "The temperature is {value}°",
                "{value}°",
            ]
        },
        'check_temp_high': {
            'hot': [
                "{yes}",
                "{yes}, it is",
                "{yes}, it's quite hot",
                "{yes}, it's hot in here",
                "{yes}, it's quite hot in here",
            ],
            'cold': [
                "{no}",
                "{no}, it's not",
                "{no}, it's rather quite cold",
                "{no}, it's actually quite cold",
                "{no}, it's actually quite cold in here",
            ],
            'warm': [
                "{no}",
                "{no}, it's warm",
                "{no}, it's actually quite warm",
                "{no}, it's actually quite warm in here",
            ]
        },
        'check_temp_low': {
            'cold': [
                "{yes}",
                "{yes}, it is",
                "{yes}, it's quite cold",
                "{yes}, it's cold in here",
                "{yes}, it's quite cold in here",
            ],
            'hot': [
                "{no}",
                "{no}, it's not",
                "{no}, it's rather quite hot",
                "{no}, it's actually quite hot",
                "{no}, it's actually quite hot in here",
            ],
            'warm': [
                "{no}",
                "{no}, it's warm",
                "{no}, it's actually quite warm",
                "{no}, it's actually quite warm in here",
            ]
        },
        'check_temp_value_above': {
            'yes': [
                "{yes}",
                "{yes}, it is",
                "{yes}, it's above {value}°",
                "{yes}, it's above {value}° in here",
            ],
            'no': [
                "{no}",
                "{no}, it's not",
                "{no}, it's below {value}°",
                "{no}, it's below {value}° in here",
            ]
        },
        'check_temp_value_below': {
            'yes': [
                "{yes}",
                "{yes}, it is",
                "{yes}, it's below {value}°",
                "{yes}, it's below {value}° in here",
            ],
            'no': [
                "{no}",
                "{no}, it's not",
                "{no}, it's above {value}°",
                "{no}, it's above {value}° in here",
            ]
        },
    },

    # Humidity ----------------------------------------------------------------
    'humidity': {
        'get_humidity': {
            'default': [
                "It is {value}% in here",
                "It's {value}%",
                "The humidity is {value}% in here",
                "The humidity is {value}%",
                "{value}%",
            ]
        },
        'check_humidity_high': {
            'humid': [
                "{yes}",
                "{yes}, it is",
                "{yes}, it's quite humid",
                "{yes}, it's humid in here",
                "{yes}, it's quite humid in here",
            ],
            'dry': [
                "{no}",
                "{no}, it's not",
                "{no}, it's rather quite dry",
                "{no}, it's actually quite dry",
                "{no}, it's actually quite dry in here",
            ],
            'pleasant': [
                "{no}",
                "{no}, it's pleasant",
                "{no}, it's actually quite pleasant",
                "{no}, it's actually quite pleasant in here",
            ]
        },
        'check_humidity_low': {
            'dry': [
                "{yes}",
                "{yes}, it is",
                "{yes}, it's quite dry",
                "{yes}, it's dry in here",
                "{yes}, it's quite dry in here",
            ],
            'humid': [
                "{no}",
                "{no}, it's not",
                "{no}, it's rather quite humid",
                "{no}, it's actually quite humid",
                "{no}, it's actually quite humid in here",
            ],
            'pleasant': [
                "{no}",
                "{no}, it's pleasant",
                "{no}, it's actually quite pleasant",
                "{no}, it's actually quite pleasant in here",
            ]
        },
        'check_humidity_value_above': {
            'yes': [
                "{yes}",
                "{yes}, it is",
                "{yes}, it's above {value}%",
                "{yes}, it's above {value}% in here",
            ],
            'no': [
                "{no}",
                "{no}, it's not",
                "{no}, it's below {value}%",
                "{no}, it's below {value}% in here",
            ]
        },
        'check_humidity_value_below': {
            'yes': [
                "{yes}",
                "{yes}, it is",
                "{yes}, it's below {value}%",
                "{yes}, it's below {value}% in here",
            ],
            'no': [
                "{no}",
                "{no}, it's not",
                "{no}, it's above {value}%",
                "{no}, it's above {value}% in here",
            ]
        },
    },

    # Light ----------------------------------------------------------------
    'light': {
        'check_light_on_or_off': {
            'on': [
                'on',
                'the lights are on'
            ],
            'off': [
                'off',
                'the lights are off'
            ],
        },
        'check_light_off': {
            'yes': [
                '{yes}',
                '{yes}, the lights are off'
            ],
            'no': [
                '{no}',
                '{no}, the lights are on',
            ],
        },
        'check_light_on': {
            'yes': [
                '{yes}',
                '{yes}, the lights are on',
            ],
            'no': [
                '{no}',
                '{no}, the lights are off',
            ],
        },
    },

    # Camera ----------------------------------------------------------------
    'camera': {
        'any': {
            'hold_on': [
                "capturing...",
                "hold on, capturing...",
                "hold on...",
                "please wait...",
                "wait...",
            ],
        },
    },
}


def get_sensor_reply(sensor_type, intent, result='default', value=None):
    reply = choice(sensor_replies[sensor_type][intent][result])

    if '{yes}' in reply:
        if '{value}' in reply:
            reply = reply.format(yes=get_yes(), value=value)
        else:
            reply = reply.format(yes=get_yes())
    elif '{no}' in reply:
        if '{value}' in reply:
            reply = reply.format(no=get_no(), value=value)
        else:
            reply = reply.format(no=get_no())
    elif '{value}' in reply:
        reply = reply.format(value=value)

    return randomly_capitalize(reply)
