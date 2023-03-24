#!/usr/local/bin/python3.10 -u
from kipr import enable_servos

from actions import init, shut_down, get_botgal, deliver_botgal, wire_shark, ws_to_ddos, ddos_to_analysis, knock_over_rings, get_noodle_one
from drive import drive, stop_motors, drive_straight
from common import ROBOT
from utilities import wait_for_button

# TODO: hardware needs to fix blue claw, can't grab botgal. deliver ws to analysis lab, figure out spacing with other
#  objects


if __name__ == '__main__':
    if ROBOT.is_blue:
        print("I am BLUE")
        init()
        get_botgal()
        deliver_botgal()
        wire_shark()
        ws_to_ddos()
        ddos_to_analysis()
        knock_over_rings()
        get_noodle_one()
        shut_down()
    elif ROBOT.is_red:
        print("I am RED")
        init()
        get_botgal()
        deliver_botgal()
        wire_shark()
        ws_to_ddos()
        # wait_for_button("Waiting for ping pong balls.")
        ddos_to_analysis()
        knock_over_rings()
        # wait_for_button()
        # get_noodle_one()
        shut_down()
    elif ROBOT.is_yellow:
        print("I am YELLOW")
        init()
        get_botgal()
        # TODO: verify that get_botgal() works with the yellow robot, finish deliver_botgal()
        deliver_botgal()
        # wire_shark()
        shut_down()
    elif ROBOT.is_green:
        print("I am GREEN")
    else:
        print("robot unidentified")
