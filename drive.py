import time

from constants.ports import LEFT_MOTOR, RIGHT_MOTOR, LEFT_TOP_HAT, RIGHT_TOP_HAT, PUSH_SENSOR
from constants.sensors import TOP_HAT_THRESHOLD, TOP_HAT_THRESHOLD_GREY
from kipr import motor_power, msleep, analog, clear_motor_position_counter, get_motor_position_counter, \
    get_digital_output
from common import ROBOT
from utilities import stop_motors
from common.gyro_movements import gyro_turn, straight_drive


def drive(left_speed, right_speed, duration):
    motor_power(LEFT_MOTOR, left_speed)
    motor_power(RIGHT_MOTOR, right_speed)
    msleep(duration)


def drive_straight(duration, direction=1):
    """
    following right side of black line
    :param duration: time in ms
    :param direction: 1 for forward or -1 for reverse, defaults to forward
    """
    if ROBOT.is_yellow:
        drive(int(direction * 100), int(direction * 96), duration)
    if ROBOT.is_blue:
        drive(int(direction * 97), int(direction * 100), duration)
    if ROBOT.is_red:
        drive(int(direction * 96), int(direction * 100), duration)


def drive_straight_until_white(direction=1):
    drive_straight(10, direction)
    while analog(0) > TOP_HAT_THRESHOLD:
        pass


def drive_straight_until_black(direction=1):
    drive_straight(10, direction)
    while analog(0) < TOP_HAT_THRESHOLD:
        pass


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
            else:
                print("Robot unidentified in line-follow")


def line_follow_left(duration):
    """
    following left side of black line
    :param duration: time in ms
    """

    x = 0
    while x < duration:
        if analog(LEFT_TOP_HAT) < TOP_HAT_THRESHOLD:  # on white
            x += 10
            drive(100, 85, 10)
        else:  # on black
            x += 10
            drive(80, 100, 10)


def line_follow_to_ddos(duration):  # less aggressive
    """
    following left side of black line
    :param duration: time in ms
    """

    x = 0
    while x < duration:
        if analog(LEFT_TOP_HAT) < TOP_HAT_THRESHOLD:  # on white
            x += 10
            drive(100, 90, 10)
        else:  # on black
            x += 10
            drive(85, 100, 10)


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


def dramatic_line_follow(duration):
    """
    following left side of black line
    :param duration: time in ms
    :redrive:
    """

    x = 0
    while x < duration:
        if analog(LEFT_TOP_HAT) < TOP_HAT_THRESHOLD:  # on white
            x += 10
            drive(100, 65, 10)
        else:  # on black
            x += 10
            drive(60, 100, 10)


def drive_until_black(left_motor, right_motor, stop=True):
    drive(left_motor, right_motor, 0)
    while analog(LEFT_TOP_HAT) < TOP_HAT_THRESHOLD:
        pass
    if stop:
        stop_motors()


def drive_until_white(left_motor, right_motor, stop=True):
    drive(left_motor, right_motor, 0)
    while analog(LEFT_TOP_HAT) > TOP_HAT_THRESHOLD:
        pass
    if stop:
        stop_motors()


def line_follow_right_lego1(duration, direction=1):
    duration = duration // 1000

    start_time = time.time()

    while time.time() - start_time < duration:
        if analog(LEFT_TOP_HAT) > 3100:
            drive(0, *([direction * 90, direction * 20][::direction]))
        elif analog(LEFT_TOP_HAT) < 2600:
            drive(0, *([direction * 40, direction * 90][::direction]))
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


def straight_timed_slow(duration, stop=True):
    offset = ROBOT.load("slow") or 0
    # print("Driving at speed 45 with offset", offset)
    motor_power(LEFT_MOTOR, 45)
    motor_power(RIGHT_MOTOR, 45 + offset)
    msleep(duration)
    if stop:
        stop_motors()


def straight_timed_fast(duration, stop=True):
    offset = ROBOT.load("fast") or 0
    # print("Driving at speed 85 with offset", offset)
    motor_power(LEFT_MOTOR, 85)
    motor_power(RIGHT_MOTOR, 85 + offset)
    msleep(duration)
    if stop:
        stop_motors()


def straight_distance_fast(distance):
    offset = ROBOT.load("fast") or 0
    ticks = distance * ROBOT.load("inches_to_ticks")
    if ticks > 0:
        motor_power(LEFT_MOTOR, 85)
        motor_power(RIGHT_MOTOR, 85 + offset)
        clear_motor_position_counter(LEFT_MOTOR)
        while get_motor_position_counter(LEFT_MOTOR) < ticks:
            # print(get_motor_position_counter(LEFT_MOTOR), ticks, ROBOT.load("inches_to_ticks"))
            pass
    if ticks < 0:
        motor_power(LEFT_MOTOR, -85)
        motor_power(RIGHT_MOTOR, -85 - offset)
        clear_motor_position_counter(LEFT_MOTOR)
        while get_motor_position_counter(LEFT_MOTOR) > ticks:
            # print(get_motor_position_counter(LEFT_MOTOR), ticks, ROBOT.load("inches_to_ticks"))
            pass
    stop_motors()


def straight_distance_slow(distance):
    offset = ROBOT.load("slow") or 0
    ticks = distance * ROBOT.load("inches_to_ticks")
    if ticks > 0:
        motor_power(LEFT_MOTOR, 45)
        motor_power(RIGHT_MOTOR, 45 + offset)
        clear_motor_position_counter(LEFT_MOTOR)
        while get_motor_position_counter(LEFT_MOTOR) < ticks:
            # print(get_motor_position_counter(LEFT_MOTOR), ticks, ROBOT.load("inches_to_ticks"))
            pass
    if ticks < 0:
        motor_power(LEFT_MOTOR, -45)
        motor_power(RIGHT_MOTOR, -45 - offset)
        clear_motor_position_counter(LEFT_MOTOR)
        while get_motor_position_counter(LEFT_MOTOR) > ticks:
            # print(get_motor_position_counter(LEFT_MOTOR), ticks, ROBOT.load("inches_to_ticks"))
            pass
    stop_motors()


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


def gyro_drive(left_speed, right_speed):
    drive(int(round(left_speed, 0)), int(round(right_speed, 0)), 0)


def line_follow_to_line(stop=True):
    while analog(RIGHT_TOP_HAT) < TOP_HAT_THRESHOLD:
        dramatic_line_follow(10)
    if stop:
        stop_motors()


def calibrate_straight_drive_distance():
    start_position = get_motor_position_counter(LEFT_MOTOR) + get_motor_position_counter(RIGHT_MOTOR)

    def condition():
        return get_digital_output(PUSH_SENSOR) == 0
    straight_drive(100, condition)
    print((get_motor_position_counter(LEFT_MOTOR)+get_motor_position_counter(RIGHT_MOTOR)-start_position)
          + " ticks driven")


def straight_drive_distance(speed, inches, stop_when_finished):
    # Number printed divided by the distance driven when running calibrate_straight_drive_distance
    straight_drive_distance_proportion = ROBOT.choose(
        red=1.0,
        blue=1.0,
        yellow=1.0,
        green=1.0
    )
    start_position = get_motor_position_counter(LEFT_MOTOR) + get_motor_position_counter(RIGHT_MOTOR)

    def condition():
        return get_motor_position_counter(LEFT_MOTOR) + get_motor_position_counter(RIGHT_MOTOR) - start_position < \
            inches * straight_drive_distance_proportion
    straight_drive(speed, condition, stop_when_finished)
