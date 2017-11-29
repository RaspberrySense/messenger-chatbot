hello = [
    'hello',
    'hey there',
    'hey',
    'hi',
]

thanks = [
    'thank you',
    'thanks',
]

thank_replies = [
    "you're welcome",
    'happy to help',
    'my pleasure',
    'no problem',
    'no probs',
]

fine_replies = [
    "i'm good",
    "i'm fine",
    "i'm OK",
]

did_not_understand = [
    "i didn't get that",
    "i don't get what you're saying :/",
    "i don't understand :/",
    "sorry I don't understand",
    "sorry, I don't get what you're saying",
    'say what?',
    'this does not mean anything to me',
]

yes = [
    'yes',
    'yeah',
    'yep',
]

no = [
    'no',
    'nah',
    'nope',
]

sensor_replies = {
    'temperature': {
        'get_temp': {
            'default': [
                "it is {value}° in here",
                "it's {value}°",
                "the temperature is {value}° in here",
                "the temperature is {value}°",
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
                "it is {value}% in here",
                "it's {value}%",
                "the humidity is {value}% in here",
                "the humidity is {value}%",
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
                'the lights are on',
            ],
            'off': [
                'off',
                'the lights are off',
            ],
        },
        'check_light_off': {
            'yes': [
                '{yes}',
                '{yes}, the lights are off',
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
        'hold_on': {
            'default': [
                'capturing...',
                'hold on, capturing...',
                'hold on...',
                'please wait...',
                'wait...',
            ],
        },
    },

    # Motion ----------------------------------------------------------------
    'motion': {
        'movement': {
            'default': [
                'something moved',
                'i detected a movement',
                'movement detected',
                'i sense some movement',
            ],
        },
        'capturing': {
            'default': [
                "recording a video of what's happening...",
                'capturing a video for you...',
                'capturing a video...',
                'recording a video for you...',
                'recording a video...',
                'sending you a video...',
            ],
        }
    },
}
