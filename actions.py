import math
import time

from kipr import msleep, enable_servos, b_button, push_button, c_button, analog, disable_servos

import servo
from common import ROBOT
from common.multitasker import Multitasker
from common.post import post_core
from constants.ports import LEFT_TOP_HAT, RIGHT_TOP_HAT
from constants.sensors import push_sensor, TOP_HAT_THRESHOLD
from drive import drive, get_motor_positions, gyro_drive, straight_drive_until_black_left, \
    straight_drive_until_white_right, straight_drive_until_black_right, drive_until_black, drive_until_white, \
    straight_drive_until_black, straight_drive_until_white, left_on_white, left_on_black, right_on_black, \
    right_on_white, drive_until_both_white, straight_drive_until_both_white, straight_drive_until_both_black, \
    enable_motor_2, square_up_top_hats
from utilities import wait_for_button, stop_motors, debug
from constants.servos import Claw, Arm, Wrist
from common.gyro_movements import gyro_turn, straight_drive, straight_drive_distance, \
    calibrate_straight_drive_distance, gyro_init


def angle_test_claw():
    servo.move(Claw.FORTY_FIVE)
    wait_for_button("waiting for button")
    servo.move(Claw.ZERO)
    wait_for_button("waiting for button")


def servo_value_test(servo1):
    if servo1 == Claw:
        try:
            servo.move(Claw.OPEN, 1)
        except ValueError:
            print("Claw.OPEN does not exist.")
        wait_for_button("Press button to test next value.")
        try:
            servo.move(Claw.CLOSE, 1)
        except ValueError:
            print("Claw.OPEN does not exist.")
    elif servo1 == Arm:
        try:
            servo.move(Arm.RET_LEVEL_0, 1)
        except ValueError:
            print("Arm.DOWN does not exist.")
        wait_for_button("Press button to test next value.")
        try:
            servo.move(Arm.RET_LEVEL_1, 1)
        except ValueError:
            print("Arm.LOW does not exist.")
        wait_for_button("Press button to test next value.")
        try:
            servo.move(Arm.LOWER, 1)
        except ValueError:
            print("Arm.LOWER does not exist.")
        wait_for_button("Press button to test next value.")
        try:
            servo.move(Claw.MIDDLE, 1)
        except ValueError:
            print("Arm.MIDDLE does not exist.")
        wait_for_button("Press button to test next value.")
        try:
            servo.move(Claw.HIGH, 1)
        except ValueError:
            print("Arm.HIGH does not exist.")
    elif servo1 == Wrist:
        try:
            servo.move(Wrist.HORIZONTAL, 1)
        except ValueError:
            print("Wrist.HORIZONTAL does not exist.")
        wait_for_button("Press button to test next value.")
        try:
            servo.move(Wrist.DIAGONAL_HORIZONTAL, 1)
        except ValueError:
            print("Wrist.DIAGONAL_HORIZONTAL does not exist.")
        wait_for_button("Press button to test next value.")
        try:
            servo.move(Wrist.DIAGONAL, 1)
        except ValueError:
            print("Wrist.DIAGONAL does not exist.")
        wait_for_button("Press button to test next value.")
        try:
            servo.move(Wrist.DIAGONAL_VERTICAL, 1)
        except ValueError:
            print("Wrist.DIAGONAL_VERTICAL does not exist.")
        wait_for_button("Press button to test next value.")
        try:
            servo.move(Wrist.VERTICAL, 1)
        except ValueError:
            print("Wrist.VERTICAL does not exist.")
    else:
        print("Unknown Servo, add test values to servo_value_test() in actions.")


def init():
    post_core(test_servos, test_motors, test_sensors, initial_setup, calibrate_drive_distance)
    msleep(500)


def initial_setup():
    if ROBOT.is_red:
        gyro_init(gyro_drive, stop_motors, get_motor_positions, push_sensor, 0.965, 0.06, 0.018, 0.3075, 0.4)
    elif ROBOT.is_green:
        gyro_init(gyro_drive, stop_motors, get_motor_positions, push_sensor, 0.92, 0.08, 0.018, 0.3075, 0.4)
    else:
        raise Exception("Gyro init not found. Currant colors are: RED and GREEN, make sure robot knows robot is robot")
    enable_motor_2()
    enable_servos()
    servo.move(Wrist.HORIZONTAL, 2)
    servo.move(Claw.SUPEROPEN, 2)
    servo.move(Arm.RET_DOWN, 2)


def calibrate_drive_distance():
    servo.move(Arm.RET_LEVEL_0_5, 4)
    calibrate_straight_drive_distance(ROBOT.choose(red=10.5, blue=10, yellow=10, green=10.25))


def test_motors():
    straight_drive_distance(80, 12)
    gyro_turn(80, -80, 90)


def test_servos():
    servo.move(Arm.RET_DOWN, 3)
    msleep(300)
    servo.move(Arm.HORIZONTAL, 3)
    msleep(500)
    servo.move(Arm.RET_LEVEL_3, 3)
    msleep(300)
    servo.move(Arm.HORIZONTAL, 3)
    servo.move(Wrist.HORIZONTAL, 3)
    msleep(300)
    servo.move(Wrist.DIAGONAL, 3)
    msleep(300)
    servo.move(Wrist.VERTICAL, 3)
    msleep(300)
    servo.move(Wrist.HORIZONTAL, 3)
    servo.move(Claw.SUPEROPEN, 3)
    msleep(300)
    servo.move(Claw.CLOSE, 3)
    msleep(300)
    servo.move(Claw.SUPEROPEN, 3)
    servo.move(Arm.RET_DOWN, 3)


def test_sensors():

    print("Driving until left top hat sees black.")
    straight_drive_until_black_left(80)
    print("Driving until right top hat sees white.")
    straight_drive_until_white_right(80)


def go_to_ret():
    gyro_turn(-80, 80, 90)
    servo.move(Arm.UP, 2)
    straight_drive_distance(80, 30.5)
    gyro_turn(80, -80, 90)
    ROBOT.run(straight_drive_distance,
              red=(100, 8, False), green=(100, 6, False))
    gyro_turn(-100, 0, 20, False)
    straight_drive_distance(-100, 17, False)
    stop_motors(10)
    servo.move(Claw.OPEN, 2)
    servo.move(Arm.RET_LEVEL_0, 4)
    stop_motors(10)
    straight_drive_distance(100, 16.5, False)
    stop_motors(400)


def ret():
    servo.move(Claw.CLOSE, 2)
    msleep(400)
    straight_drive_distance(-100, 2.5, False)
    stop_motors(100)
    servo.move(Arm.RET_LEVEL_0_25, 2)
    straight_drive_distance(-100, 2, False)
    stop_motors(100)
    servo.move(Arm.RET_LEVEL_0_5, 2)
    servo.move(Wrist.DIAGONAL_HORIZONTAL)
    servo.move(Arm.RET_LEVEL_0_75)
    servo.move(Wrist.DIAGONAL, 2)
    servo.move(Arm.RET_LEVEL_1)
    straight_drive_distance(-100, 1, False)
    stop_motors(100)
    gyro_turn(-100, -10, 6, False)
    stop_motors(100)
    servo.move(Wrist.DIAGONAL_VERTICAL, 2)
    gyro_turn(-100, -10, 20, False)
    stop_motors(100)
    servo.move(Wrist.DIAGONAL_HORIZONTAL, 2)
    servo.move(Arm.RET_LEVEL_2, 2)
    servo.move(Wrist.DIAGONAL, 2)
    gyro_turn(-80, 100, 6, False)
    stop_motors(100)
    servo.move(Wrist.DIAGONAL_VERTICAL, 2)
    gyro_turn(-80, 100, 26, False)
    stop_motors(100)
    servo.move(Wrist.DIAGONAL_HORIZONTAL, 2)
    servo.move(Arm.RET_LEVEL_2_5, 2)
    straight_drive_distance(100, 2, False)
    stop_motors(100)
    servo.move(Arm.RET_LEVEL_2_75, 2)
    servo.move(Wrist.DIAGONAL, 2)
    servo.move(Arm.RET_LEVEL_3, 2)
    servo.move(Wrist.DIAGONAL_VERTICAL, 2)
    straight_drive_distance(100, 2, False)
    stop_motors(100)
    servo.move(Wrist.VERTICAL, 2)
    gyro_turn(30, 100, 10, False)
    stop_motors(100)
    gyro_turn(0, 100, 17, False)
    stop_motors(100)
    servo.move(Wrist.DROP, 2)
    # opening claw in the good position
    servo.move(Claw.OPEN, 0)


def get_firewall():
    straight_drive_distance(-100, 5, False)
    stop_motors(100)
    gyro_turn(0, -100, 34, False)
    stop_motors(100)
    straight_drive_distance(-100, 5, False)
    stop_motors(100)
    servo.move(Wrist.HORIZONTAL, 0)
    servo.move(Arm.GRAB_FIREWALL, 5)
    straight_drive_distance(100, 12, False)
    stop_motors(100)
    servo.move(Claw.FIREWALL, 2)
    msleep(200)


def deliver_firewall():
    ROBOT.run(straight_drive_distance,
              red=(-100, 13, False), green=(-100, 14, False))
    stop_motors(100)
    servo.move(Arm.LIFT_FIREWALL, 3)
    gyro_turn(100, 0, 140, False)
    stop_motors(100)
    straight_drive_until_black_right(100, False)
    stop_motors(100)
    straight_drive_until_both_white(-60, False)
    stop_motors(100)
    square_up_top_hats()
    gyro_turn(100, 0, 6, False)
    stop_motors(100)
    straight_drive_distance(100, 30, False)
    straight_drive_until_both_black(100, False)
    stop_motors(100)
    servo.move(Arm.LIFT_FIREWALL_SLIGHTLY, 5)
    gyro_turn(100, 0, 44.5, False)
    stop_motors(100)
    straight_drive_distance(100, 6.5, False)
    stop_motors(100)
    servo.move(Arm.GRAB_FIREWALL, 2)
    servo.move(Claw.SUPEROPEN, 0)
    msleep(100)
    gyro_turn(100, 0, 5, False)
    stop_motors(100)


def return_from_enc():
    straight_drive_distance(-100, 4.5, False)
    stop_motors(100)
    servo.move(Arm.DOWN, 3)
    gyro_turn(100, 0, 55, False)
    stop_motors(100)
    straight_drive_distance(-100, 2, False)
    stop_motors(100)
    gyro_turn(0, 100, 10, False)
    stop_motors(100)
    straight_drive_distance(-80, 4, False)
    stop_motors(100)
    straight_drive_distance(100, 0.75, False)
    stop_motors(100)
    servo.move(Arm.ALARM_SQUARE_UP, 3)
    gyro_turn(100, -100, 118, False)
    stop_motors(100)
    straight_drive_distance(100, 6, False)
    stop_motors(100)
    gyro_turn(0, 100, 34, False)
    stop_motors(100)
    straight_drive_distance(100, 32, False)
    stop_motors(100)


def activate_alarm():
    gyro_turn(0, 100, 20, False)
    stop_motors()
    straight_drive_distance(100, 10, False)
    stop_motors(100)
    gyro_turn(0, 100, 25, False)
    stop_motors(100)
    straight_drive_until_black_right(100, False)
    stop_motors(100)
    gyro_turn(100, 0, 46, False)
    stop_motors(100)
    straight_drive_distance(100, 11, False)
    stop_motors(100)
    straight_drive_distance(-100, 0.95, False)
    stop_motors(100)
    servo.move(Arm.BELOW_ALARM, 4)
    msleep(100)
    servo.move(Arm.ABOVE_ALARM, 0)
    msleep(400)
    servo.move(Arm.ALARM_SQUARE_UP, 0)
    straight_drive_distance(-100, 2, False)
    stop_motors(100)
    servo.move(Arm.ABOVE_ALARM, 4)


def get_enc_key():
    gyro_turn(100, -100, 110)
    straight_drive_distance(-80, 14)
    gyro_turn(-80, 0, 30)
    wait_for_button()
    drive(-60, -60, 1000)
    wait_for_button()


def get_noodle_one():
    gyro_turn(100, -100, 130, False)
    stop_motors(100)
    servo.move(Wrist.HORIZONTAL, 0)
    servo.move(Arm.NOODLE_GRAB, 4)
    straight_drive_distance(100, 16.5, False)
    stop_motors(100)
    servo.move(Claw.CLOSE, 1)
    msleep(100)
    servo.move(Arm.NOODLE_LIFT, 4)


def deliver_noodle_one():
    straight_drive_distance(-100, 1, False)
    gyro_turn(100, -100, 165, False)
    stop_motors(100)
    straight_drive_until_black(100, False)
    stop_motors(100)
    square_up_top_hats()
    gyro_turn(100, 0, 6, False)
    stop_motors(100)
    straight_drive_distance(100, 25, False)
    stop_motors(100)
    wait_for_button()
    straight_drive_distance(-100, 4.5, False)
    stop_motors(100)
    gyro_turn(-100, 100, 120, False)
    stop_motors(100)
    servo.move(Wrist.NOODLE_DEL, 0)
    servo.move(Arm.NOODLE_DELIVERY, 4)
    gyro_turn(100, -100, 50, False)
    stop_motors(100)
    wait_for_button()
    gyro_turn(100, 0, 14, False)
    stop_motors(100)
    servo.move(Claw.OPEN, 2)
    straight_drive_distance(-100, 6,  False)
    stop_motors(100)
    servo.move(Wrist.HORIZONTAL, 0)
    servo.move(Arm.NOODLE_GRAB, 5)


def shutdown(start_time):
    print("Push button to disable servos.")
    while (time.time() - start_time) < 30 and not push_button():
        pass
    servo.move(Claw.OPEN, 2)
    servo.move(Wrist.HORIZONTAL, 2)
    servo.move(Arm.RET_DOWN, 4)
    disable_servos()
