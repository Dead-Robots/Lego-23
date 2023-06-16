from kipr import msleep, enable_servos, b_button, push_button

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
    gyro_init(gyro_drive, stop_motors, get_motor_positions, push_sensor, 0.975, 0.08, 0.018, 0.3, 0.4)
    enable_servos()
    print("Press 'B' to run the POST.\nPress the button to begin the run.")
    while not push_button():
        if b_button():
            while b_button():
                pass
            msleep(250)
            post()
    msleep(500)


def post():
    print("Starting POST.")
    servo.move(Wrist.HORIZONTAL, 2)
    msleep(300)
    servo.move(Arm.START, 2)
    msleep(300)
    servo.move(Arm.HORIZONTAL, 2)
    servo.move(Claw.CLOSE, 2)
    servo.move(Claw.OPEN, 2)
    servo.move(Claw.CLOSE, 2)
    msleep(300)
    servo.move(Arm.RET_LEVEL_3, 2)
    msleep(300)
    servo.move(Claw.CLOSE, 2)
    servo.move(Claw.OPEN, 2)
    servo.move(Claw.CLOSE, 2)
    msleep(300)
    servo.move(Wrist.HORIZONTAL, 2)
    msleep(300)
    servo.move(Wrist.VERTICAL, 2)
    msleep(300)
    servo.move(Wrist.HORIZONTAL, 2)
    msleep(300)
    servo.move(Arm.START, 2)
    servo.move(Claw.SUPEROPEN, 2)
    msleep(500)
    straight_drive_distance(80, 12)
    gyro_turn(80, 0, 90)
    print("POST Complete.")


def go_to_ret():
    servo.move(Arm.RET_LEVEL_0_75, 2)
    straight_drive_distance(100, 15)
    gyro_turn(100, 0, 90)
    straight_drive_distance(100, 17.3)
    gyro_turn(100, 0, 70)
    servo.move(Arm.RET_PUSH, 2)
    servo.move(Claw.PUSH_RET, 2)
    straight_drive_distance(100, 6)
    servo.move(Claw.OPEN, 2)
    straight_drive_distance(100, 2.5)


def ret():
    servo.move(Claw.CLOSE, 2)
    msleep(200)
    servo.move(Arm.RET_LEVEL_0_25, 2)
    straight_drive_distance(-20, 2)
    servo.move(Arm.RET_LEVEL_0_5, 2)
    straight_drive_distance(-20, 1)
    servo.move(Wrist.DIAGONAL_HORIZONTAL)
    servo.move(Arm.RET_LEVEL_0_75)
    servo.move(Wrist.DIAGONAL, 2)
    servo.move(Arm.RET_LEVEL_1)

    gyro_turn(-30, -20, 3)
    servo.move(Wrist.DIAGONAL_VERTICAL, 2)
    gyro_turn(-30, -10, 4)
    servo.move(Wrist.VERTICAL, 2)
    gyro_turn(-30, -10, 4)
    servo.move(Wrist.DIAGONAL_VERTICAL, 2)
    gyro_turn(-30, -20, 3)
    servo.move(Wrist.DIAGONAL, 2)
    servo.move(Wrist.DIAGONAL_HORIZONTAL, 2)
    servo.move(Arm.RET_LEVEL_1_25, 2)
    servo.move(Wrist.HORIZONTAL, 2)
    servo.move(Arm.RET_LEVEL_1_5, 2)
    servo.move(Wrist.DIAGONAL_HORIZONTAL, 2)
    servo.move(Arm.RET_LEVEL_1_75, 2)
    servo.move(Wrist.DIAGONAL, 2)
    servo.move(Arm.RET_LEVEL_2, 2)

    servo.move(Wrist.DIAGONAL_VERTICAL, 2)
    gyro_turn(-20, -5, 12)
    servo.move(Wrist.DIAGONAL, 2)
    gyro_turn(5, 30, 5)
    servo.move(Wrist.DIAGONAL_HORIZONTAL, 2)
    servo.move(Arm.RET_LEVEL_2_25, 2)
    servo.move(Wrist.HORIZONTAL, 2)
    servo.move(Arm.RET_LEVEL_2_5, 2)
    straight_drive_distance(30, 2)
    servo.move(Wrist.DIAGONAL_HORIZONTAL, 2)
    servo.move(Arm.RET_LEVEL_2_75, 2)
    servo.move(Wrist.DIAGONAL, 2)
    servo.move(Arm.RET_LEVEL_3, 2)

    straight_drive_distance(20, 1)
    servo.move(Wrist.DIAGONAL_VERTICAL, 2)
    gyro_turn(-10, 30, 2)
    servo.move(Wrist.VERTICAL, 2)
    gyro_turn(0, 30, 10)

    servo.move(Claw.OPEN, 2)
    straight_drive_distance(-60, 8)
    servo.move(Wrist.HORIZONTAL, 2)
    servo.move(Arm.RET_LEVEL_0, 2)
