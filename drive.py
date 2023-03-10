import time

from constants.ports import LEFT_MOTOR, RIGHT_MOTOR, TOP_HAT
from kipr import motor_power, msleep, analog, freeze, clear_motor_position_counter, get_motor_position_counter
from common import ROBOT


def drive(left_speed, right_speed, duration):
    motor_power(LEFT_MOTOR, left_speed)
    motor_power(RIGHT_MOTOR, right_speed)
    msleep(duration)


def drive_straight(duration, direction=1):         # direction is 1 for forward or -1 for reverse defaults to 1
    if ROBOT.is_yellow:
        drive(direction * 100, direction * 97, duration)
    if ROBOT.is_blue:
        drive(direction * 95, direction * 100, duration)
    if ROBOT.is_red:
        drive(direction * 100, direction * 94, duration)
    if ROBOT.is_green:
        drive(direction * 100, direction * 100, duration)


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
            if ROBOT.is_yellow:
                drive(84, 100, 10)
            elif ROBOT.is_blue:
                drive(80, 100, 10)
            elif ROBOT.is_red:
                drive(88, 100, 10)
            elif ROBOT.is_green:
                drive(80, 100, 10)
            else:
                print("Robot unidentified in line-follow")
        else:  # on black
            x += 10
            if ROBOT.is_yellow:
                drive(100, 80, 10)
            elif ROBOT.is_blue:
                drive(100, 85, 10)
            elif ROBOT.is_red:
                drive(100, 80, 10)
            elif ROBOT.is_green:
                drive(100, 80, 10)
            else:
                print("Robot unidentified in line-follow")


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


def line_follow_to_ddos(duration):  # less aggressive
    """
    following left side of black line
    :param duration: time in ms
    :redrive:
    """

    x = 0
    while x < duration:
        if analog(TOP_HAT) < 1800:  # on white
            x += 10
            drive(100, 90, 10)
        else:  # on black
            x += 10
            drive(85, 100, 10)


def line_follow_right(duration):
    """
    following right side of black line
    :param duration: time in ms
    :redrive:
    """

    x = 0
    while x < duration:
        if analog(TOP_HAT) < 1800:  # on white
            x += 10
            drive(85, 100, 10)
        else:  # on black
            x += 10
            drive(100, 80, 10)


def line_follow_to_ws(duration):
    """
    following left side of black line
    :param duration: time in ms
    :redrive:
    """

    x = 0
    while x < duration:
        if analog(TOP_HAT) < 1800:  # on white
            x += 10
            drive(100, 70, 10)
        else:  # on black
            x += 10
            drive(65, 100, 10)


def line_follow_right_lego1(duration, direction=1):
    duration = duration // 1000

    start_time = time.time()

    while time.time() - start_time < duration:
        if analog(TOP_HAT) > 3100:
            drive(0, *([direction * 90, direction * 20][::direction]))
        elif analog(TOP_HAT) < 2600:
            drive(0, *([direction * 40, direction * 90][::direction]))
        else:
            drive(0, direction * 85, direction * 85)


def stop_motors():
    freeze(LEFT_MOTOR)
    freeze(RIGHT_MOTOR)
    msleep(500)
