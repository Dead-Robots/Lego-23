#!/usr/local/bin/python3.10 -u

from kipr import motor_power, msleep, enable_servos, set_servo_position
RIGHT_MOTOR = 0
LEFT_MOTOR = 3
ARM_SERVO = 0
CLAW_SERVO = 1
TOP_HAT = 0


def print_hi(name):

    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    enable_servos()
    set_servo_position(ARM_SERVO, 200)
    set_servo_position(CLAW_SERVO, 500)
    motor_power(RIGHT_MOTOR, 75)
    motor_power(LEFT_MOTOR,75)
    msleep(2500)
    motor_power(RIGHT_MOTOR,0)
    motor_power(LEFT_MOTOR,0)
    set_servo_position(CLAW_SERVO, )

    motor_power(RIGHT_MOTOR, 99)
    motor_power(LEFT_MOTOR, 100)
    msleep(6200)
    motor_power(RIGHT_MOTOR, 0)
    motor_power(LEFT_MOTOR, 0)
    motor_power(RIGHT_MOTOR, 100)
    motor_power(LEFT_MOTOR, 0)
    msleep(1500)
    motor_power(RIGHT_MOTOR, 0)
    motor_power(LEFT_MOTOR, 0)
    #90 degree turn
    motor_power(RIGHT_MOTOR, 100)
    motor_power(LEFT_MOTOR, 100)
    msleep(1000)
    motor_power(RIGHT_MOTOR, 0)
    motor_power(LEFT_MOTOR, 0)
    motor_power(RIGHT_MOTOR, 100)
    motor_power(LEFT_MOTOR, 0)
    msleep(1800)
    motor_power(RIGHT_MOTOR, 0)
    motor_power(LEFT_MOTOR, 0)
    motor_power(LEFT_MOTOR,100)
    motor_power(RIGHT_MOTOR,100)
    msleep(2500)
    motor_power(RIGHT_MOTOR,0)
    motor_power(LEFT_MOTOR,0)

    #motor_power(RIGHT_MOTOR, 75)
    #motor_power(LEFT_MOTOR, 100)
    #msleep(2700)
    #motor_power(RIGHT_MOTOR, 0)
    #motor_power(LEFT_MOTOR, 0)
