#!/usr/local/bin/python3.10 -u

from actions import init, shut_down, get_botgal, deliver_botgal, wire_shark
from drive import drive, stop_motors, drive_straight
from common import ROBOT
from utilities import wait_for_button

if __name__ == '__main__':
    if ROBOT.is_blue:
        print("hi I am blue start")
        init()
        get_botgal()
        # TODO: verify that get_botgal() works with the blue robot, finish deliver_botgal()
        deliver_botgal()
        wire_shark()
        shut_down()
    elif ROBOT.is_red or ROBOT.is_yellow:
        print("hi I am red or yellow start")
        init()
        get_botgal()
        wait_for_button()
        # TODO: verify that get_botgal() works with the blue robot, finish deliver_botgal()
        deliver_botgal()
        # wire_shark()
        shut_down()
    elif ROBOT.is_green:
        print("hi I am green start")
    else:
        print("robot unidentified")
