from time import sleep

import pigpio
from sensors import DHT22


pi = pigpio.pi()
dht22 = DHT22.sensor(pi, 27)

HUMID_LOWER_LIMIT = 75  # percent
DRY_UPPER_LIMIT = 25    # percent

is_initialised = False


def init_sensor():
    dht22.trigger()
    sleep(0.5)
    global is_initialised
    is_initialised = True


def get_humidity():
    if not is_initialised:
        init_sensor()
    dht22.trigger()

    return dht22.humidity()


def is_humid():
    return get_humidity() >= HUMID_LOWER_LIMIT


def is_dry():
    return get_humidity() <= DRY_UPPER_LIMIT


def is_pleasant():
    return DRY_UPPER_LIMIT < get_humidity() < HUMID_LOWER_LIMIT
