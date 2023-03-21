import time
from kipr import msleep, enable_servos, set_servo_position, analog, freeze, \
    get_servo_position, disable_servos, disable_servo, \
    enable_servo
from drive import drive, stop_motors, line_follow, line_follow_left, drive_straight, line_follow_right_lego1,\
    dramatic_line_follow, line_follow_right
from servo import move_servo_lego
from utilities import wait_for_button
from constants.ports import TOP_HAT, LEFT_MOTOR, RIGHT_MOTOR
from constants.servos import BackClaw, Claw, Arm


def init():
    enable_servos()
    power_on_self_test()
    move_servo_lego(BackClaw.UP)
    move_servo_lego(Claw.CLOSED, 0)
    move_servo_lego(Arm.UP)
    wait_for_button()
    move_servo_lego(Claw.OPEN, 0)
    move_servo_lego(Arm.STRAIGHT)


def power_on_self_test():
    while analog(TOP_HAT) < 1800:
        drive_straight(10)
    stop_motors()
    msleep(800)
    drive_straight(500)
    drive(93, 0, 1450)
    stop_motors()
    move_servo_lego(Claw.OPEN, 1)
    move_servo_lego(Arm.STRAIGHT)
    move_servo_lego(Arm.UP)
    move_servo_lego(Arm.DOWN)
    move_servo_lego(Arm.UP)
    move_servo_lego(Claw.GRAB, 1)
    move_servo_lego(BackClaw.DOWN)
    move_servo_lego(BackClaw.UP)
    stop_motors()


def shut_down():
    disable_servos()
    stop_motors()
    print("end")


def get_botgal():
    line_follow(3200)  # go to botgal
    stop_motors()
    drive_straight(200, -1)
    stop_motors()
    move_servo_lego(Arm.GRAB)
    move_servo_lego(Claw.GRAB, 2)
    move_servo_lego(Arm.UP, 20)


def deliver_botgal():
    drive_straight(600, -1)
    drive(0, 100, 2000)
    drive(-85, 85, 0)
    while analog(TOP_HAT) < 1800:
        pass
    line_follow_right(1200)
    stop_motors()
    move_servo_lego(Arm.DOWN)
    drive(100, 20, 400)
    stop_motors()
    move_servo_lego(Claw.OPEN)
    move_servo_lego(Arm.STRAIGHT)


# def go_to_ws():
#     drive(-85, 85, 950)
#     line_follow_left(2000)
#     wait_for_button()
#     drive(1000, 100, 95)
#     wait_for_button()
#     line_follow_left(3500)
#     wait_for_button()
#     freeze(LEFT_MOTOR)
#     freeze(RIGHT_MOTOR)
#     msleep(1000)
#     while analog(TOP_HAT) < 3400:
#         drive(-85, 85, 5)
#     while analog(TOP_HAT) > 2050:
#         drive(-85, 85, 5)
#     freeze(LEFT_MOTOR)
#     freeze(RIGHT_MOTOR)
#     wait_for_button()
#     drive(750, -100, -100)


def wire_shark():
    drive(-30, 100, 800)
    # stop_motors()
    drive(0, 100, 0)
    while analog(TOP_HAT) < 1800:  # line follow to turn until black
        pass
    dramatic_line_follow(3255)
    # stop_motors()
    drive(100, -100, 1000)
    drive(80, -80, 0)
    while analog(TOP_HAT) < 1800:  # line follow to turn until black
        pass
    # stop_motors()
    drive(-80, 80, 0)
    while analog(TOP_HAT) > 1600:  # line follow to turn until white
        pass
    drive(-65, 65, 75)


def ws_to_ddos():
    drive(-85, -85, 100)
    move_servo_lego(BackClaw.DOWN)
    drive(85, 85, 1500)
    # stop_motors()
    drive(-85, -85, 50)
    move_servo_lego(BackClaw.SUPERDOWN)
    line_follow_left(6800)
    drive(-85, 85, 1450)
    drive(-80, 80, 0)
    while analog(TOP_HAT) < 1800:  # line follow to turn until black
        pass
    drive(-40, 40, 0)
    while analog(TOP_HAT) > 1600:  # line follow to turn until white
        pass
    drive(-65, 65, 150)
    # stop_motors()
    drive(-80, -80, 1300)
    stop_motors()
    msleep(10)

    # drive(100, 90, 0)
    # while analog(TOP_HAT) < 1800:  # arc until white to line up for right line follow
    #     pass
    # wait_for_button()
    # drive(-80, 80, 150)
    # wait_for_button()
    # line_follow_right(2000)
    # wait_for_button()
    # drive(0, -100, 1500)
    # line_follow_right_lego1(4500)


def ddos_to_analysis():
    # drive(85, 85, 250)
    # wait_for_button()
    # drive(0, 85, 400)
    # wait_for_button()
    # drive(85, 85, 250)
    wait_for_button()
    dramatic_line_follow(1700)
    stop_motors()
    drive(0, 85, 1500)
    drive(-85, -85, 900)
    stop_motors()
    move_servo_lego(BackClaw.UP)


def knock_over_rings():
    drive_straight(650)
    drive(-80, 80, 1800)
    stop_motors()
    move_servo_lego(Arm.DOWN)
    drive(100, -100, 600)
    stop_motors()
    move_servo_lego(Claw.CLOSED)
    drive(-100, 100, 500)
    stop_motors()


def get_noodle_one():
    wait_for_button()
    drive(-60, 60, 0)
    while analog(TOP_HAT) < 1800:
        pass
    stop_motors()
    wait_for_button()
    drive(-80, 80, 1400)
    stop_motors()
