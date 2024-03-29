#!/usr/local/bin/python3.10 -u
from actions import init, ret, go_to_ret, get_firewall, deliver_firewall, return_from_enc, activate_alarm, shutdown,\
    get_enc_key
from common import ROBOT
from common.gyro_movements import gyro_turn_test
from utilities import debug
import time


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
    init(is_seeding=True)
    start_time = time.time()
    go_to_ret()
    ret()
    get_firewall()
    deliver_firewall()
    firewall_time = time.time()
    print(str(firewall_time-start_time) + " seconds elapsed when firewall dropped.")
    return_from_enc()
    activate_alarm()
    get_enc_key()
    end_time = time.time()
    print(str(round(end_time-start_time, 2)) + " seconds elapsed when finished.")
    shutdown(end_time)
