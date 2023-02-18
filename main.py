#!/usr/local/bin/python3.10 -u
# Code for Lego 306
# check instructions in to_analysis_lab 2/16/2023
import time

from kipr import *

lm = 3
rm = 0
lt = 0
claw = 0
claw_open = 50
claw_close = 675


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


def line_follow_right(duration):
    duration = duration // 1000

    start_time = time.time()

    while time.time() - start_time < duration:
        if analog(lt) > 3100:
            drive(0, 90, 20)
        elif analog(lt) < 2600:
            drive(0, 40, 90)
        else:
            drive(0, 85, 85)


def line_follow_left_function(duration):
    min_expected = 2200
    max_expected = 3900

    duration = duration // 1000

    start_time = time.time()

    while time.time() - start_time < duration:
        current_value = analog(lt)

        right_motor = (current_value - min_expected) // 17
        right_motor = min(80, right_motor)
        left_motor = min(80, 80 - right_motor)
        drive(0, left_motor, right_motor)


def go_to_botgal():
    enable_servo(claw)
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
    turn(700, -85, 85)
    wait_for_button()
    drive(2500)
    line_follow_left_function(4000)
    freeze(lm)
    freeze(rm)
    msleep(1000)
    wait_for_button()


def ws_to_ddos():
    drive(500, -85, -85)
    turn(1500, -85, 85)
    line_follow_right(2785)
    freeze(lm)
    freeze(rm)
    drive(1500)
    line_follow_right(4500)


if __name__ == '__main__':
    print("start")
    go_to_botgal()
    to_analysis_lab()
    freeze(lm)
    freeze(rm)
    msleep(1000)
    go_to_ws()
    ws_to_ddos()
    print("end")
