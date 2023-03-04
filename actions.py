import time
from kipr import msleep, enable_servos, set_servo_position, analog, freeze, \
    get_servo_position, disable_servos, disable_servo, \
    enable_servo
from drive import drive, stop_motors, line_follow, line_follow_left
from utilities import wait_for_button
from constants.ports import TOP_HAT, LEFT_MOTOR, RIGHT_MOTOR
from constants.servos import BackClaw, Claw, Arm


def init():
    enable_servos()
    disable_servo(BackClaw.port)
    power_on_self_test()
    move_servo_lego(Claw.OPEN, 0)
    move_servo_lego(Arm.STRAIGHT)
    move_servo_lego(BackClaw.UP)
    wait_for_button()


def power_on_self_test():
    while analog(TOP_HAT) < 1800:
        drive(95, 100, 10)
    stop_motors()
    drive(93, 0, 1450)
    stop_motors()
    move_servo_lego(Claw.OPEN, 1)
    move_servo_lego(Claw.CLOSED, 1)
    move_servo_lego(Arm.STRAIGHT)
    move_servo_lego(Arm.UP)
    move_servo_lego(Arm.DOWN)
    move_servo_lego(Arm.UP)
    move_servo_lego(BackClaw.DOWN)
    move_servo_lego(BackClaw.UP)
    stop_motors()


def shut_down():
    disable_servos()
    stop_motors()


def get_botgal():
    move_servo_lego(Claw.OPEN, 0)
    drive(100, 100, 1050)                 # move tophat out of start box while lining up for line follow
    line_follow(2200)  # go to botgal
    stop_motors()
    drive(-100, 0, 150)
    drive(-95, -100, 150)
    stop_motors()
    move_servo_lego(Arm.GRAB)
    # drive(93, 100, 500)                  # square up with pvc
    # stop_motors()
    # wait_for_button()
    move_servo_lego(Claw.CLOSED, 2)
    move_servo_lego(Arm.UP)


def deliver_botgal():
    drive(-95, -100, 1600)
    drive(-100, 100, 1150)
    drive(95, 100, 750)
    stop_motors()
    move_servo_lego(Arm.DOWN)
    move_servo_lego(Claw.OPEN)
    move_servo_lego(Arm.STRAIGHT)


def wire_shark():
    drive(-30, 100, 1700)
    while analog(TOP_HAT) < 1700:
        drive(0, 100, 10)
    line_follow_left(2500)
    stop_motors()
    drive(100, -100, 1000)
    while analog(TOP_HAT) < 1700:
        drive(20, -20, 10)
    while analog(TOP_HAT) > 200:
        drive(-20, 20, 25)
    drive(-20, 20, 850)
    stop_motors()
    drive(-85, -85, 250)
    move_servo_lego(BackClaw.DOWN)
    drive(50, 50, 150)
    move_servo_lego(BackClaw.DOWN)
    drive(85, 85, 1000)
    drive(-85, -85, 500)
    move_servo_lego(BackClaw.DOWN)


def wireshark_to_ddos():
    drive(100, 100, 50)
    move_servo_lego(BackClaw.DOWN)
    line_follow_left(7000)
    drive(85, -85, 1285)
    while analog(TOP_HAT) < 1700:
        drive(20, -20, 25)
    drive(-20, 20, 2200)
    drive(-85, -85, 885)


def go_to_ws():
    drive(-85, 85, 950)
    line_follow_left(2000)
    drive(1000, 100, 95)
    line_follow_left(3500)
    freeze(LEFT_MOTOR)
    freeze(RIGHT_MOTOR)
    msleep(1000)
    while analog(TOP_HAT) < 3400:
        drive(-85, 85, 5)
    while analog(TOP_HAT) > 2050:
        drive(-85, 85, 5)
    freeze(LEFT_MOTOR)
    freeze(RIGHT_MOTOR)
    wait_for_button()
    drive(750, -100, -100)


def line_follow_right_lego1(duration, direction=1):
    duration = duration // 1000

    start_time = time.time()

    while time.time() - start_time < duration:
        if analog(TOP_HAT) > 3100:
            drive(0, *([direction * 90, direction * 20][::direction]))
        elif analog(TOP_HAT) < 2600:
            drive(0, *([direction * 40, direction * 90][::direction]))
        else:
            drive(0, direction * 85, direction * 85)


def move_servo_lego(new_position, step_time=10):
    servo = new_position.port
    temp = get_servo_position(servo)
    if servo == BackClaw.port:
        enable_servo(BackClaw.port)

    if temp < new_position:
        while temp < new_position:
            set_servo_position(servo, temp)
            temp += 5
            msleep(step_time)
    else:
        while temp > new_position:
            set_servo_position(servo, temp)
            temp -= 5
            msleep(step_time)

    if servo == BackClaw.port:
        disable_servo(BackClaw.port)
