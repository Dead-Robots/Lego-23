import math
import time
from time import sleep
from typing import Optional

from kipr import enable_servos, b_button, push_button, c_button, analog, disable_servos, \
    clear_motor_position_counter, motor_power, shut_down_in

import servo
from common import ROBOT
from common.light import wait_4_light
from common.multitasker import MultitaskedMotor
from common.post import post_core
from constants.ports import RAKE, LIGHT_SENSOR
from constants.sensors import push_sensor
from drive import drive, get_motor_positions, basic_drive, straight_drive_until_black_left, \
    straight_drive_until_white_right, straight_drive_until_black_right, straight_drive_until_black, \
    straight_drive_until_both_white, straight_drive_until_both_black, enable_grayson, square_up_top_hats, stop_motors
from utilities import debug, msleep
from constants.servos import Claw, Arm, Wrist
from common.gyro_movements import gyro_turn, straight_drive, straight_drive_distance, \
    calibrate_straight_drive_distance, gyro_init, wait_for_button

rake_manager: Optional[MultitaskedMotor] = None


def angle_test_claw():
    servo.move(Claw.FORTY_FIVE)
    wait_for_button("waiting for button")
    servo.move(Claw.ZERO)
    wait_for_button("waiting for button")


def init():
    post_core(test_servos, test_motors, test_sensors, initial_setup, calibrate_drive_distance)
    wait_4_light(LIGHT_SENSOR)
    shut_down_in(119)


def initial_setup():
    if ROBOT.is_red:
        gyro_init(basic_drive, stop_motors, get_motor_positions, push_sensor, 0.965, 0.06, 0.018, 0.3075, 0.4)
    elif ROBOT.is_green:
        gyro_init(basic_drive, stop_motors, get_motor_positions, push_sensor, 0.970, 0.06, 0.018, 0.6, 0.4)
    else:
        raise Exception("Gyro init not found. Currant colors are: RED and GREEN, make sure robot knows robot is robot")
    enable_grayson()
    enable_servos()
    global rake_manager
    motor_power(RAKE, -40)
    msleep(1000)
    motor_power(RAKE, -20)
    servo.move(Wrist.HORIZONTAL, 2)
    servo.move(Claw.SUPEROPEN, 2)
    servo.move(Arm.START, 2)
    clear_motor_position_counter(RAKE)
    rake_manager = MultitaskedMotor(RAKE, 0)


def calibrate_drive_distance():
    servo.move(Arm.RET_LEVEL_0_5, 4)
    calibrate_straight_drive_distance(ROBOT.choose(red=10.5, blue=10, yellow=10, green=10.25))


def test_motors():
    rake_manager.position = 500
    square_up_top_hats(60, 60, 3, timeout=False)
    stop_motors(100)
    straight_drive_until_both_white(60, False)
    stop_motors(100)
    rake_manager.position = 0
    straight_drive_distance(80, 5, False)
    stop_motors(100)
    gyro_turn(80, -80, 90)


def test_servos():
    servo.move(Arm.RET_DOWN, 3)
    msleep(300)
    servo.move(Arm.HORIZONTAL, 3)
    msleep(500)
    servo.move(Arm.RET_LEVEL_3, 3)
    msleep(300)
    servo.move(Arm.HORIZONTAL, 3)
    servo.move(Wrist.HORIZONTAL, 1)
    msleep(300)
    servo.move(Wrist.DIAGONAL, 1)
    msleep(300)
    servo.move(Wrist.VERTICAL, 1)
    msleep(300)
    servo.move(Wrist.HORIZONTAL, 1)
    servo.move(Claw.SUPEROPEN, 1)
    servo.move(Claw.CLOSE, 1)
    servo.move(Claw.SUPEROPEN, 1)
    servo.move(Arm.RET_DOWN, 3)


def test_sensors():

    print("Driving until left top hat sees black.")
    straight_drive_until_black_left(100, False)
    stop_motors()
    print("Driving until right top hat sees white.")
    straight_drive_until_white_right(100, False)
    msleep(500)
    gyro_turn(-100, 100, 180)
    straight_drive_distance(100, 14, True)


def go_to_ret():
    gyro_turn(-100, 100, 90, False)
    stop_motors(150)
    servo.move(Claw.CLOSE, 0)
    servo.move(Arm.UP, 2)
    straight_drive_until_black(100, False)
    straight_drive_distance(100, ROBOT.choose(red=27, green=25.5), False)
    stop_motors(150)
    gyro_turn(100, -100, 90, False)
    stop_motors(150)
    ROBOT.run(straight_drive_distance, red=(100, 9, False), green=(100, 11.5, False))
    gyro_turn(-100, 0, 20, False)
    straight_drive_distance(-100, 15.5, False)
    stop_motors(10)
    servo.move(Claw.OPEN, 0)
    servo.move(Arm.RET_LEVEL_0, 2)
    straight_drive_distance(100, 15, False)
    stop_motors(300)


def ret():
    servo.move(Claw.CLOSE, 2)
    straight_drive_distance(-100, 2.5, False)
    stop_motors(50)
    servo.move(Arm.RET_LEVEL_0_25, 1)
    straight_drive_distance(-100, 2, False)
    stop_motors(50)
    servo.move(Arm.RET_LEVEL_0_5, 1)
    servo.move(Wrist.DIAGONAL_HORIZONTAL, 1)
    servo.move(Arm.RET_LEVEL_0_75, 1)
    servo.move(Wrist.DIAGONAL, 1)
    servo.move(Arm.RET_LEVEL_1, 1)
    straight_drive_distance(-100, 1, False)
    stop_motors(50)
    gyro_turn(-100, -10, 6, False)
    stop_motors(50)
    straight_drive_distance(-100, 1, False)
    stop_motors(50)
    servo.move(Wrist.DIAGONAL_VERTICAL, 1)
    gyro_turn(-100, -10, 20, False)
    stop_motors(50)
    servo.move(Wrist.DIAGONAL_HORIZONTAL, 1)
    servo.move(Arm.RET_LEVEL_2, ROBOT.choose(red=3, green=3))
    servo.move(Wrist.DIAGONAL, 1)
    gyro_turn(-80, 100, 6, False)
    stop_motors(50)
    servo.move(Wrist.DIAGONAL_VERTICAL, 1)
    gyro_turn(-80, 100, 26, False)
    stop_motors(50)
    servo.move(Wrist.DIAGONAL_HORIZONTAL, 1)
    servo.move(Arm.RET_LEVEL_2_5, 1)
    straight_drive_distance(100, 2, False)
    stop_motors(50)
    servo.move(Arm.RET_LEVEL_2_75, 1)
    servo.move(Wrist.DIAGONAL, 1)
    servo.move(Arm.RET_LEVEL_3, 1)
    servo.move(Wrist.DIAGONAL_VERTICAL, 1)
    straight_drive_distance(100, 2, False)
    stop_motors(50)
    servo.move(Wrist.VERTICAL, 1)
    gyro_turn(30, 100, 10, False)
    stop_motors(50)
    gyro_turn(0, 100, 20, False)
    stop_motors(50)
    servo.move(Wrist.DROP, 1)
    straight_drive_distance(100, 1, False)
    stop_motors(50)
    # opening claw in the good position
    servo.move(Claw.OPEN, 0)
    msleep(200)
    straight_drive_distance(-100, 1, False)
    stop_motors(50)
    gyro_turn(0, -100, 3, False)
    stop_motors(50)


def get_firewall():
    straight_drive_distance(-100, 5, False)
    stop_motors(100)
    gyro_turn(0, -100, ROBOT.choose(red=34, green=36), False)
    stop_motors(100)
    straight_drive_distance(-100, 5, False)
    stop_motors(100)
    servo.move(Wrist.HORIZONTAL, 0)
    servo.move(Arm.GRAB_FIREWALL, 4)
    straight_drive_distance(100, ROBOT.choose(red=12, green=12.5), False)
    stop_motors(100)
    servo.move(Claw.FIREWALL, 2)
    msleep(200)


def deliver_firewall():
    straight_drive_distance(-100, ROBOT.choose(red=14, green=14.5), False)
    stop_motors(100)
    servo.move(Arm.LIFT_FIREWALL, 3)
    gyro_turn(100, -100, 50, False)
    stop_motors(100)
    straight_drive_distance(100, 10, False)
    drive(80, 80, 1200)
    stop_motors(100)
    msleep(300)
    straight_drive_distance(-100, 4, False)
    stop_motors(100)
    gyro_turn(100, -100, 90, False)
    stop_motors(100)
    straight_drive_distance(100, 10, False)
    straight_drive_until_black(100, False)
    square_up_top_hats(40, 40, 2)
    straight_drive_distance(100, 20, False)
    stop_motors(100)
    gyro_turn(30, -30, 12, False)
    stop_motors(100)
    straight_drive_distance(100, 10, False)
    straight_drive_until_both_black(100, False)
    stop_motors(100)
    servo.move(Arm.LIFT_FIREWALL_SLIGHTLY, 5)
    servo.move(Claw.SUPEROPEN, 2)
    straight_drive_distance(-100, 2, False)
    stop_motors(100)
    straight_drive_distance(100, 2, False)
    stop_motors(100)
    servo.move(Arm.GRAB_FIREWALL, 3)
    servo.move(Claw.FIREWALL, 2)
    servo.move(Arm.LIFT_FIREWALL_SLIGHTLY, 3)
    gyro_turn(100, 0, ROBOT.choose(red=16, green=36), False)
    stop_motors(100)
    straight_drive_distance(100, 6.5, False)
    stop_motors(100)
    # servo.move(Arm.GRAB_FIREWALL, 2)
    servo.move(Claw.SUPEROPEN, 0)
    msleep(100)
    gyro_turn(100, 0, 5, False)
    stop_motors(100)


def return_from_enc():
    straight_drive_distance(-100, ROBOT.choose(red=5.5, green=4.5), False)
    stop_motors(100)
    servo.move(Claw.CLOSE, 0)
    servo.move(Arm.DOWN, 3)
    gyro_turn(100, 0, 55, False)
    stop_motors(100)
    # square up
    straight_drive_distance(-100, 9.5, False)
    stop_motors(0)
    straight_drive_distance(100, 0.75, False)
    stop_motors(100)
    servo.move(Arm.ALARM_SQUARE_UP, 3)
    gyro_turn(100, -100, ROBOT.choose(red=121.5, green=121.5), False)
    stop_motors(100)
    straight_drive_distance(100, 6, False)
    stop_motors(100)
    gyro_turn(0, 100, ROBOT.choose(red=36, green=31), False)
    stop_motors(100)
    straight_drive_distance(100, 10, False)
    straight_drive_until_black(100, False)
    straight_drive_distance(100, 5, False)
    straight_drive_until_black(100, False)
    square_up_top_hats(40, 40, 2)
    straight_drive_distance(100, 15, False)
    stop_motors(100)


def activate_alarm():
    gyro_turn(0, 100, 90, False)
    stop_motors(100)
    straight_drive_until_black(100, False)
    square_up_top_hats(40, 40, 3)
    stop_motors(100)
    straight_drive_distance(100, 0.8, False)
    stop_motors(100)
    servo.move(Claw.OPEN, 0)
    gyro_turn(100, 0, ROBOT.choose(red=90, green=93), False)
    stop_motors(100)
    straight_drive_distance(100, 6, False)
    stop_motors(100)
    straight_drive_distance(-100, ROBOT.choose(red=1.5, green=1), False)
    stop_motors(100)
    servo.move(Arm.BELOW_ALARM, 4)
    msleep(100)
    servo.move(Arm.ABOVE_ALARM, 0)
    msleep(600)
    servo.move(Arm.ALARM_SQUARE_UP, 0)
    straight_drive_distance(-100, 2.25, False)
    stop_motors(100)
    servo.move(Arm.RET_DOWN, 4)


def get_enc_key():
    straight_drive_distance(100, ROBOT.choose(red=2.25, green=2.25), False)
    stop_motors(100)
    gyro_turn(100, -100, ROBOT.choose(red=90, green=91), False)
    stop_motors(100)
    rake_manager.position = 350
    straight_drive_distance(-100, 15.5, False)
    stop_motors(0)
    rake_manager.position = 450
    straight_drive_distance(100, 0.1, False)
    rake_manager.position = 520
    straight_drive_distance(100, 6, False)

    # For single seeding:

    stop_motors(100)
    rake_manager.position = 30
    straight_drive_distance(100, 4, False)
    stop_motors(100)

    # For DE and/or double seeding:

    # stop_motors(100)
    # rake_manager.position = 420
    # straight_drive_distance(-100, 2, False)
    # stop_motors(100)
    # rake_manager.position = 540


def shutdown(start_time):
    print("Push button to disable servos.")
    while (time.time() - start_time) < 30 and not push_button():
        pass
    rake_manager.position = 0
    servo.move(Claw.OPEN, 0)
    servo.move(Wrist.HORIZONTAL, 2)
    servo.move(Arm.RET_DOWN, 4)
    rake_manager.running = False
    disable_servos()
    exit(0)
