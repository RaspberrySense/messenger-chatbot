from collections import deque
import pickle
from threading import Timer, Thread

from gpiozero import MotionSensor, LED, LightSensor

import app
from replies import get_sensor_reply
from sensors import temperature, humidity, camera


MONITOR_RATE = 0.5      # seconds


def send_alert(alert_text):
    sender_id = None
    try:
        with open('data.pickle', 'rb') as file:
            sender_id = pickle.load(file)
    except:
        pass
    if sender_id:
        app.bot.send_text_message(sender_id, alert_text)

    return sender_id


# Motion sensor ---------------------------------------------------------------
def alert_motion_detected():
    send_alert(get_sensor_reply('motion', 'movement'))
    app.log('Motion detected')
    sender_id = send_alert(get_sensor_reply('motion', 'capturing'))
    if sender_id:
        t = Thread(target=app.send_video, args=(sender_id,))
        t.start()

motion_sensor = MotionSensor(17)
motion_sensor.when_motion = alert_motion_detected


# Light sensor ----------------------------------------------------------------
def alert_light_on():
    send_alert('The lights were just switched on')
    app.log('Lights switched on')


def alert_light_off():
    send_alert('The lights were just switched off')
    app.log('Lights switched off')

light_sensor = LightSensor(4, threshold=0.9)
light_sensor.when_light = alert_light_on
light_sensor.when_dark = alert_light_off


# Monitor ---------------------------------------------------------------------
temperature_values = deque(maxlen=20)
humidity_values = deque(maxlen=20)
red = LED(10)
cooldown_time = 0


def monitor():
    global cooldown_time
    cooldown_time -= 1 / MONITOR_RATE       # 1 second
    red.toggle()

    temperature_values.append(temperature.get_temperature())
    humidity_values.append(humidity.get_humidity())

    temperature_rate = ((temperature_values[-1] - temperature_values[0])
                        / (len(temperature_values) * MONITOR_RATE))
    if temperature_rate >= 2 and cooldown_time <= 0:
        send_alert('The temperature has been rising sharply at '
                   '{:.1f}° per second'.format(temperature_rate))
        app.log('Temperature increasing')
        cooldown_time = 30 / MONITOR_RATE      # 30 seconds
    elif temperature_rate <= -2 and cooldown_time <= 0:
        send_alert('The temperature has been dropping sharply at '
                   '{:.1f}° per second'.format(temperature_rate))
        app.log('Temperature decreasing')
        cooldown_time = 30 / MONITOR_RATE      # 30 seconds

    humidity_rate = ((humidity_values[-1] - humidity_values[0])
                     / (len(humidity_values) * MONITOR_RATE))
    if humidity_rate >= 2 and cooldown_time <= 0:
        send_alert('The humidity has been rising sharply at '
                   '{:.1f}% per second'.format(humidity_rate))
        app.log('Humidity increasing')
        cooldown_time = 30 / MONITOR_RATE      # 30 seconds
    elif humidity_rate <= -2 and cooldown_time <= 0:
        send_alert('The humidity has been dropping sharply at '
                   '{:.1f}% per second'.format(humidity_rate))
        app.log('Humidity decreasing')
        cooldown_time = 30 / MONITOR_RATE      # 30 seconds


if __name__ == '__main__':
    while True:
        t = Timer(MONITOR_RATE, monitor)
        t.start()
        t.join()
