from time import sleep

import pigpio
import DHT22


pi = pigpio.pi()
dht22 = DHT22.sensor(pi, 27)

HOT_LOWER_LIMIT = 35    # Celsius
COLD_UPPER_LIMIT = 25   # Celsius


def init_sensor():
    dht22.trigger()
    sleep(0.5)


def get_temperature():
    dht22.trigger()

    return dht22.temperature()


def is_hot():
    return get_temperature() >= HOT_LOWER_LIMIT


def is_cold():
    return get_temperature() <= COLD_UPPER_LIMIT


def is_warm():
    return COLD_UPPER_LIMIT < get_temperature() < HOT_LOWER_LIMIT
