#!/usr/local/bin/python3.10 -u
from actions import init, servo_value_test, ret, go_to_ret
from common import ROBOT
from constants.servos import Wrist, Arm, Claw
from utilities import debug, wait_for_button

start_time = 0

if __name__ == '__main__':
    if ROBOT.is_blue:
        print("I am BLUE")
    elif ROBOT.is_red:
        print("I am RED")
    elif ROBOT.is_yellow:
        print("I am YELLOW")
    elif ROBOT.is_green:
        print("I am GREEN")
    else:
        print("Help! I'm having an identity crisis (robot unidentified)")
        debug()
    init()
    # servo_value_test(Claw)
    # wait_for_button('click button to start run')
    go_to_ret()
    ret()
