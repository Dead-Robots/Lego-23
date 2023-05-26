#!/usr/local/bin/python3.10 -u
from kipr import msleep

from actions import init, shut_down, get_botgal, deliver_botgal, get_wire_shark, ws_to_ddos, ddos_to_analysis, \
    knock_over_rings, get_noodle_one, deliver_noodle_one, yellow_get_noodle_one, yellow_deliver_noodle_one, \
    avoid_create, clap_claw
from common import ROBOT
from utilities import debug
import time
from common.gyro_movements import gyro_turn_test, straight_drive
from drive import straight_drive_distance

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
    elif ROBOT.is_yellow:
        print("I am YELLOW")
    elif ROBOT.is_green:
        print("I am GREEN")
    else:
        print("Help! I'm having an identity crisis (robot unidentified)")
        debug()
    init()
    straight_drive_distance(100, 24)
    # gyro_demo()
    # gyro_turn_test(0, 100, 180, 1)
    # start_time = time.time()
    # get_botgal()
    # deliver_botgal()
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
    shut_down()
