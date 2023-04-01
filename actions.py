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
    # goes to botgal
    line_follow(2750)
    ROBOT.run(drive_straight, red=420)
    ROBOT.run(drive_straight, blue=420)
    ROBOT.run(drive_straight, yellow=420)
    stop_motors()
    # backs up to prepare for grab
    ROBOT.run(drive_straight, red=(200, -1))
    ROBOT.run(drive_straight, blue=(200, -1))
    ROBOT.run(drive_straight, yellow=(200, -1))
    stop_motors()
    # grabs and lifts botgal
    move_servo_lego(Arm.GRAB, 4)
    move_servo_lego(Claw.GRAB, 4)
    move_servo_lego(Arm.UP, 20)


def deliver_botgal():
    # backs up to make space for turn
    ROBOT.run(drive_straight, red=(600, -1))
    ROBOT.run(drive_straight, blue=(600, -1))
    ROBOT.run(drive_straight, yellow=(600, -1))
    # turns left past black line
    ROBOT.run(drive, red=(0, 100, 2000))
    ROBOT.run(drive, blue=(0, 100, 2000))
    ROBOT.run(drive, yellow=(0, 100, 2000))
    # turns left to next black line
    drive(-85, 85, 0)
    while analog(TOP_HAT) < 1800:
        pass
    # line follows to botgal delivery zone
    ROBOT.run(line_follow_right, red=1000)
    ROBOT.run(line_follow_right, blue=1000)
    ROBOT.run(line_follow_right, yellow=1000)
    stop_motors()
    # lowers arm early to avoid hitting green pool noodles
    move_servo_lego(Arm.DOWN, 4)
    # drives straight to get botgal in line with the delivery zone
    ROBOT.run(drive_straight, red=470)
    ROBOT.run(drive_straight, blue=470)
    ROBOT.run(drive_straight, yellow=470)
    # arcs right to move botgal away from black line
    ROBOT.run(drive, red=(100, 10, 525))
    ROBOT.run(drive, blue=(100, 10, 525))
    ROBOT.run(drive, yellow=(100, 10, 525))
    stop_motors()
    # releases botgal
    move_servo_lego(Claw.OPEN, 2)
    # backs away from botgal to make room for lifting arm
    ROBOT.run(drive_straight, red=(350, -1))
    ROBOT.run(drive_straight, blue=(350, -1))
    ROBOT.run(drive_straight, yellow=(350, -1))
    stop_motors()
    # lifts arm and closes claw to help get out of Create's path
    move_servo_lego(Arm.STRAIGHT, 4)
    move_servo_lego(Arm.UP, 5)
    move_servo_lego(Claw.CLOSED, 0)


def wire_shark():
    # turns past black line
    ROBOT.run(drive, red=(-30, 100, 800))
    ROBOT.run(drive, blue=(-30, 100, 800))
    ROBOT.run(drive, yellow=(-30, 100, 800))
    # turns until next black line to prepare for line follow
    drive(0, 100, 0)
    while analog(TOP_HAT) < 1800:
        pass
    # line follows to wireshark
    ROBOT.run(dramatic_line_follow, red=3650)
    ROBOT.run(dramatic_line_follow, blue=3650)
    ROBOT.run(dramatic_line_follow, yellow=3650)
    # turns right past black line
    ROBOT.run(drive, red=(100, -100, 1000))
    ROBOT.run(drive, blue=(100, -100, 1000))
    ROBOT.run(drive, yellow=(100, -100, 1000))
    # turns until next black line
    drive(80, -80, 0)
    while analog(TOP_HAT) < 1800:
        pass
    # turns back until white
    drive(-40, 40, 0)
    while analog(TOP_HAT) > 1600:
        pass
    # turns left slightly to line up correctly with wireshark
    ROBOT.run(drive, red=(-65, 65, 40))
    ROBOT.run(drive, blue=(-65, 65, 40))
    ROBOT.run(drive, yellow=(-65, 65, 40))
    # backs up to wireshark
    ROBOT.run(drive_straight, red=(1250, -1))
    ROBOT.run(drive_straight, blue=(1250, -1))
    ROBOT.run(drive_straight, yellow=(1250, -1))
    stop_motors()
    # grabs wireshark
    move_servo_lego(BackClaw.DOWN, 5)
    move_servo_lego(Claw.OPEN)


def ws_to_ddos():
    # begins moving to ddos with wireshark
    ROBOT.run(drive_straight, red=1390)
    ROBOT.run(drive_straight, blue=1390)
    ROBOT.run(drive_straight, yellow=1390)
    # moves backclaw farther down to more securely grab wireshark
    move_servo_lego(BackClaw.SUPERDOWN, 2)
    # line follow to ddos
    ROBOT.run(line_follow_left, red=6400)
    ROBOT.run(line_follow_left, blue=6400)
    ROBOT.run(line_follow_left, yellow=6400)
    # turns left past black line
    ROBOT.run(drive, red=(-85, 85, 1450))
    ROBOT.run(drive, blue=(-85, 85, 1450))
    ROBOT.run(drive, yellow=(-85, 85, 1450))
    # turns until next black line
    drive(-80, 80, 0)
    while analog(TOP_HAT) < 1800:
        pass
    # turns until the end of the black line
    drive(-40, 40, 0)
    while analog(TOP_HAT) > 1600:
        pass
    stop_motors()
    # turns left to line up with ddos
    ROBOT.run(drive, red=(-65, 65, 100))
    ROBOT.run(drive, blue=(-65, 65, 100))
    ROBOT.run(drive, yellow=(-65, 65, 100))
    # backs up to position wireshark under ddos
    ROBOT.run(drive_straight, red=(780, -1))
    ROBOT.run(drive_straight, blue=(780, -1))
    ROBOT.run(drive_straight, yellow=(780, -1))
    stop_motors()
    # waits for ddos to release ping pong balls at 60s
    ROBOT.run(msleep, red=5000)
    ROBOT.run(msleep, blue=5000)
    ROBOT.run(msleep, yellow=5000)


def ddos_to_analysis():
    # line follows to line up with delivery zone
    ROBOT.run(dramatic_line_follow, red=1800)
    ROBOT.run(dramatic_line_follow, blue=1800)
    ROBOT.run(dramatic_line_follow, yellow=1800)
    stop_motors()
    # turns left to line up with delivery zone
    ROBOT.run(drive, red=(0, 85, 1500))
    ROBOT.run(drive, blue=(0, 85, 1500))
    ROBOT.run(drive, yellow=(0, 85, 1500))
    # backs up to put wireshark in delivery zone
    ROBOT.run(drive_straight, red=(850, -1))
    ROBOT.run(drive_straight, blue=(850, -1))
    ROBOT.run(drive_straight, yellow=(850, -1))
    stop_motors()
    # releases wireshark
    move_servo_lego(BackClaw.UP)


def knock_over_rings():
    # moves away from rings to space the claw correctly
    ROBOT.run(drive_straight, red=800)
    ROBOT.run(drive_straight, blue=800)
    ROBOT.run(drive_straight, yellow=800)
    # turns right to prepare to knock over rings
    ROBOT.run(drive, red=(-80, 80, 1650))
    ROBOT.run(drive, blue=(-80, 80, 1650))
    ROBOT.run(drive, yellow=(-80, 80, 1650))
    stop_motors()
    # closes the claw and lowers the arm to prepare to knock over rings
    move_servo_lego(Claw.CLOSED, 0)
    move_servo_lego(Arm.RING, 4)
    # turns quickly to knock over rings
    ROBOT.run(drive, red=(-100, 100, 450))
    ROBOT.run(drive, blue=(-100, 100, 450))
    ROBOT.run(drive, yellow=(-100, 100, 450))
    stop_motors()


def get_noodle_one():
    drive(-60, 60, 0)
    while analog(TOP_HAT) < 1800:
        pass
    stop_motors()
    wait_for_button()
    ROBOT.run(drive, red=(-80, 80, 1400))
    ROBOT.run(drive, blue=(-80, 80, 1400))
    ROBOT.run(drive, yellow=(-80, 80, 1400))
    stop_motors()
