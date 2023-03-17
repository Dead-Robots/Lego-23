#!/usr/local/bin/python3.10 -u

from actions import init, shut_down, get_botgal, deliver_botgal, wire_shark, ws_to_ddos, ddos_to_analysis
from drive import drive, stop_motors, drive_straight
from common import ROBOT
from utilities import wait_for_button

# TODO: hardware needs to fix blue claw, can't grab botgal. deliver ws to analysis lab, figure out spacing with other
#  objects


if __name__ == '__main__':
    if ROBOT.is_blue:
        print("hi I am blue start")
        init()
        get_botgal()
        deliver_botgal()
        wire_shark()
        ws_to_ddos()
        ddos_to_analysis()
        shut_down()
    elif ROBOT.is_red:
        print("hi I am red start")
        init()
        get_botgal()
        deliver_botgal()
        wire_shark()
        ws_to_ddos()
        shut_down()
    elif ROBOT.is_yellow:
        print("hi I am yellow start")
        init()
        get_botgal()
        # TODO: verify that get_botgal() works with the yellow robot, finish deliver_botgal()
        deliver_botgal()
        # wire_shark()
        shut_down()
    elif ROBOT.is_green:
        print("hi I am green start")
    else:
        print("robot unidentified")
