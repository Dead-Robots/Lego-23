#!/usr/local/bin/python3.10 -u
from kipr import b_button, freeze, c_button, a_button, get_motor_position_counter, clear_motor_position_counter, \
    push_button

from common import ROBOT
from constants.ports import LEFT_MOTOR, RIGHT_MOTOR
from drive import drive, straight_timed_fast, straight_distance_fast, straight_distance_slow
from utilities import wait_for_button, stop_motors


def choose_to_calibrate():
    while not push_button():
        print("Press 'B' to calibrate drive, push button to skip")
        while True:
            if b_button():
                while b_button():
                    pass
                run_calibration()
                break
            elif push_button():
                break
    while push_button():
        pass


# Press the green button in the gutter to run the script.
def run_calibration():
    calibrate_drive_offset(85, "fast", 5000)
    wait_for_button()
    calibrate_drive_offset(45, "slow", 8000)
    wait_for_button()
    calibrate_distance_from_ticks(10000)
    wait_for_button()


def calibrate_drive_offset(base_speed, name: str, duration=7500):
    print("Calibrate drive for", name)
    print("A go more right, C go more left, B when done")
    offset = ROBOT.load(name) or 0
    print("Starting with offset", offset)
    starting_left = base_speed
    starting_right = base_speed
    while not b_button():
        print(starting_left, starting_right + offset)
        drive(starting_left, starting_right + offset, duration)
        stop_motors()
        while True:
            if a_button():
                print("Went too far left - offset decreased")
                offset -= 1
                break
            elif c_button():
                print("Went too far right - offset increased")
                offset += 1
                break
            elif b_button():
                break
    while b_button():
        pass
    ROBOT.store(name, offset)
    print("Drive adjusted! New offset:", offset)


# def calibrate_distance_from_inches(inches):
#     print("Calibrate drive distance for", inches, "inches")
#     conversion = 1000
#     while not b_button():
#         clear_motor_position_counter(LEFT_MOTOR)
#         while get_motor_position_counter(LEFT_MOTOR) < conversion * inches:
#             straight_timed_fast(0)
#         stop_motors()
#         while True:
#             if c_button():
#                 while c_button():
#                     pass
#                 print("went too far right - offset decreased")
#                 conversion -= 100
#             elif a_button():
#                 while a_button():
#                     pass
#                 print("went too far left - offset increased")
#                 conversion += 100
#             elif b_button():
#                 while b_button():
#                     pass
#                 break
#     ROBOT.store("inches_to_ticks", conversion)
#     print("Drive adjusted! New conversion value:", conversion)


def get_a_number(default=0):
    print("A to increase value, C to decrease value, B when done")
    print("Starting value:", default)
    number = default
    while True:
        if c_button():
            while c_button():
                pass
            number -= 1
            print("Current value:", number)
        elif a_button():
            while a_button():
                pass
            number += 1
            print("Current value:", number)
        elif b_button():
            while b_button():
                pass
            print("Current value:", number)
            break
    while b_button():
        pass
    return number


def calibrate_distance_from_ticks(ticks):
    print("Calibrate drive distance for", ticks, "ticks")
    clear_motor_position_counter(LEFT_MOTOR)
    while get_motor_position_counter(LEFT_MOTOR) < ticks:
        straight_timed_fast(0, stop=False)
    stop_motors()
    print("Enter the number of inches that the robot drove")
    ones = get_a_number(50)
    print("Enter the additional tenths of inches that the robot drove")
    tenths = get_a_number()
    inches = ones + 0.1 * tenths
    conversion = ticks / inches
    ROBOT.store("inches_to_ticks", conversion)
    print("Drive adjusted! New conversion value:", conversion)


if __name__ == '__main__':
    run_calibration()
    straight_distance_fast(3*12)
    wait_for_button()
    straight_distance_slow(3*12)
    print("done!")
