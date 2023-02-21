#!/usr/local/bin/python3.10 -u

from kipr import motor_power, msleep, enable_servos, set_servo_position, analog, push_button, freeze, clear_motor_position_counter, get_motor_position_counter
RIGHT_MOTOR = 0
LEFT_MOTOR = 3
ARM_SERVO = 1
CLAW_SERVO = 0
TOP_HAT = 0
CLAW_OPEN = 350
CLAW_CLOSE = 1000


def drive(left_speed, right_speed, time):
    motor_power(LEFT_MOTOR, left_speed)
    motor_power(RIGHT_MOTOR, right_speed)
    msleep(time)


def line_follow(time):
    x = 0
    while x < time:
        if analog(TOP_HAT) < 1800:  # on white
            x += 10
            drive(80, 100, 10)
        else:                       # on black
            x += 10
            drive(100, 85, 10)


def stop_motors():
    freeze(LEFT_MOTOR)
    freeze(RIGHT_MOTOR)
    msleep(200)


def wait_for_button():
    stop_motors()
    print("push the button")
    while not push_button():
        pass
    msleep(1000)


def get_botgal():
    drive(70, 100, 1000)                 # move tophat out of start box while lining up for line follow
    drive(100, 80, 1000)
    line_follow(1600)                    # go to botgal
    drive(93, 100, 500)                  # square up with pvc
    stop_motors()
    set_servo_position(CLAW_SERVO, CLAW_CLOSE)


def deliver_botgal():
    drive(-100, -100, 800)
    drive(0, 100, 1050)                 # cross bump perpendicularly
    drive(100, 100, 900)
    wait_for_button()
    drive(0, 100, 1050)
    wait_for_button()
    drive(100, 100, 3000)


def start():
    enable_servos()
    set_servo_position(CLAW_SERVO, CLAW_OPEN)


if __name__ == '__main__':
    start()
    wait_for_button()
    get_botgal()
    deliver_botgal()
