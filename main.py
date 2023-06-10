#!/usr/local/bin/python3.10 -u
from actions import init, servo_value_test, ret
from common import ROBOT
from constants.servos import Wrist, Arm, Claw
from utilities import debug

start_time = 0

if __name__ == '__main__':
    if ROBOT.is_blue:
        print("I am BLUE")
    elif ROBOT.is_red:
        print("I am RED")
    elif ROBOT.is_yellow:
        print("I am YELLOW")
    else:
        print("Help! I'm having an identity crisis (robot unidentified)")
        debug()
    init()
    # servo_value_test(Wrist)
    ret()
