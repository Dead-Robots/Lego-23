from kipr import msleep, push_button, disable_servos, freeze
from constants.ports import LEFT_MOTOR, RIGHT_MOTOR


def wait_for_button(text="waiting for button"):
    stop_motors()
    print(text)
    while not push_button():
        pass
    msleep(1000)


def stop_motors(stop_time=400):
    freeze(LEFT_MOTOR)
    freeze(RIGHT_MOTOR)
    msleep(stop_time)


def debug():
    disable_servos()
    stop_motors()
    print("stopping code for debug")
    exit(0)
