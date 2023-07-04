import time
import os

from common.gyro_movements import straight_drive
from constants.ports import LEFT_MOTOR, RIGHT_MOTOR, LEFT_TOP_HAT, RIGHT_TOP_HAT, GRAYSON
from constants.sensors import TOP_HAT_THRESHOLD, TOP_HAT_THRESHOLD_GREY
from kipr import motor_power, analog, clear_motor_position_counter, get_motor_position_counter, digital, freeze
from common import ROBOT
from utilities import msleep


def drive(left_speed, right_speed, duration):
    motor_power(LEFT_MOTOR, left_speed)
    motor_power(RIGHT_MOTOR, right_speed)
    msleep(duration)


def enable_grayson():
    motor_power(GRAYSON, 100)


def left_on_black():
    return analog(LEFT_TOP_HAT) > TOP_HAT_THRESHOLD


def left_on_white():
    return analog(LEFT_TOP_HAT) < TOP_HAT_THRESHOLD


def right_on_black():
    return analog(RIGHT_TOP_HAT) > TOP_HAT_THRESHOLD


def right_on_white():
    return analog(RIGHT_TOP_HAT) < TOP_HAT_THRESHOLD


def line_follow(duration):
    """
    following right side of black line
    :param duration: time in ms
    """
    x = 0
    while x < duration:
        if analog(LEFT_TOP_HAT) < TOP_HAT_THRESHOLD_GREY:  # on white or grey
            x += 10
            if ROBOT.is_yellow:
                drive(84, 100, 10)
            elif ROBOT.is_blue:
                drive(80, 100, 10)
            elif ROBOT.is_red:
                drive(80, 100, 10)
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


def line_follow_right(duration):
    """
    following right side of black line
    :param duration: time in ms
    """

    x = 0
    while x < duration:
        if analog(LEFT_TOP_HAT) < TOP_HAT_THRESHOLD:  # on white
            x += 10
            drive(65, 100, 10)
        else:  # on black
            x += 10
            drive(100, 62, 10)


def drive_until_black(left_motor, right_motor, top_hat=None, stop=True):
    drive(left_motor, right_motor, 0)
    if top_hat is None:
        while right_on_white() and left_on_white():
            pass
    else:
        while analog(top_hat) < TOP_HAT_THRESHOLD:
            pass
    if stop:
        stop_motors()


def drive_until_both_black(left_motor, right_motor, top_hat=None, stop=True):
    drive(left_motor, right_motor, 0)
    if top_hat is None:
        while right_on_white() and left_on_white():
            pass
    else:
        while analog(top_hat) < TOP_HAT_THRESHOLD:
            pass
    if stop:
        stop_motors()


def drive_until_white(left_motor, right_motor, top_hat=None, stop=True):
    drive(left_motor, right_motor, 0)
    if top_hat is None:
        while right_on_black() and left_on_black():
            pass
    else:
        while analog(top_hat) > TOP_HAT_THRESHOLD:
            pass
    if stop:
        stop_motors()


def drive_until_both_white(left_motor, right_motor, top_hat=None, stop=True):
    drive(left_motor, right_motor, 0)
    if top_hat is None:
        while right_on_black() or left_on_black():
            pass
    else:
        while analog(top_hat) > TOP_HAT_THRESHOLD:
            pass
    if stop:
        stop_motors()


def straight_drive_until_black_left(speed, stop_when_finished=True):
    def condition():
        return left_on_white()

    straight_drive(speed, condition, stop_when_finished)


def straight_drive_until_black_right(speed, stop_when_finished=True):
    def condition():
        return right_on_white()

    straight_drive(speed, condition, stop_when_finished)


def straight_drive_until_white_left(speed, stop_when_finished=True):
    def condition():
        return left_on_black()

    straight_drive(speed, condition, stop_when_finished)


def straight_drive_until_white_right(speed, stop_when_finished=True):
    def condition():
        return right_on_black()

    straight_drive(speed, condition, stop_when_finished)


def straight_drive_until_black(speed, stop_when_finished=True):
    def condition():
        return left_on_white() and right_on_white()

    straight_drive(speed, condition, stop_when_finished)


def straight_drive_until_both_black(speed, stop_when_finished=True):
    def condition():
        return left_on_white() or right_on_white()
    straight_drive(speed, condition, stop_when_finished)


def straight_drive_until_white(speed, stop_when_finished=True):
    def condition():
        return left_on_black() and right_on_black()

    straight_drive(speed, condition, stop_when_finished)


def straight_drive_until_both_white(speed, stop_when_finished=True):
    def condition():
        return left_on_black() or right_on_black()

    straight_drive(speed, condition, stop_when_finished)


def line_follow_time_lego1(top_hat, duration, side="left", direction=1):
    duration = duration // 1000

    start_time = time.time()
    if side == "left":
        while time.time() - start_time < duration:
            if analog(top_hat) > 3100:
                drive(0, *([direction * 90, direction * 20][::direction]))
            elif analog(top_hat) < 2600:
                drive(0, *([direction * 20, direction * 90][::direction]))
            else:
                drive(0, direction * 85, direction * 85)
    else:
        while time.time() - start_time < duration:
            if analog(top_hat) > 3100:
                drive(0, *([direction * 20, direction * 90][::direction]))
            elif analog(top_hat) < 2600:
                drive(0, *([direction * 90, direction * 20][::direction]))
            else:
                drive(0, direction * 85, direction * 85)


def slay_line_follow(duration):
    duration = duration // 1000
    start_time = time.time()
    while time.time() - start_time < duration:
        if analog(LEFT_TOP_HAT) <= 840:
            drive(100, 70, 0)
        elif 1125 >= analog(LEFT_TOP_HAT) > 840:
            drive(100, 92, 0)
        elif 1410 >= analog(LEFT_TOP_HAT) > 1125:
            drive(100, 95, 0)
        elif 1410 > analog(LEFT_TOP_HAT) >= 1980:
            drive(100, 100, 0)
        elif 1980 < analog(LEFT_TOP_HAT) <= 2265:
            drive(97, 100, 0)
        elif 2265 < analog(LEFT_TOP_HAT) <= 2550:
            drive(95, 100, 0)
        else:
            drive(70, 100, 0)


def line_follow_ticks(ticks, stop=True):
    clear_motor_position_counter(RIGHT_MOTOR)
    clear_motor_position_counter(LEFT_MOTOR)
    while (get_motor_position_counter(RIGHT_MOTOR) + get_motor_position_counter(LEFT_MOTOR)) / 2 < ticks:
        if analog(LEFT_TOP_HAT) < TOP_HAT_THRESHOLD:  # on white
            drive(100, 80, 10)
        else:  # on black
            drive(80, 100, 10)
    if stop:
        stop_motors()


def line_follow_to_black(top_hat, stop=True):
    while analog(top_hat) < TOP_HAT_THRESHOLD:
        line_follow(10)
    if stop:
        stop_motors()


def get_motor_positions():
    return get_motor_position_counter(LEFT_MOTOR), get_motor_position_counter(RIGHT_MOTOR)


def basic_drive(left_speed, right_speed):
    motor_power(LEFT_MOTOR, left_speed)
    motor_power(RIGHT_MOTOR, right_speed)


def square_up_top_hats(left_speed=20, right_speed=20, iterations=1):
    drive_until_both_white(-30, -30)
    for _ in range(iterations):
        ls = left_speed
        rs = right_speed
        ls2 = -left_speed
        rs2 = -right_speed
        basic_drive(ls, rs)
        while ls != 0 or rs != 0:
            if left_on_black():
                ls = 0
                rs2 = 0 if ls2 else rs2
            if right_on_black():
                rs = 0
                ls2 = 0 if rs2 else ls2
            basic_drive(ls, rs)
        while ls2 != 0 or rs2 != 0:
            if left_on_white():
                ls2 = 0
            if right_on_white():
                rs2 = 0
            basic_drive(ls2, rs2)
        left_speed //= 2
        right_speed //= 2
    stop_motors(100)


def stop_motors(stop_time=100):
    freeze(LEFT_MOTOR)
    freeze(RIGHT_MOTOR)
    msleep(stop_time)
