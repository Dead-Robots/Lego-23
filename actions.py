import time
from kipr import motor_power, msleep, enable_servos, set_servo_position, analog, push_button, freeze, \
    clear_motor_position_counter, get_motor_position_counter, get_servo_position, disable_servos, disable_servo, \
    enable_servo
from common.drive import drive, stop_motors, line_follow, line_follow_left
from common.servo import move_servo
from common.utilities import wait_for_button
from constants.ports import TOP_HAT, LEFT_MOTOR, RIGHT_MOTOR
from constants.servos import BackClaw, Claw, Arm


def init():
    enable_servos()
    disable_servo(BackClaw.port)
    # power_on_self_test()
    move_servo(Claw.OPEN, 0)
    move_servo(Arm.STRAIGHT)
    move_servo(BackClaw.UP)
    wait_for_button()


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


def shut_down():
    disable_servos()
    stop_motors()


def get_botgal():
    # drive(70, 100, 1050)                 # move tophat out of start box while lining up for line follow
    # drive(100, 80, 1050)
    line_follow(3000)  # go to botgal
    stop_motors()
    drive(-100, 0, 150)
    drive(-95, -100, 150)
    stop_motors()
    move_servo(Arm.GRAB)
    # drive(93, 100, 500)                  # square up with pvc
    # stop_motors()
    # wait_for_button()
    move_servo(Claw.CLOSED, 2)
    move_servo(Arm.UP)


def deliver_botgal():
    drive(-95, -100, 1600)
    drive(-100, 100, 1150)
    drive(95, 100, 900)
    stop_motors()
    move_servo(Arm.DOWN)
    move_servo(Claw.OPEN)
    move_servo(Arm.STRAIGHT)


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
    line_follow(2785)
    freeze(LEFT_MOTOR)
    freeze(RIGHT_MOTOR)
    drive(0, -100, 1500)
    line_follow_right_lego1(4500)
