from constants.ports import LEFT_MOTOR, RIGHT_MOTOR, TOP_HAT
from kipr import motor_power, msleep, analog, freeze, clear_motor_position_counter, get_motor_position_counter


def drive(left_speed, right_speed, duration):
    motor_power(LEFT_MOTOR, left_speed)
    motor_power(RIGHT_MOTOR, right_speed)
    msleep(duration)


def line_follow(duration):
    """
    following right side of black line
    :param duration: time in ms
    :redrive:
    """
    x = 0
    while x < duration:
        if analog(TOP_HAT) < 1800:  # on white
            x += 10
            drive(80, 100, 10)
        else:  # on black
            x += 10
            drive(100, 85, 10)


def line_follow_left(duration):
    """
    following left side of black line
    :param duration: time in ms
    :redrive:
    """

    x = 0
    while x < duration:
        if analog(TOP_HAT) < 1800:  # on white
            x += 10
            drive(100, 85, 10)
        else:  # on black
            x += 10
            drive(80, 100, 10)


def stop_motors():
    freeze(LEFT_MOTOR)
    freeze(RIGHT_MOTOR)
    msleep(500)
