#!/usr/local/bin/python3.10 -u


import time
from kipr import motor_power, msleep, enable_servos, set_servo_position, analog, push_button, freeze, \
    clear_motor_position_counter, get_motor_position_counter, get_servo_position, disable_servos, disable_servo, \
    enable_servo
from common import ROBOT
from constants.servos import *


def drive(left_speed, right_speed, duration):
    motor_power(LEFT_MOTOR, left_speed)
    motor_power(RIGHT_MOTOR, right_speed)
    msleep(duration)


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


def wait_for_button():
    stop_motors()
    print("push the button")
    while not push_button():
        pass
    msleep(1000)


def move_servo(new_position, step_time=10):
    servo = new_position.port
    temp = get_servo_position(servo)
    if servo == BackClaw.port:
        enable_servo(BackClaw.port)

    if temp < new_position:
        while temp < new_position:
            set_servo_position(servo, temp)
            temp += 5
            msleep(step_time)
    else:
        while temp > new_position:
            set_servo_position(servo, temp)
            temp -= 5
            msleep(step_time)

    if servo == BackClaw.port:
        disable_servo(BackClaw.port)


def get_botgal():
    drive(70, 100, 1050)  # move tophat out of start box while lining up for line follow
    drive(100, 80, 1050)
    line_follow_right(1600)  # go to botgal
    drive(93, 100, 500)  # square up with pvc
    stop_motors()
    wait_for_button()
    move_servo(Claw.CLOSED, 2)
    wait_for_button()
    move_servo(Arm.UP)
    wait_for_button()


def deliver_botgal():
    drive(-95, -100, 800)
    wait_for_button()
    drive(0, 100, 1450)
    wait_for_button()
    drive(95, 100, 900)
    drive(0, 100, 1450)
    wait_for_button()
    drive(100, 100, 3000)


def init():
    enable_servos()
    power_on_self_test()
    move_servo(Claw.OPEN, 0)
    move_servo(Arm.STRAIGHT)
    move_servo(BackClaw.UP)
    wait_for_button()


def shut_down():
    disable_servos()
    stop_motors()


def power_on_self_test():
    while analog(TOP_HAT) < 1800:
        drive(95, 100, 10)
    stop_motors()
    drive(93, 0, 1450)
    stop_motors()
    move_servo(Claw.OPEN, 1)
    move_servo(Claw.CLOSED, 1)
    move_servo(Arm.STRAIGHT)
    move_servo(Arm.UP)
    move_servo(Arm.DOWN)
    move_servo(Arm.UP)
    move_servo(BackClaw.DOWN)
    move_servo(BackClaw.UP)
    stop_motors()


def go_to_ws():
    drive(-85, 85, 950)
    line_follow_left(2000)
    wait_for_button()
    drive(1000, 100, 95)
    wait_for_button()
    line_follow_left(3500)
    wait_for_button()
    freeze(LEFT_MOTOR)
    freeze(RIGHT_MOTOR)
    msleep(1000)
    while analog(TOP_HAT) < 3400:
        drive(-85, 85, 5)
    while analog(TOP_HAT) > 2050:
        drive(-85, 85, 5)
    freeze(LEFT_MOTOR)
    freeze(RIGHT_MOTOR)
    wait_for_button()
    drive(750, -100, -100)


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


def ws_to_ddos():
    drive(500, -85, -85)
    drive(-85, 85, 1200)
    line_follow_right(2785)
    freeze(LEFT_MOTOR)
    freeze(RIGHT_MOTOR)
    drive(0, -100, 1500)
    line_follow_right_lego1(4500)


if __name__ == '__main__':
    if ROBOT.is_red:
        init()
        get_botgal()
        # TODO: verify that get_botgal() works with the blue robot, finish deliver_botgal()
        deliver_botgal()
        shut_down()
    elif ROBOT.is_yellow:
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
