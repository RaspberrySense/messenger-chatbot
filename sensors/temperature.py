from time import sleep

import pigpio
from sensors import DHT22


pi = pigpio.pi()
dht22 = DHT22.sensor(pi, 27)

HOT_LOWER_LIMIT = 35    # Celsius
COLD_UPPER_LIMIT = 25   # Celsius

is_initialised = False


def init_sensor():
    dht22.trigger()
    sleep(0.5)
    global is_initialised
    is_initialised = True


def get_temperature():
    if not is_initialised:
        init_sensor()
    dht22.trigger()

    return dht22.temperature()


def is_hot():
    return get_temperature() >= HOT_LOWER_LIMIT


def is_cold():
    return get_temperature() <= COLD_UPPER_LIMIT


def is_warm():
    return COLD_UPPER_LIMIT < get_temperature() < HOT_LOWER_LIMIT
