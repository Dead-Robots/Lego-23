from kipr import msleep, enable_servos, set_servo_position, analog, disable_servos, enable_servo
from kipr import motor_power, shut_down_in, wait_for_light
from calibrate import choose_to_calibrate
from constants.sensors import TOP_HAT_THRESHOLD, calibrate_gyro
from drive import drive, line_follow, line_follow_left, drive_straight, \
    dramatic_line_follow, line_follow_right, line_follow_ticks, drive_until_black, drive_until_white, gyro_drive, \
    line_follow_to_line, drive_straight_until_white, drive_straight_until_black
from servo import move_servo_lego
from utilities import wait_for_button, stop_motors, debug
from constants.ports import LEFT_TOP_HAT, SERVO_REPLACEMENT, RIGHT_TOP_HAT
from constants.servos import BackClaw, Claw, Arm, LIGHT_SENSOR
from common import ROBOT, light
from common.gyro_movements import gyro_init, gyro_turn


def init():
    ROBOT.run(
        gyro_init,
        red=(gyro_drive, stop_motors, 0, 1, 0.013, 0.005),
        blue=(gyro_drive, stop_motors, 0.05, 1),
        yellow=(gyro_drive, stop_motors, 0, 1),
        green=(gyro_drive, stop_motors, 0, 1, 0.013, 0.005)
    )
    # choose_to_calibrate()
    # wait_for_button("Press button for POST.")
    # enable_servos()
    # power_on_self_test()
    # move_servo_lego(BackClaw.UP)
    # move_servo_lego(Claw.CLOSED, 0, False)
    # move_servo_lego(Arm.START, 5, False)
    # wait_for_button("Press button to calibrate light sensor.")
    # light.wait_4_light(LIGHT_SENSOR)
    # # wait_for_light(LIGHT_SENSOR)
    # shut_down_in(119)


def power_on_self_test():
    set_servo_position(BackClaw.port, BackClaw.UP)
    drive_straight(0)
    while analog(LEFT_TOP_HAT) < TOP_HAT_THRESHOLD:
        pass
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
    drive_straight(0, -1)
    while analog(RIGHT_TOP_HAT) < TOP_HAT_THRESHOLD:
        pass
    stop_motors()


def shut_down():
    disable_servos()
    stop_motors()
    print("end")


def get_botgal():
    # moves from starting position
    move_servo_lego(Claw.OPEN, 2, False)
    # goes to botgal
    line_follow(ROBOT.choose(red=3000, blue=2550, yellow=2750))
    drive_straight(ROBOT.choose(red=530, blue=620, yellow=420))
    # backs up to prepare for grab
    drive_straight(ROBOT.choose(red=100, blue=100, yellow=200), -1)
    # grabs and lifts botgal
    move_servo_lego(Arm.GRAB, 4)
    move_servo_lego(Claw.GRAB, 2, False)
    move_servo_lego(Arm.UP, 20, False)


# bad robots :(
def deliver_botgal():
    # backs up to make space for turn
    drive_straight(ROBOT.choose(red=600, blue=600, yellow=600), -1)
    # turns left past black linedrive_straight_until_white
    gyro_turn(0, 100, ROBOT.choose(red=40, blue=40, yellow=40))
    # turns left to next black line
    drive_until_black(-85, 85, False)
    # line follows to botgal delivery zone
    line_follow_right(ROBOT.choose(red=1150, blue=850, yellow=1000))
    # lowers arm early to avoid hitting green pool noodles
    move_servo_lego(Arm.DOWN, 4)
    # positions botgal for final delivery
    drive_straight_until_white()
    drive_until_black(5, 85, False)
    gyro_turn(80, 0, 14)
    # releases botgal
    move_servo_lego(Claw.OPEN, 2)
    # backs away from botgal to make room for lifting arm
    drive_straight(ROBOT.choose(red=350, blue=350, yellow=350), -1)
    # lifts arm and closes claw to help get out of Create's path
    move_servo_lego(Arm.STRAIGHT, 4)
    move_servo_lego(Arm.UP, 5, False)
    move_servo_lego(Claw.CLOSED, 0, False)


def get_wire_shark():
    drive_until_black(0, 100, False)
    # turns past black line
    gyro_turn(0, 100, ROBOT.choose(red=80, blue=35, yellow=70))
    # turns until next black line to prepare for line follow
    drive_until_black(0, 100, False)
    # line follows to wireshark
    line_follow_to_line(False)
    line_follow_ticks(ROBOT.choose(red=5750, blue=5000, yellow=5700), False)
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
    drive_straight(ROBOT.choose(red=2900, blue=2700, yellow=2400), -0.5)
    drive_straight(ROBOT.choose(red=0, blue=20, yellow=0))
    # sets the backclaw to down prior to enabling it to prevent it from jumping upwards
    stop_motors(0)
    set_servo_position(BackClaw.port, BackClaw.DOWN)
    enable_servo(BackClaw.port)
    # grabs wireshark
    msleep(1300)


def ws_to_ddos():
    # begins moving to ddos with wireshark
    drive_straight(ROBOT.choose(red=400, blue=400, yellow=400))
    # moves backclaw farther down to more securely grab wireshark
    drive_straight(ROBOT.choose(red=150, blue=150, yellow=150), -1)
    move_servo_lego(BackClaw.SUPERDOWN, 1)
    enable_servo(BackClaw.port)
    drive_straight(ROBOT.choose(red=150, blue=150, yellow=150), -1)
    # line follow to ddos
    line_follow_ticks(ROBOT.choose(red=14350, blue=14100, yellow=14350))
    # turns left past black line
    drive(-85, 85, ROBOT.choose(red=1450, blue=1450, yellow=1450))
    # turns until next black line
    drive_until_black(-80, 80, False)
    # turns until the end of the black line
    drive_until_white(-40, 40, False)
    # turns left to line up with ddos
    drive(-65, 65, ROBOT.choose(red=155, blue=135, yellow=100))
    # backs up to position wireshark under ddos
    drive_straight(ROBOT.choose(red=850, blue=800, yellow=830), -1)
    stop_motors()


def ddos_to_analysis():
    # shakes to disperse ping-pongs in wireshark
    drive(65, 65, ROBOT.choose(red=200, blue=100, yellow=100))
    msleep(50)
    drive(-65, -65, ROBOT.choose(red=200, blue=100, yellow=100))
    msleep(50)
    drive(-65, 65, ROBOT.choose(red=200, blue=200, yellow=100))
    msleep(50)
    drive(65, -65, ROBOT.choose(red=200, blue=200, yellow=100))
    msleep(50)
    drive(-65, 65, ROBOT.choose(red=200, blue=200, yellow=100))
    msleep(50)
    drive(65, -65, ROBOT.choose(red=200, blue=200, yellow=100))
    msleep(50)
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
    drive_straight(ROBOT.choose(red=900, blue=800, yellow=900))
    # turns right to prepare to knock over rings
    drive(-80, 80, ROBOT.choose(red=1650, blue=1450, yellow=1650))
    # lowers the arm to prepare to knock over rings
    move_servo_lego(Arm.RING, 4)
    # turns quickly to knock over rings
    drive(-100, 100, ROBOT.choose(red=500, blue=500, yellow=450))
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
    line_follow_left(ROBOT.choose(red=500, blue=350, yellow=500))
    # turns left to face the noodle
    drive_until_white(-80, 80, False)
    gyro_turn(-80, 80, ROBOT.choose(red=88, blue=89, yellow=87))
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
    gyro_turn(-100, 100, ROBOT.choose(red=145, blue=155, yellow=145))
    drive_straight(ROBOT.choose(red=600, blue=600, yellow=600), -1)
    # lowers the arm and drops the noodle into analysis lab
    move_servo_lego(Arm.DOWN, 3)
    move_servo_lego(Claw.NOODLE_OPEN, 1, False)
    move_servo_lego(Arm.STRAIGHT, 3, False)


def yellow_get_noodle_one():
    # waits for Create
    msleep(ROBOT.choose(red=13000, blue=13000, yellow=13000))
    # moves arm up so it does not run into anything
    move_servo_lego(Arm.STRAIGHT, 4, False)
    # turns left past the black line
    drive_until_black(-60, 60, False)
    drive_until_white(-60, 60, False)
    # line follows to line up with the noodle
    line_follow_left(ROBOT.choose(red=700, blue=350, yellow=150))
    # turns left to face the noodle
    drive_until_white(-80, 80, False)
    gyro_turn(-80, 80, ROBOT.choose(red=90, blue=90, yellow=90))
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
    gyro_turn(100, -100, ROBOT.choose(red=75, blue=65, yellow=65))
    drive_straight(ROBOT.choose(red=2500, blue=2500, yellow=2500))
    stop_motors()


def clap_claw():
    move_servo_lego(Claw.CLOSED, 1, False)
    move_servo_lego(Claw.OPEN, 1, False)
    move_servo_lego(Claw.CLOSED, 1, False)
    move_servo_lego(Claw.OPEN, 1, False)
    move_servo_lego(Claw.CLOSED, 1, False)
    move_servo_lego(Claw.OPEN, 1, False)
    move_servo_lego(Claw.CLOSED, 1, False)
