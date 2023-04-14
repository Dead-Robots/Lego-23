import time
from kipr import msleep, enable_servos, set_servo_position, analog, disable_servos, enable_servo

from calibrate import choose_to_calibrate
from drive import drive, line_follow, line_follow_left, drive_straight, line_follow_right_lego1,\
    dramatic_line_follow, line_follow_right
from servo import move_servo_lego
from utilities import wait_for_button, stop_motors, debug
from constants.ports import TOP_HAT
from constants.servos import BackClaw, Claw, Arm
from common import ROBOT


def init():
    choose_to_calibrate()
    enable_servos()
    power_on_self_test()
    move_servo_lego(BackClaw.UP)
    move_servo_lego(Claw.CLOSED, 0)
    move_servo_lego(Arm.UP)
    wait_for_button("push button to start")


def power_on_self_test():
    set_servo_position(BackClaw.port, BackClaw.UP)
    while analog(TOP_HAT) < 2300:
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
    move_servo_lego(BackClaw.SUPERDOWN, 5)
    move_servo_lego(BackClaw.DOWN, 5)
    msleep(1000)
    move_servo_lego(BackClaw.UP, 5)
    stop_motors()


def shut_down():
    disable_servos()
    stop_motors()
    print("end")


def get_botgal():
    # moves claw and arm from start position
    move_servo_lego(Claw.OPEN, 0)
    move_servo_lego(Arm.STRAIGHT)
    # goes to botgal
    line_follow(ROBOT.choose(red=2850, blue=2750, yellow=2750))
    drive_straight(ROBOT.choose(red=320, blue=420, yellow=420))
    stop_motors()
    # backs up to prepare for grab
    drive_straight(ROBOT.choose(red=200, blue=100, yellow=200), -1)
    stop_motors()
    # grabs and lifts botgal
    move_servo_lego(Arm.GRAB, 4)
    move_servo_lego(Claw.GRAB, 4)
    move_servo_lego(Arm.UP, 20)


def deliver_botgal():
    # backs up to make space for turn
    drive_straight(ROBOT.choose(red=600, blue=600, yellow=600), -1)
    # turns left past black line
    drive(0, 100, ROBOT.choose(red=2000, blue=2000, yellow=2000))
    # turns left to next black line
    drive(-85, 85, 0)
    while analog(TOP_HAT) < 2300:
        pass
    # line follows to botgal delivery zone
    # while analog(TOP_HAT) < 2300: try to account for difficulty grabbing botgal
    line_follow_right(ROBOT.choose(red=1000, blue=900, yellow=1000))
    stop_motors()
    # lowers arm early to avoid hitting green pool noodles
    move_servo_lego(Arm.DOWN, 4)
    # drives straight to get botgal in line with the delivery zone
    drive_straight(ROBOT.choose(red=470, blue=570, yellow=470))
    # arcs right to move botgal away from black line
    drive(100, 30, ROBOT.choose(red=525, blue=350, yellow=525))
    stop_motors()
    # releases botgal
    move_servo_lego(Claw.OPEN, 2)
    # backs away from botgal to make room for lifting arm
    drive_straight(ROBOT.choose(red=350, blue=350, yellow=350), -1)
    stop_motors()
    # lifts arm and closes claw to help get out of Create's path
    move_servo_lego(Arm.STRAIGHT, 4)
    move_servo_lego(Arm.UP, 5)
    move_servo_lego(Claw.CLOSED, 0)


def get_wire_shark():
    # turns past black line
    drive(-30, 100, ROBOT.choose(red=1000, blue=1000, yellow=800))
    # turns until next black line to prepare for line follow
    drive(0, 100, 0)
    while analog(TOP_HAT) < 2300:
        pass
    # line follows to wireshark
    dramatic_line_follow(ROBOT.choose(red=3300, blue=3200, yellow=3850))
    stop_motors()
    # lowers the backclaw to sweep the poms out of the way
    move_servo_lego(BackClaw.SUPERDOWN, 2)
    # turns right past black line
    drive(100, -100, ROBOT.choose(red=800, blue=800, yellow=1000))
    # turns until next black line
    drive(80, -80, 0)
    while analog(TOP_HAT) < 2300:
        pass
    # turns back until white
    drive(-30, 30, 0)
    while analog(TOP_HAT) > 2300:
        pass
    # turns left slightly to line up correctly with wireshark
    drive(-65, 65, ROBOT.choose(red=40, blue=150, yellow=40))
    # lifts backclaw again to prepare to get wireshark
    stop_motors()
    move_servo_lego(BackClaw.UP, 3)
    # backs up to wireshark
    drive_straight(ROBOT.choose(red=1425, blue=1450, yellow=1250), -1)
    stop_motors()
    drive_straight(ROBOT.choose(red=10, blue=20, yellow=0))
    stop_motors()
    # sets the backclaw to down prior to enabling it to prevent it from jumping upwards
    set_servo_position(BackClaw.port, BackClaw.DOWN)
    enable_servo(BackClaw.port)
    # grabs wireshark
    msleep(300)


def ws_to_ddos():
    # begins moving to ddos with wireshark
    drive_straight(ROBOT.choose(red=400, blue=400, yellow=400))
    # moves backclaw farther down to more securely grab wireshark
    drive_straight(ROBOT.choose(red=100, blue=100, yellow=100), -1)
    move_servo_lego(BackClaw.SUPERDOWN, 2)
    enable_servo(BackClaw.port)
    drive_straight(ROBOT.choose(red=100, blue=100, yellow=100), -1)
    # line follow to ddos
    # line_follow_left(ROBOT.choose(red=0, blue=1000, yellow=0))
    # drive_straight(ROBOT.choose(red=0, blue=200, yellow=0), -1)
    # move_servo_lego(BackClaw.SUPERDOWN, 0)
    # enable_servo(BackClaw.port)
    # drive_straight(ROBOT.choose(red=0, blue=200, yellow=0))
    line_follow_left(ROBOT.choose(red=7000, blue=7100, yellow=7500))
    # turns left past black line
    drive(-85, 85, ROBOT.choose(red=1450, blue=1450, yellow=1450))
    # turns until next black line
    drive(-80, 80, 0)
    while analog(TOP_HAT) < 2300:
        pass
    # turns until the end of the black line
    drive(-40, 40, 0)
    while analog(TOP_HAT) > 2300:
        pass
    # turns left to line up with ddos
    drive(-65, 65, ROBOT.choose(red=50, blue=135, yellow=100))
    stop_motors()
    # backs up to position wireshark under ddos
    drive_straight(ROBOT.choose(red=780, blue=800, yellow=780), -1)
    stop_motors()


def ddos_to_analysis():
    # line follows to line up with delivery zone
    dramatic_line_follow(ROBOT.choose(red=1500, blue=1250, yellow=1800))
    stop_motors()
    # turns left to line up with delivery zone
    drive(0, 85, ROBOT.choose(red=1500, blue=1500, yellow=1500))
    # backs up to put wireshark in delivery zone
    drive_straight(ROBOT.choose(red=850, blue=850, yellow=850), -1)
    stop_motors()
    # releases wireshark
    move_servo_lego(BackClaw.UP)


def knock_over_rings():
    # moves away from rings to space the claw correctly
    drive_straight(ROBOT.choose(red=800, blue=800, yellow=800))
    # turns right to prepare to knock over rings
    drive(-80, 80, ROBOT.choose(red=1650, blue=1450, yellow=1650))
    stop_motors()
    # lowers the arm to prepare to knock over rings
    move_servo_lego(Arm.RING, 4)
    # turns quickly to knock over rings
    drive(-100, 100, ROBOT.choose(red=450, blue=450, yellow=450))
    stop_motors()


def get_noodle_one():
    msleep(13000)
    move_servo_lego(Arm.STRAIGHT, 4)
    drive(-60, 60, 0)
    while analog(TOP_HAT) < 2300:
        pass
    if ROBOT.is_blue:
        drive(-60, 60, 200)
        line_follow_left(700)
        drive(-60, 60, 1360)
        stop_motors()
        move_servo_lego(Arm.NOODLE)
        move_servo_lego(Claw.NOODLE_OPEN, 0)
        drive_straight(625)
        wait_for_button()
        move_servo_lego(Claw.NOODLE_GRAB, 2)
        drive_straight(200, -1)
        move_servo_lego(Claw.NOODLE_OPEN)

    if ROBOT.is_red:
        drive(-60, 60, 0)
        while analog(TOP_HAT) > 2300:
            pass
        line_follow_left(ROBOT.choose(red=700, blue=700, yellow=700))
        drive(-60, 60, ROBOT.choose(red=1450, blue=1500, yellow=1500))
        drive_straight(ROBOT.choose(red=700, blue=750, yellow=750))
        stop_motors()
        move_servo_lego(Claw.NOODLE_OPEN)
        move_servo_lego(Arm.RED_NOODLE_GRAB_1, 6)
        move_servo_lego(Claw.RED_NOODLE_GRAB_1, 2)
        drive_straight(ROBOT.choose(red=400, blue=400, yellow=400), -1)
        stop_motors()
        move_servo_lego(Claw.NOODLE_OPEN, 2)
        move_servo_lego(Arm.RED_NOODLE_GRAB_2, 4)
        drive_straight(ROBOT.choose(red=400, blue=200, yellow=200))
        stop_motors()
        move_servo_lego(Claw.RED_NOODLE_GRAB_2, 2)
        drive_straight(ROBOT.choose(red=1200, blue=800, yellow=800), -1)
        stop_motors()
        move_servo_lego(Arm.STRAIGHT, 4)
        drive_straight(ROBOT.choose(red=900))
        drive(-60, 60, ROBOT.choose(red=1200, blue=1500, yellow=1500))
        drive_straight(500)
        drive(-60, 60, ROBOT.choose(red=1450, blue=1500, yellow=1500))


