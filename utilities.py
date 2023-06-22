from kipr import msleep, push_button, disable_servos, freeze
from constants.ports import LEFT_MOTOR, RIGHT_MOTOR, SERVO_REPLACEMENT


def wait_for_button(text="waiting for button"):
    stop_motors()
    print(text)
    while not push_button():
        msleep(50)
    msleep(1000)


def stop_motors(stop_time=400, stop_servo_replacement=True):
    freeze(LEFT_MOTOR)
    freeze(RIGHT_MOTOR)
    if stop_servo_replacement:
        freeze(SERVO_REPLACEMENT)
    msleep(stop_time)


def debug():
    disable_servos()
    stop_motors()
    print("stopping code for debug")
    exit(0)
