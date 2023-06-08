#!/usr/local/bin/python3.10 -u
from kipr import msleep, enable_servos

from actions import init, shut_down, get_botgal, deliver_botgal, get_wire_shark, ws_to_ddos, ddos_to_analysis, \
    knock_over_rings, get_noodle_one, deliver_noodle_one, yellow_get_noodle_one, yellow_deliver_noodle_one, \
    avoid_create, clap_claw, move_hook, angle_test_arm, angle_test_claw, rev
from common import ROBOT
from constants.servos import translate_arm
from utilities import debug
import time

start_time = 0

if __name__ == '__main__':
    # drive calibration code:
    # run_calibration()
    # straight_distance_fast(3 * 12)
    # wait_for_button()
    # straight_distance_slow(3 * 12)
    # print("done!")
    # enable_servos()
    # move_hook()
    # angle_test_arm()
    # angle_test_claw()
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
    rev()
    # start_time = time.time()
    # # get_botgal()
    # # deliver_botgal()
    # move_hook()
    # exit(0)
    # get_wire_shark()
    # ws_to_ddos()
    # while time.time() - start_time < 60.8:
    #     msleep(10)
    # ddos_to_analysis()
    # knock_over_rings()
    #
    # if ROBOT.is_yellow:
    #     yellow_get_noodle_one()
    #     yellow_deliver_noodle_one()
    #
    # else:
    #     get_noodle_one()
    #     deliver_noodle_one()
    # avoid_create()
    # while time.time() - start_time < 114:
    #     msleep(10)
    # clap_claw()
    # shut_down()
