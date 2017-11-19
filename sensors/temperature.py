import random

HOT_LOWER_LIMIT = 35      # Celsius
COLD_UPPER_LIMIT = 20     # Celsius


def get_temperature():
    return random.uniform(5, 40)


def is_hot():
    temperature = get_temperature()
    if temperature >= HOT_LOWER_LIMIT:
        return True
    return False


def is_cold():
    temp = get_temperature()
    if temperature <= COLD_UPPER_LIMIT:
        return True
    return False


def is_warm():
    temperature = get_temperature()
    if COLD_UPPER_LIMIT < temperature < HOT_LOWER_LIMIT:
        return True
    return False
