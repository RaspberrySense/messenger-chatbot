import random

HUMID_LOWER_LIMIT = 0.8     # min = 0, max = 1
DRY_UPPER_LIMIT = 0.2       # min = 0, max = 1


def get_humidity():
    return random.uniform(0, 1)


def is_humid():
    humidity = get_humidity()
    if humidity >= HUMID_LOWER_LIMIT:
        return True
    return False


def is_dry():
    humidity = get_humidity()
    if humidity <= DRY_UPPER_LIMIT:
        return True
    return False


def is_pleasant():
    humidity = get_humidity()
    if DRY_UPPER_LIMIT < humidity < HUMID_LOWER_LIMIT:
        return True
    return False
