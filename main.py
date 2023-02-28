#!/usr/local/bin/python3.10 -u

from kipr import motor_power, msleep, enable_servos, set_servo_position, analog, push_button, freeze, clear_motor_position_counter, get_motor_position_counter, get_servo_position, disable_servos, disable_servo, enable_servo
from common import ROBOT
from constants.ports import *
from constants.servos import *


def drive(left_speed, right_speed, time):
    motor_power(LEFT_MOTOR, left_speed)
    motor_power(RIGHT_MOTOR, right_speed)
    msleep(time)


def line_follow(time):
    x = 0
    while x < time:
        if analog(TOP_HAT) < 1800:  # on white
            x += 10
            drive(80, 100, 10)
        else:                       # on black
            x += 10
            drive(100, 85, 10)


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
    # drive(70, 100, 1050)                 # move tophat out of start box while lining up for line follow
    # drive(100, 80, 1050)
    line_follow(3000)                      # go to botgal
    stop_motors()
    drive(-100, 0, 300)
    stop_motors()
    wait_for_button()
    drive(-95, -100, 400)
    stop_motors()
    wait_for_button()
    # drive(93, 100, 500)                  # square up with pvc
    # stop_motors()
    # wait_for_button()
    move_servo(Claw.CLOSED, 2)
    wait_for_button()
    move_servo(Arm.UP)



def deliver_botgal():
    drive(-95, -100, 800)
    # wait_for_button()
    # drive(0, 100, 1450)
    # wait_for_button()
    # drive(95, 100, 900)
    # drive(0, 100, 1450)
    # wait_for_button()
    # drive(100, 100, 3000)


def init():
    enable_servos()
    disable_servo(BackClaw.port)
    # POST()
    move_servo(Claw.OPEN, 0)
    move_servo(Arm.STRAIGHT)
    move_servo(BackClaw.UP)
    wait_for_button()


def shut_down():
    disable_servos()
    stop_motors()


def POST():
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


if __name__ == '__main__':
    if ROBOT.is_red:
        print("yes i am red")
    init()
    get_botgal()
    wait_for_button()
    # TODO: verify that get_botgal() works with the blue robot, finish deliver_botgal()
    deliver_botgal()
    shut_down()
