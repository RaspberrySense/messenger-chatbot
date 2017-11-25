import os
from collections import deque
from threading import Timer

from gpiozero import MotionSensor, LED, LightSensor

from app import get_sender_id, get_bot
from replies import get_sensor_reply
from sensors import temperature, humidity, camera


bot = get_bot()


def send_alert(alert_text):
    sender_id = get_sender_id()
    if sender_id:
        bot.send_text_message(sender_id, alert_text)


# Motion sensor ---------------------------------------------------------------
def alert_motion_detected():
    send_alert(get_sensor_reply('motion', 'something_moved'))

motion_sensor = MotionSensor(17)
motion_sensor.when_motion = alert_motion_detected


# Light sensor ----------------------------------------------------------------
def alert_light_on():
    send_alert('The lights were just switched on')


def alert_light_off():
    send_alert('The lights were just switched off')

light_sensor = LightSensor(4, threshold=0.9)
light_sensor.when_light = alert_light_on
light_sensor.when_dark = alert_light_off


# Regression ------------------------------------------------------------------
temperature_values = deque(maxlen=20)
humidity_values = deque(maxlen=20)


def best_fit_slope(X, Y):
    x_bar = sum(X) / len(X)
    y_bar = sum(Y) / len(Y)
    n = len(X)

    numer = sum([xi*yi for xi, yi in zip(X, Y)]) - n * x_bar * y_bar
    denum = sum([xi**2 for xi in X]) - n * x_bar**2

    return numer / denum


def get_temperature_rate():
    time = list(range(1, len(temperature_values) + 1))
    temperature_rate = best_fit_slope(list(temperature_values), time)

    return temperature_rate


def get_humidity_rate():
    time = list(range(1, len(humidity_values) + 1))
    humidity_rate = best_fit_slope(list(humidity_values), time)

    return humidity_rate


# Monitor ---------------------------------------------------------------------
red = LED(10)


def monitor():
    red.toggle()

    temperature_values.append(temperature.get_temperature())
    humidity_values.append(humidity.get_humidity())

    os.system('cls' if os.name == 'nt' else 'clear')
    temperature_rate = get_temperature_rate()   # ° per sec
    if temperature_rate >= 2:
        send_alert('The temperature has been rising sharply at '
                   '{:.1f}° per second'.format(temperature_rate))
    elif temperature_rate <= -2:
        send_alert('The temperature has been dropping sharply at '
                   '{:.1f}° per second'.format(temperature_rate))

    humidity_rate = get_humidity_rate()     # % per sec
    if humidity_rate >= 4:
        send_alert('The humidity has been rising sharply at '
                   '{:.1f}% per second'.format(humidity_rate))
    elif humidity_rate <= -4:
        send_alert('The humidity has been dropping sharply at '
                   '{:.1f}% per second'.format(humidity_rate))


if __name__ == '__main__':
    temperature.init_sensor()
    humidity.init_sensor()

    while True:
        t = Timer(0.5, monitor)     # monitor every 0.5 seconds
        t.start()
        t.join()

