import time
from kipr import msleep, enable_servos, set_servo_position, analog, disable_servos, enable_servo

from calibrate import choose_to_calibrate
from constants.sensors import TOP_HAT_THRESHOLD, calibrate_gyro
from drive import drive, line_follow, line_follow_left, drive_straight, line_follow_right_lego1, \
    dramatic_line_follow, line_follow_right, line_follow_ticks, drive_until_black, drive_until_white, gyro_turn
from servo import move_servo_lego
from utilities import wait_for_button, stop_motors, debug
from constants.ports import TOP_HAT, SERVO_REPLACEMENT
from constants.servos import BackClaw, Claw, Arm
from common import ROBOT
from kipr import motor_power


def init():
    print("Calibrating gyro, do not touch.")
    msleep(500)
    calibrate_gyro()
    msleep(500)
    choose_to_calibrate()
    enable_servos()
    power_on_self_test()
    move_servo_lego(BackClaw.UP)
    move_servo_lego(Claw.CLOSED, 0, False)
    move_servo_lego(Arm.UP, False)
    wait_for_button("push button to start")


def power_on_self_test():
    set_servo_position(BackClaw.port, BackClaw.UP)
    while analog(TOP_HAT) < TOP_HAT_THRESHOLD:
        drive_straight(10)
    stop_motors()
    msleep(800)
    drive_straight(500)
    gyro_turn(100, 0, 40)
    move_servo_lego(Claw.OPEN, 0)
    move_servo_lego(Arm.STRAIGHT, 4, False)
    move_servo_lego(Arm.UP, 5, False)
    move_servo_lego(Arm.DOWN, 4, False)
    move_servo_lego(Arm.STRAIGHT, 4, False)
    move_servo_lego(Arm.UP, 5, False)
    move_servo_lego(Claw.GRAB, 0, False)
    move_servo_lego(BackClaw.SUPERDOWN, 4, False)
    move_servo_lego(BackClaw.DOWN, 4, False)
    msleep(800)
    move_servo_lego(BackClaw.UP, 4, False)


def shut_down():
    disable_servos()
    stop_motors()
    print("end")


def get_botgal():
    # moves claw and arm from start position
    move_servo_lego(Claw.OPEN, 0, False)
    move_servo_lego(Arm.STRAIGHT, 8, False)
    # goes to botgal
    line_follow(ROBOT.choose(red=2850, blue=2750, yellow=2750))
    drive_straight(ROBOT.choose(red=320, blue=420, yellow=420))
    # backs up to prepare for grab
    drive_straight(ROBOT.choose(red=200, blue=100, yellow=200), -1)
    # grabs and lifts botgal
    move_servo_lego(Arm.GRAB, 4)
    move_servo_lego(Claw.GRAB, 2, False)
    move_servo_lego(Arm.UP, 20, False)


def deliver_botgal():
    # backs up to make space for turn
    drive_straight(ROBOT.choose(red=600, blue=600, yellow=600), -1)
    # turns left past black line
    drive(0, 100, ROBOT.choose(red=2000, blue=2000, yellow=2000))
    # turns left to next black line
    drive_until_black(-85, 85, False)
    # line follows to botgal delivery zone
    line_follow_right(ROBOT.choose(red=1000, blue=900, yellow=1000))
    # lowers arm early to avoid hitting green pool noodles
    move_servo_lego(Arm.DOWN, 4)
    # drives straight to get botgal in line with the delivery zone
    drive_straight(ROBOT.choose(red=470, blue=570, yellow=470))
    # arcs right to move botgal away from black line
    drive_until_white(100, 30, False)
    gyro_turn(100, 30, 6)
    # releases botgal
    move_servo_lego(Claw.OPEN, 2)
    # backs away from botgal to make room for lifting arm
    drive_straight(ROBOT.choose(red=350, blue=350, yellow=350), -1)
    # lifts arm and closes claw to help get out of Create's path
    move_servo_lego(Arm.STRAIGHT, 4)
    move_servo_lego(Arm.UP, 5, False)
    move_servo_lego(Claw.CLOSED, 0, False)


def get_wire_shark():
    # turns past black line
    gyro_turn(0, 100, 70)
    # turns until next black line to prepare for line follow
    drive_until_black(0, 100, False)
    # line follows to wireshark
    dramatic_line_follow(ROBOT.choose(red=3300, blue=3200, yellow=3500))
    # lowers the backclaw to sweep the poms out of the way
    move_servo_lego(BackClaw.SUPERDOWN, 1)
    # turns right past black line
    drive(100, -100, ROBOT.choose(red=800, blue=800, yellow=1000))
    # turns until next black line
    drive_until_black(80, -80, False)
    # turns back until white
    drive_until_white(-30, 30, False)
    # turns left slightly to line up correctly with wireshark
    drive(-65, 65, ROBOT.choose(red=160, blue=140, yellow=130))
    # lifts backclaw again to prepare to get wireshark
    move_servo_lego(BackClaw.UP, 2)
    # backs up to wireshark
    drive_straight(ROBOT.choose(red=2800, blue=2700, yellow=2400), -0.5)
    drive_straight(ROBOT.choose(red=10, blue=20, yellow=0))
    # sets the backclaw to down prior to enabling it to prevent it from jumping upwards
    stop_motors(0)
    set_servo_position(BackClaw.port, BackClaw.DOWN)
    enable_servo(BackClaw.port)
    # grabs wireshark
    msleep(300)


def ws_to_ddos():
    # begins moving to ddos with wireshark
    drive_straight(ROBOT.choose(red=400, blue=400, yellow=400))
    # moves backclaw farther down to more securely grab wireshark
    drive_straight(ROBOT.choose(red=100, blue=150, yellow=100), -1)
    move_servo_lego(BackClaw.SUPERDOWN, 1)
    enable_servo(BackClaw.port)
    drive_straight(ROBOT.choose(red=100, blue=150, yellow=100), -1)
    # line follow to ddos
    line_follow_ticks(ROBOT.choose(red=14350, blue=10750, yellow=14350))
    # turns left past black line
    drive(-85, 85, ROBOT.choose(red=1450, blue=1450, yellow=1450))
    # turns until next black line
    drive_until_black(-80, 80, False)
    # turns until the end of the black line
    drive_until_white(-40, 40, False)
    # turns left to line up with ddos
    drive(-65, 65, ROBOT.choose(red=160, blue=160, yellow=100))
    # backs up to position wireshark under ddos
    drive_straight(ROBOT.choose(red=850, blue=800, yellow=830), -1)
    stop_motors()


def ddos_to_analysis():
    # line follows to line up with delivery zone
    dramatic_line_follow(ROBOT.choose(red=1500, blue=1450, yellow=1500))
    # turns left to line up with delivery zone
    drive(0, 85, ROBOT.choose(red=1500, blue=1500, yellow=1500))
    # backs up to put wireshark in delivery zone
    drive_straight(ROBOT.choose(red=850, blue=850, yellow=750), -1)
    # releases wireshark
    move_servo_lego(BackClaw.UP, 4)


def knock_over_rings():
    # moves away from rings to space the claw correctly
    drive_straight(ROBOT.choose(red=800, blue=800, yellow=900))
    # turns right to prepare to knock over rings
    drive(-80, 80, ROBOT.choose(red=1650, blue=1450, yellow=1650))
    # lowers the arm to prepare to knock over rings
    move_servo_lego(Arm.RING, 4)
    # turns quickly to knock over rings
    drive(-100, 100, ROBOT.choose(red=450, blue=500, yellow=450))
    stop_motors()


def get_noodle_one():
    # waits for Create
    msleep(13000)
    # moves arm up so it does not run into anything
    move_servo_lego(Arm.STRAIGHT, 4, False)
    # turns left past the black line
    drive_until_black(-60, 60, False)
    drive_until_white(-60, 60, False)
    # line follows to line up with the noodle
    line_follow_left(ROBOT.choose(red=700, blue=350, yellow=500))
    # turns left to face the noodle
    drive_until_white(-80, 80, False)
    gyro_turn(-80, 80, 87)
    # drives forward so the noodle is within reach
    drive_straight(ROBOT.choose(red=700, blue=650, yellow=750))
    # initially grabs the noodle
    move_servo_lego(Claw.NOODLE_OPEN, 2)
    move_servo_lego(Arm.RED_NOODLE_GRAB_1, 4, False)
    move_servo_lego(Claw.RED_NOODLE_GRAB_1, 2, False)
    # pulls the server partway from the server rack
    drive_straight(ROBOT.choose(red=400, blue=400, yellow=400), -1)
    # releases the claw
    move_servo_lego(Claw.NOODLE_OPEN, 2)
    # moves the arm and drives forward to more securely grab the noodle
    move_servo_lego(Arm.RED_NOODLE_GRAB_2, 4, False)
    drive_straight(ROBOT.choose(red=400, blue=300, yellow=200))
    # grabs the noodle
    move_servo_lego(Claw.RED_NOODLE_GRAB_2, 2)


def deliver_noodle_one():
    # removes the noodle from the server rack
    drive_straight(ROBOT.choose(red=1200, blue=1050, yellow=800), -1)
    # lifts the arm
    move_servo_lego(Arm.STRAIGHT, 4)
    # drives away from analysis lab to avoid hitting the cubes while turning
    drive_straight(ROBOT.choose(red=800, blue=1200, yellow=800), 1)
    # turns around to score the noodle
    drive(-80, 80, ROBOT.choose(red=1200, blue=1570, yellow=1500))
    # lowers the arm and drops the noodle into analysis lab
    move_servo_lego(Arm.RED_NOODLE_GRAB_2, 4)
    move_servo_lego(Claw.OPEN, 2, False)
    move_servo_lego(Arm.STRAIGHT, 4, False)


def yellow_get_noodle_one():
    # waits for Create
    msleep(13000)
    # moves arm up so it does not run into anything
    move_servo_lego(Arm.STRAIGHT, 4, False)
    # turns left past the black line
    drive_until_black(-60, 60, False)
    drive_until_white(-60, 60, False)
    # line follows to line up with the noodle
    line_follow_left(ROBOT.choose(red=700, blue=350, yellow=150))
    # turns left to face the noodle
    drive_until_white(-80, 80, False)
    gyro_turn(-80, 80, 90)
    # drives forward so the noodle is within reach
    wait_for_button()
    drive_straight(ROBOT.choose(red=1800, blue=1800, yellow=1850))
    wait_for_button()
    stop_motors(0)
    motor_power(SERVO_REPLACEMENT, 100)
    msleep(250)
    motor_power(SERVO_REPLACEMENT, 30)


def yellow_deliver_noodle_one():
    # removes the noodle from the server rack
    drive_straight(ROBOT.choose(red=1200, blue=1050, yellow=1500), -1)
    # turns around to score the noodle
    drive(-80, 80, ROBOT.choose(red=1200, blue=1570, yellow=1550))
    drive_straight(ROBOT.choose(red=500, blue=500, yellow=500))
    stop_motors(0)
    motor_power(SERVO_REPLACEMENT, -100)
    msleep(200)
    stop_motors()



def avoid_create():
    gyro_turn(80, -80, 90)
    drive_straight(ROBOT.choose(red=1500, blue=1500, yellow=1500))
    stop_motors(0)
    move_servo_lego(Claw.CLOSED, 2, False)
    move_servo_lego(Claw.OPEN, 2, False)
    move_servo_lego(Claw.CLOSED, 2, False)
    move_servo_lego(Claw.OPEN, 2, False)
    move_servo_lego(Claw.CLOSED, 2, False)
    move_servo_lego(Claw.CLOSED, 2, False)
    move_servo_lego(Claw.OPEN, 2, False)
    move_servo_lego(Claw.CLOSED, 2, False)
    move_servo_lego(Claw.OPEN, 2, False)
    move_servo_lego(Claw.CLOSED, 2, False)

