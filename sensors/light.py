import random

BRIGHTNESS_THRESHOLD = 0.8      # min = 0, max = 1


def get_light_intensity():
    return random.uniform(0, 1)


def is_light_on():
    light_intensity = get_light_intensity()
    if light_intensity >= BRIGHTNESS_THRESHOLD:
        return True
    return False
