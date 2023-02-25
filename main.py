#!/usr/local/bin/python3.10 -u

from kipr import motor_power, msleep, enable_servos, set_servo_position, analog, push_button, freeze, \
    clear_motor_position_counter, get_motor_position_counter, get_servo_position

from common import ROBOT

import time

lm = 3
rm = 0
lt = 0
claw = 0
claw_open = 50
claw_close = 675
ws_plow_up = 635
ws_plow_down = 1730


def wait_for_button():
    print("waiting for button")
    freeze(lm)
    freeze(rm)
    msleep(1000)
    while not push_button():
        msleep(100)


def drive(duration, left_speed=100, right_speed=100):
    motor_power(rm, right_speed)
    motor_power(lm, left_speed)
    msleep(duration)


def turn(duration, left=0, right=-100):
    motor_power(lm, left)
    motor_power(rm, right)
    msleep(duration)


def line_follow_right(duration, direction=1):
    duration = duration // 1000

    start_time = time.time()

    while time.time() - start_time < duration:
        if analog(lt) > 3100:
            drive(0, *([direction * 90, direction * 20][::direction]))
        elif analog(lt) < 2600:
            drive(0, *([direction * 40, direction * 90][::direction]))
        else:
            drive(0, direction * 85, direction * 85)


def line_follow_left(duration, direction=1):
    duration = duration // 1000

    start_time = time.time()

    while time.time() - start_time < duration:
        if analog(lt) > 3100:
            # if direction is -1, flips polarity and direction of motor (WORK IN PROGRESS, default should work fine)
            # enables the line following to work backwards
            drive(0, *([direction * 40, direction * 90][::direction]))
        elif analog(lt) < 2600:
            # same thing as before
            drive(0, *([direction * 90, direction * 40][::direction]))
        else:
            drive(0, direction * 85, direction * 85)


def line_follow_left_function(duration):
    min_expected = 2200
    max_expected = 3900

    duration = duration // 1000

    start_time = time.time()

    while time.time() - start_time < duration:
        current_value = analog(lt)

        right_motor = (current_value - min_expected) // ((max_expected - min_expected)/100)
        right_motor = min(80, right_motor)
        left_motor = min(80, 80 - right_motor)
        drive(0, left_motor, right_motor)


def go_to_botgal():
    enable_servos()
    set_servo_position(claw, claw_open)
    # moves straight past first black line
    drive(2000, 95, 95)
    # starts line following
    # if it's on black, go right, if on white go left
    line_follow_right(2285)
    freeze(lm)
    freeze(rm)
    drive(985, 80, 80)
    freeze(lm)
    freeze(rm)
    msleep(1000)
    # set_servo_position(claw, claw_close)
    freeze(lm)
    freeze(rm)
    msleep(500)


def to_analysis_lab():
    drive(850, -75, -75)
    turn(2885)
    drive(2200, 75, 75)


def go_to_ws():
    turn(950, -85, 85)
    drive(3085, 100, 95)
    line_follow_left(3500)
    freeze(lm)
    freeze(rm)
    msleep(1000)
    while analog(lt) < 3400:
        turn(5, -85, 85)
    wait_for_button()
    drive(750, -100, -100)


def ws_to_ddos():
    drive(500, -85, -85)
    turn(1200, -85, 85)
    line_follow_right(2785)
    freeze(lm)
    freeze(rm)
    drive(1500)
    line_follow_left_function(4500)


if __name__ == '__main__':
    print("start")
    # go_to_botgal()
    # to_analysis_lab()
    # freeze(lm)
    # freeze(rm)
    # msleep(1000)
    # wait_for_button()
    go_to_ws()
    wait_for_button()
    # TODO:
    # Fix turn once at wireshark
    # Lower ws_plow
    # Line follow right to DDOS
    ws_to_ddos()
    wait_for_button()
    print("end")
