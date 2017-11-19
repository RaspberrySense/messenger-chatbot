import random

MOTION_THRESHOLD = 0.7      # min = 0, max = 1


def get_motion_value():
    return random.uniform(0, 1)


def is_motion_detected():
    motion_value = get_motion_value()
    if motion_value >= MOTION_THRESHOLD:
        return True
    return False
