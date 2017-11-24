from gpiozero import LightSensor


LIGHT_THRESHOLD = 0.9		# min = 0, max = 1
ldr = LightSensor(4, LIGHT_THRESHOLD)


def is_light_on():
    return ldr.light_detected()
