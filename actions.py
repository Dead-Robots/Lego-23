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
from common import ROBOT


def init():
    enable_servos()
    power_on_self_test()
    move_servo_lego(BackClaw.UP)
    move_servo_lego(Claw.CLOSED, 0)
    move_servo_lego(Arm.UP)
    wait_for_button("push button to start")
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
    move_servo_lego(Claw.OPEN, 0)
    move_servo_lego(Arm.STRAIGHT, 4)
    move_servo_lego(Arm.UP, 5)
    move_servo_lego(Arm.DOWN, 4)
    move_servo_lego(Arm.STRAIGHT, 4)
    move_servo_lego(Arm.UP, 5)
    move_servo_lego(Claw.GRAB, 0)
    move_servo_lego(BackClaw.DOWN, 5)
    move_servo_lego(BackClaw.UP, 5)
    stop_motors()


def shut_down():
    disable_servos()
    stop_motors()
    print("end")


def get_botgal():
    line_follow(2750)  # go to botgal
    if ROBOT.is_red:
        drive_straight(420)
    elif ROBOT.is_blue:
        drive_straight(420)
    elif ROBOT.is_yellow:
        drive_straight(420)
    elif ROBOT.is_green:
        drive_straight(420)
    else:
        print("ROBOT UNIDENTIFIED")
    stop_motors()
    if ROBOT.is_red:
        drive_straight(200, -1)
    elif ROBOT.is_blue:
        drive_straight(200, -1)
    elif ROBOT.is_yellow:
        drive_straight(200, -1)
    elif ROBOT.is_green:
        drive_straight(200, -1)
    else:
        print("ROBOT UNIDENTIFIED")
    stop_motors()
    move_servo_lego(Arm.GRAB, 4)
    move_servo_lego(Claw.GRAB, 4)
    move_servo_lego(Arm.UP, 20)


def deliver_botgal():

    if ROBOT.is_red:
        drive_straight(600, -1)
    elif ROBOT.is_blue:
        drive_straight(600, -1)
    elif ROBOT.is_yellow:
        drive_straight(600, -1)
    elif ROBOT.is_green:
        drive_straight(600, -1)
    else:
        print("ROBOT UNIDENTIFIED")

    if ROBOT.is_red:
        drive(0, 100, 2000)
    elif ROBOT.is_blue:
        drive(0, 100, 2000)
    elif ROBOT.is_yellow:
        drive(0, 100, 2000)
    elif ROBOT.is_green:
        drive(0, 100, 2000)
    else:
        print("ROBOT UNIDENTIFIED")

    drive(-85, 85, 0)
    while analog(TOP_HAT) < 1800:
        pass

    line_follow_right(
        ROBOT.choose(
            red=1000,
            blue=1000,
            yellow=1000,
            green=1000
        )
    )

    stop_motors()

    move_servo_lego(Arm.DOWN, 4)
    if ROBOT.is_red:
        drive_straight(470)
    elif ROBOT.is_blue:
        drive_straight(470)
    elif ROBOT.is_yellow:
        drive_straight(470)
    elif ROBOT.is_green:
        drive_straight(470)
    else:
        print("ROBOT UNIDENTIFIED")

    drive(100, 10, ROBOT.choose(
            red=525,
            blue=525,
            yellow=525,
            green=525
        )
    )

    stop_motors()
    move_servo_lego(Claw.OPEN, 2)

    if ROBOT.is_red:
        drive_straight(350, -1)
    elif ROBOT.is_blue:
        drive_straight(350, -1)
    elif ROBOT.is_yellow:
        drive_straight(350, -1)
    elif ROBOT.is_green:
        drive_straight(350, -1)
    else:
        print("ROBOT UNIDENTIFIED")

    stop_motors()
    move_servo_lego(Arm.STRAIGHT, 4)
    move_servo_lego(Arm.UP, 5)
    move_servo_lego(Claw.CLOSED, 0)


def wire_shark():

    drive(-30, 100, ROBOT.choose(
            red=800,
            blue=800,
            yellow=800,
            green=800
        )
    )

    # stop_motors()
    drive(0, 100, 0)
    while analog(TOP_HAT) < 1800:  # line follow to turn until black
        pass

    dramatic_line_follow(
        ROBOT.choose(
            red=3650,
            blue=3650,
            yellow=3650,
            green=3650
        )
    )
    # stop_motors()
    drive(100, -100, ROBOT.choose(
            red=1000,
            blue=1000,
            yellow=1000,
            green=1000
        )
    )
    drive(80, -80, 0)
    while analog(TOP_HAT) < 1800:  # line follow to turn until black
        pass
    # stop_motors()
    drive(-80, 80, 0)
    while analog(TOP_HAT) > 1600:  # line follow to turn until white
        pass
    drive(-65, 65, ROBOT.choose(
            red=40,
            blue=40,
            yellow=40,
            green=40
        )
    )
    if ROBOT.is_red:
        drive_straight(1250, -1)
    elif ROBOT.is_blue:
        drive_straight(1250, -1)
    elif ROBOT.is_yellow:
        drive_straight(1250, -1)
    elif ROBOT.is_green:
        drive_straight(1250, -1)
    else:
        print("ROBOT UNIDENTIFIED")
    stop_motors()
    move_servo_lego(BackClaw.DOWN, 5)
    move_servo_lego(Claw.OPEN)


def ws_to_ddos():
    if ROBOT.is_red:
        drive_straight(1400)
    elif ROBOT.is_blue:
        drive_straight(1400)
    elif ROBOT.is_yellow:
        drive_straight(1400)
    elif ROBOT.is_green:
        drive_straight(1400)
    else:
        print("ROBOT UNIDENTIFIED")
    # stop_motors()
    drive(-85, -85, ROBOT.choose(
            red=10,
            blue=10,
            yellow=10,
            green=10
        )
    )
    move_servo_lego(BackClaw.SUPERDOWN, 2)
    line_follow_left(ROBOT.choose(
            red=6000,
            blue=6000,
            yellow=6000,
            green=6000
        )
    )
    drive(-85, 85, ROBOT.choose(
            red=1450,
            blue=1450,
            yellow=1450,
            green=1450
        )
    )
    drive(-80, 80, 0)
    while analog(TOP_HAT) < 1800:  # line follow to turn until black
        pass
    drive(-40, 40, 0)
    while analog(TOP_HAT) > 1600:  # line follow to turn until white
        pass
    stop_motors()
    drive(-65, 65, ROBOT.choose(
            red=100,
            blue=100,
            yellow=100,
            green=100
        )
    )
    # stop_motors()
    if ROBOT.is_red:
        drive_straight(780, -1)
    elif ROBOT.is_blue:
        drive_straight(780, -1)
    elif ROBOT.is_yellow:
        drive_straight(780, -1)
    elif ROBOT.is_green:
        drive_straight(780, -1)
    else:
        print("ROBOT UNIDENTIFIED")
    stop_motors()
    msleep(ROBOT.choose(
            red=5000,
            blue=5000,
            yellow=5000,
            green=5000
        )
    )


def ddos_to_analysis():
    dramatic_line_follow(ROBOT.choose(
            red=1400,
            blue=1400,
            yellow=1400,
            green=1400
        )
    )
    stop_motors()
    drive(0, 85, ROBOT.choose(
            red=1500,
            blue=1500,
            yellow=1500,
            green=1500
        )
    )
    drive(-85, -85, ROBOT.choose(
            red=900,
            blue=900,
            yellow=900,
            green=900
        )
    )
    stop_motors()
    move_servo_lego(BackClaw.UP)


def knock_over_rings():
    if ROBOT.is_red:
        drive_straight(800)
    elif ROBOT.is_blue:
        drive_straight(800)
    elif ROBOT.is_yellow:
        drive_straight(800)
    elif ROBOT.is_green:
        drive_straight(800)
    else:
        print("ROBOT UNIDENTIFIED")
    drive(-80, 80, ROBOT.choose(
            red=1650,
            blue=1650,
            yellow=1650,
            green=1650
        )
    )
    stop_motors()
    move_servo_lego(Claw.CLOSED, 0)
    move_servo_lego(Arm.RING)
    drive(-100, 100, ROBOT.choose(
            red=450,
            blue=450,
            yellow=450,
            green=450
        )
    )
    stop_motors()


def get_noodle_one():
    drive(-60, 60, 0)
    while analog(TOP_HAT) < 1800:
        pass
    stop_motors()
    wait_for_button()
    drive(-80, 80, ROBOT.choose(
            red=1400,
            blue=1400,
            yellow=1400,
            green=1400
        )
    )
    stop_motors()
