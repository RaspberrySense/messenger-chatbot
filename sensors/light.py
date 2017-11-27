from gpiozero import LightSensor


LIGHT_THRESHOLD = 0.9       # min = 0, max = 1
ldr = None


def init_sensor():
    global ldr
    if not ldr:
        ldr = LightSensor(4, threshold=LIGHT_THRESHOLD)


def is_light_on():
    init_sensor()
    return ldr.light_detected
