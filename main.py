#!/usr/local/bin/python3.10 -u
from kipr import enable_servos, msleep

from actions import init, shut_down, get_botgal, deliver_botgal, get_wire_shark, ws_to_ddos, ddos_to_analysis, \
    knock_over_rings, get_noodle_one, deliver_noodle_one
from common import ROBOT
from utilities import wait_for_button, debug
from calibrate import *
from drive import drive_straight
import time

start_time = 0

if __name__ == '__main__':
    # drive calibration code:
    # run_calibration()
    # straight_distance_fast(3 * 12)
    # wait_for_button()
    # straight_distance_slow(3 * 12)
    # print("done!")

    if ROBOT.is_blue:
        print("I am BLUE")
    elif ROBOT.is_red:
        print("I am RED")
    elif ROBOT.is_yellow:  # not tested
        print("I am YELLOW")
    else:
        print("Help! I'm having an identity crisis (robot unidentified)")
        debug()
    init()
    start_time = time.time()
    get_botgal()
    deliver_botgal()
    get_wire_shark()
    ws_to_ddos()
    while time.time() - start_time < 60.8:
        msleep(10)
    ddos_to_analysis()
    knock_over_rings()
    get_noodle_one()
    deliver_noodle_one()
    shut_down()
