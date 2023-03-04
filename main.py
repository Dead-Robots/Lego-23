#!/usr/local/bin/python3.10 -u

from actions import init, shut_down, get_botgal, deliver_botgal, go_to_ws, wireshark_to_ddos, wire_shark
from utilities import wait_for_button
from common import ROBOT

if __name__ == '__main__':
    if ROBOT.is_red or ROBOT.is_blue:
        print("Hi, I am red or blue. Started.")
        init()
        get_botgal()
        # TODO: verify that get_botgal() works with the blue robot, finish deliver_botgal()
        deliver_botgal()
        #wait_for_button()
        wire_shark()
        wireshark_to_ddos()
        shut_down()
    elif ROBOT.is_yellow:
        print("hi I am yellow start")
        init()
        # go_to_botgal()
        # to_analysis_lab()
        # wait_for_button()
        go_to_ws()
        wait_for_button()
        # TODO: Fix turn once at wireshark, Lower ws_plow, Line follow right to DDOS
        #ws_to_ddos()
        wait_for_button()
        shut_down()
        print("end")
    else:
        print("robot unidentified")
