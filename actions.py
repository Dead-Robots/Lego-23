from kipr import msleep, enable_servos

import servo
from common.multitasker import Multitasker
from constants.sensors import push_sensor
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
            servo.move(Arm.DOWN, 1)
        except ValueError:
            print("Arm.DOWN does not exist.")
        wait_for_button("Press button to test next value.")
        try:
            servo.move(Arm.LOW, 1)
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
    gyro_init(gyro_drive, stop_motors, get_motor_positions, push_sensor, 0.975, 0.05, 0.018, 0.3, 0.4)
    enable_servos()
    wait_for_button("Begin run?")


def ret():
    servo.move(Claw.OPEN, 2)
    servo.move(Wrist.HORIZONTAL, 2)
    servo.move(Arm.DOWN, 2)
    wait_for_button("Press button to close claw.")
    servo.move(Claw.CLOSE, 2)
    wait_for_button("Press button to start.")
    servo.move(Arm.LOW_LOW_DOWN, 2)
    straight_drive_distance(-20, 2)
    servo.move(Arm.LOW_DOWN, 2)
    straight_drive_distance(-20, 1)
    servo.move(Wrist.DIAGONAL_HORIZONTAL)
    servo.move(Arm.HIGH_LOW_DOWN)
    servo.move(Wrist.DIAGONAL, 2)
    servo.move(Arm.LOW)

    gyro_turn(-30, -20, 3)
    servo.move(Wrist.DIAGONAL_VERTICAL, 2)
    gyro_turn(-30, -10, 4)
    servo.move(Wrist.VERTICAL, 2)
    gyro_turn(-30, -10, 4)
    servo.move(Wrist.DIAGONAL_VERTICAL, 2)
    gyro_turn(-30, -20, 3)
    servo.move(Wrist.DIAGONAL, 2)
    servo.move(Wrist.DIAGONAL_HORIZONTAL, 2)
    servo.move(Arm.LOW_MIDDLE_LOW, 2)
    servo.move(Wrist.HORIZONTAL, 2)
    servo.move(Arm.MIDDLE_LOW, 2)
    servo.move(Wrist.DIAGONAL_HORIZONTAL, 2)
    servo.move(Arm.HIGH_MIDDLE_LOW, 2)
    servo.move(Wrist.DIAGONAL, 2)
    servo.move(Arm.MIDDLE, 2)

    servo.move(Wrist.DIAGONAL_VERTICAL, 2)
    gyro_turn(-20, -5, 12)
    servo.move(Wrist.DIAGONAL, 2)
    gyro_turn(5, 30, 5)
    servo.move(Wrist.DIAGONAL_HORIZONTAL, 2)
    servo.move(Arm.LOW_MIDDLE_HIGH, 2)
    servo.move(Wrist.HORIZONTAL, 2)
    servo.move(Arm.MIDDLE_HIGH, 2)
    straight_drive_distance(30, 2)
    servo.move(Wrist.DIAGONAL_HORIZONTAL, 2)
    servo.move(Arm.HIGH_MIDDLE_HIGH, 2)
    servo.move(Wrist.DIAGONAL, 2)
    servo.move(Arm.HIGH, 2)

    straight_drive_distance(20, 1)
    servo.move(Wrist.DIAGONAL_VERTICAL, 2)
    gyro_turn(-10, 30, 2)
    servo.move(Wrist.VERTICAL, 2)
    gyro_turn(0, 30, 10)

    servo.move(Claw.OPEN, 2)
    straight_drive_distance(-60, 8)
    servo.move(Wrist.HORIZONTAL, 2)
    servo.move(Arm.DOWN, 2)
