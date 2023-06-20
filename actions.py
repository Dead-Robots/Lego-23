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
    gyro_init(gyro_drive, stop_motors, get_motor_positions, push_sensor, 0.975, 0.08, 0.018, 0.3, 0.4)
    enable_servos()
    servo.move(Wrist.HORIZONTAL, 2)
    servo.move(Claw.SUPEROPEN, 2)
    servo.move(Arm.START, 2)


def calibrate_drive_distance():
    servo.move(Arm.RET_LEVEL_0_25, 2)
    calibrate_straight_drive_distance(ROBOT.choose(red=10.75, blue=10, yellow=10, green=11))


def test_motors():
    straight_drive_distance(80, 12)
    gyro_turn(80, 0, 90)


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

    def condition():
        return analog(LEFT_TOP_HAT) < TOP_HAT_THRESHOLD

    def condition_2():
        return analog(RIGHT_TOP_HAT) > TOP_HAT_THRESHOLD

    print("Driving until left top hat sees black.")
    straight_drive(80, condition)
    print("Driving until right top hat sees white.")
    straight_drive(80, condition_2)


def go_to_ret():
    servo.move(Arm.RET_LEVEL_0_5, 2)
    straight_drive_distance(100, 15)
    gyro_turn(100, 0, 90)
    straight_drive_distance(100, 16.9)
    gyro_turn(100, 0, 69.5)
    servo.move(Arm.RET_PUSH, 2)
    servo.move(Claw.PUSH_RET, 2)
    straight_drive_distance(100, 6)
    wait_for_button()
    straight_drive_distance(-100, 1)
    wait_for_button()
    servo.move(Arm.RET_LEVEL_0, 2)
    wait_for_button()
    servo.move(Claw.OPEN, 2)
    wait_for_button()
    straight_drive_distance(100, 2)
    wait_for_button()
    servo.move(Arm.RET_PUSH, 2)
    wait_for_button()
    straight_drive_distance(100, 1.5)
    wait_for_button()


def ret():
    # bringing coupler from ground level to level 1
    servo.move(Claw.CLOSE, 2)
    wait_for_button()
    msleep(100)
    straight_drive_distance(-50, 4)
    wait_for_button()
    servo.move(Arm.RET_LEVEL_0_5, 2)
    wait_for_button()
    straight_drive_distance(-50, 1)
    wait_for_button()
    servo.move(Wrist.DIAGONAL_HORIZONTAL)
    wait_for_button()
    servo.move(Arm.RET_LEVEL_0_75)
    wait_for_button()
    servo.move(Wrist.DIAGONAL, 2)
    wait_for_button()
    servo.move(Arm.RET_LEVEL_1)
    wait_for_button()

    # bringing coupler from level 1 to level 2
    gyro_turn(-60, -30, 4)
    wait_for_button()
    servo.move(Wrist.DIAGONAL_VERTICAL, 2)
    wait_for_button()
    gyro_turn(-60, -30, 5)
    wait_for_button()
    servo.move(Wrist.VERTICAL, 2)
    wait_for_button()
    gyro_turn(-60, -15, 5)
    wait_for_button()
    servo.move(Wrist.DIAGONAL_VERTICAL, 2)
    wait_for_button()
    gyro_turn(-60, 0, 7)
    wait_for_button()
    servo.move(Wrist.DIAGONAL, 2)
    wait_for_button()
    servo.move(Arm.RET_LEVEL_1_25, 2)
    wait_for_button()
    servo.move(Wrist.DIAGONAL_HORIZONTAL, 2)
    wait_for_button()
    servo.move(Arm.RET_LEVEL_1_75, 2)
    wait_for_button()
    servo.move(Wrist.DIAGONAL, 2)
    wait_for_button()
    servo.move(Arm.RET_LEVEL_2, 2)
    wait_for_button()

    # bringing coupler from level 2 to level 3
    servo.move(Wrist.DIAGONAL_VERTICAL, 2)
    wait_for_button()
    gyro_turn(-20, 20, 12)
    wait_for_button()
    servo.move(Wrist.DIAGONAL, 2)
    wait_for_button()
    gyro_turn(-20, 20, 5)
    wait_for_button()
    servo.move(Wrist.DIAGONAL_HORIZONTAL, 2)
    wait_for_button()
    servo.move(Arm.RET_LEVEL_2_25, 2)
    wait_for_button()
    straight_drive_distance(50, 1.5)
    wait_for_button()
    servo.move(Wrist.HORIZONTAL, 2)
    wait_for_button()
    servo.move(Arm.RET_LEVEL_2_5, 2)
    wait_for_button()
    straight_drive_distance(50, 2)
    wait_for_button()
    servo.move(Wrist.DIAGONAL_HORIZONTAL, 2)
    wait_for_button()
    servo.move(Arm.RET_LEVEL_2_75, 2)
    wait_for_button()
    servo.move(Wrist.DIAGONAL, 2)
    wait_for_button()
    servo.move(Arm.RET_LEVEL_3, 2)
    wait_for_button()

    # getting the coupler in a good position
    straight_drive_distance(50, 1)
    wait_for_button()
    servo.move(Wrist.DIAGONAL_VERTICAL, 2)
    wait_for_button()
    gyro_turn(-5, 60, 2)
    wait_for_button()
    servo.move(Wrist.VERTICAL, 2)
    wait_for_button()
    gyro_turn(0, 60, 10)
    wait_for_button()

    # opening claw in the good position
    servo.move(Claw.OPEN, 2)
    straight_drive_distance(-80, 8)
    servo.move(Wrist.HORIZONTAL, 2)
    servo.move(Arm.START, 2)
