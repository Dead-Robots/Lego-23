from kipr import msleep, enable_servos, b_button, push_button, c_button, analog

import servo
from common import ROBOT
from common.multitasker import Multitasker
from common.post import post_core
from constants.ports import LEFT_TOP_HAT, RIGHT_TOP_HAT
from constants.sensors import push_sensor, TOP_HAT_THRESHOLD
from drive import drive, get_motor_positions, gyro_drive
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
    gyro_init(gyro_drive, stop_motors, get_motor_positions, push_sensor, 0.965, 0.06, 0.018, 0.3, 0.4)
    enable_servos()
    servo.move(Wrist.HORIZONTAL, 2)
    servo.move(Claw.SUPEROPEN, 2)
    servo.move(Arm.RET_LEVEL_3, 2)


def calibrate_drive_distance():
    servo.move(Arm.RET_LEVEL_0_25, 2)
    calibrate_straight_drive_distance(ROBOT.choose(red=10.5, blue=10, yellow=10, green=10.25), direction=-1)


def test_motors():
    straight_drive_distance(80, 12)
    gyro_turn(80, -80, 90)


def test_servos():
    servo.move(Arm.START, 2)
    msleep(300)
    servo.move(Arm.HORIZONTAL, 2)
    msleep(500)
    servo.move(Arm.RET_LEVEL_3, 2)
    msleep(300)
    servo.move(Arm.HORIZONTAL, 2)
    servo.move(Wrist.HORIZONTAL, 2)
    msleep(300)
    servo.move(Wrist.DIAGONAL, 2)
    msleep(300)
    servo.move(Wrist.VERTICAL, 2)
    msleep(300)
    servo.move(Wrist.HORIZONTAL, 2)
    servo.move(Claw.SUPEROPEN, 2)
    msleep(300)
    servo.move(Claw.CLOSE, 2)
    msleep(300)
    servo.move(Claw.SUPEROPEN, 2)
    servo.move(Arm.START, 2)


def test_sensors():
    print("Press push sensor.")
    while not push_sensor():
        pass
    while push_sensor():
        pass
    msleep(200)
    print("Push sensor input detected")

    # def condition():
    #     return analog(LEFT_TOP_HAT) < TOP_HAT_THRESHOLD
    #
    # def condition_2():
    #     return analog(RIGHT_TOP_HAT) > TOP_HAT_THRESHOLD
    #
    # print("Driving until left top hat sees black.")
    # straight_drive(80, condition)
    # print("Driving until right top hat sees white.")
    # straight_drive(80, condition_2)


def go_to_ret():
    # servo.move(Claw.SUPEROPEN, 0)
    # servo.move(Arm.RET_LEVEL_3, 4)
    straight_drive_distance(100, 5, False)
    stop_motors(150)
    gyro_turn(100, 0, 90, False)
    stop_motors(150)
    straight_drive_distance(100, 27, False)
    stop_motors(150)
    gyro_turn(100, -100, 90, False)
    stop_motors(150)
    straight_drive_distance(100, 18, False)
    gyro_turn(-100, 0, 20, False)
    straight_drive_distance(-100, 17, False)
    stop_motors(10)
    # # servo.move(Arm.RET_LEVEL_0, 2)
    # stop_motors(1500)
    # straight_drive_distance(-100, -2, False)
    # stop_motors(10)
    servo.move(Claw.OPEN, 2)
    servo.move(Arm.RET_LEVEL_0, 5)
    stop_motors(10)
    straight_drive_distance(100, 13, False)
    stop_motors(400)


def ret():
    servo.move(Claw.CLOSE, 2)
    msleep(400)
    straight_drive_distance(-100, 2, False)
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
    gyro_turn(0, 100, 15, False)
    stop_motors(100)
    servo.move(Wrist.DROP, 2)
    # opening claw in the good position
    servo.move(Claw.OPEN, 0)


def get_firewall():
    straight_drive_distance(-100, 5, False)
    stop_motors(100)
    gyro_turn(0, -100, 33, False)
    stop_motors(100)
    straight_drive_distance(-100, 6, False)
    stop_motors(100)
    servo.move(Wrist.HORIZONTAL, 0)
    servo.move(Arm.GRAB_FIREWALL, 5)
    straight_drive_distance(100, 13, False)
    stop_motors(100)
    servo.move(Claw.FIREWALL, 2)
    msleep(200)


def deliver_firewall():
    straight_drive_distance(-100, 12, False)
    stop_motors(100)
    servo.move(Arm.LIFT_FIREWALL, 3)
    gyro_turn(100, 0, 135, False)
    stop_motors(100)
    straight_drive_distance(100, 30, False)
    stop_motors(100)
    gyro_turn(100, 0, 12, False)
    stop_motors(100)
    servo.move(Arm.LIFT_FIREWALL_SLIGHTLY, 4)
    straight_drive_distance(100, 22, False)
    stop_motors(100)
    gyro_turn(100, 0, 30, False)
    stop_motors(100)
    straight_drive_distance(100, 6, False)
    stop_motors(100)
    servo.move(Arm.GRAB_FIREWALL, 2)
    servo.move(Claw.SUPEROPEN, 0)
    msleep(100)
    gyro_turn(100, 0, 5, False)
    stop_motors(100)


def return_from_enc():
    straight_drive_distance(-100, 9, False)
    stop_motors(100)
    gyro_turn(-100, 0, 40, False)
    stop_motors(100)
    straight_drive_distance(-100, 35.5, False)
    stop_motors(100)
    gyro_turn(100, 0, 93, False)
    stop_motors(100)


def activate_alarm():
    servo.move(Claw.SUPEROPEN, 0)
    servo.move(Arm.LIFT_FIREWALL_SLIGHTLY, 6)
    straight_drive_distance(-100, 5, False)
    stop_motors(100)
    gyro_turn(-100, 0, 270, False)
    stop_motors(100)
    servo.move(Arm.ALARM_SQUARE_UP, 2)
    straight_drive_distance(100, 10, False)
    stop_motors(100)
    gyro_turn(100, -100, 90, False)
    stop_motors(100)
