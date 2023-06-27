from common import ROBOT
from common.core.enums import ServoEnum
from constants.ports import *


def translate_arm(angle):
    position = int(angle / 175 * 2047 + int(ROBOT.choose(red=-213, yellow=-165, blue=-165, green=-213)))
    if position < 0 or position > 2047:
        raise Exception("Resulting position invalid " + str(position) + " " + str(angle))
    return position


def translate_claw(angle):
    position = int(angle / 175 * 2047 + ROBOT.choose(red=287, blue=287, yellow=287, green=830))
    if position < 0 or position > 2047:
        raise Exception("Resulting position invalid " + str(position) + " " + str(angle))
    return position


def translate_wrist(angle):
    position = int(-angle / 175 * 2047 + int(ROBOT.choose(red=1650, blue=1650, yellow=1650, green=1720)))
    if position < 0 or position > 2047:
        raise Exception("Resulting position invalid " + str(position) + " " + str(angle))
    return position


class Wrist(ServoEnum):
    port = WRIST
    translation_function = translate_wrist

    VERTICAL = translate_wrist(95)
    DIAGONAL_VERTICAL = translate_wrist(70)
    DIAGONAL = translate_wrist(46)
    DIAGONAL_HORIZONTAL = translate_wrist(23)
    HORIZONTAL = translate_wrist(0)
    DROP = translate_wrist(140)


class Claw(ServoEnum):
    port = CLAW
    translation_function = translate_claw

    CLOSE = translate_claw(90)
    OPEN = translate_claw(14)
    SUPEROPEN = translate_claw(0)
    PUSH_RET = translate_claw(48)
    FIREWALL = translate_claw(56.5)


class Arm(ServoEnum):
    port = ARM
    translation_function = translate_arm

    # RET Values (ugly)
    RET_DOWN = translate_arm(170)
    RET_LEVEL_0 = translate_arm(165)
    RET_LEVEL_0_25 = translate_arm(145)
    RET_LEVEL_0_5 = translate_arm(135)
    RET_LEVEL_0_75 = translate_arm(125)
    RET_LEVEL_1 = translate_arm(118)
    RET_LEVEL_1_25 = translate_arm(108)
    RET_LEVEL_1_5 = translate_arm(95)
    RET_LEVEL_1_75 = translate_arm(85)
    RET_LEVEL_2 = translate_arm(74)
    RET_LEVEL_2_25 = translate_arm(54)
    RET_LEVEL_2_5 = translate_arm(41)
    RET_LEVEL_2_75 = translate_arm(29)
    RET_LEVEL_3 = translate_arm(20)

    # Everything Else
    START = translate_arm(20)
    HORIZONTAL = translate_arm(90)
    GRAB_FIREWALL = translate_arm(160)
    LIFT_FIREWALL = translate_arm(20)
    LIFT_FIREWALL_SLIGHTLY = translate_arm(155)
    BELOW_ALARM = translate_arm(136)
    ALARM_SQUARE_UP = translate_arm(106.5)
    ABOVE_ALARM = translate_arm(35)
    DOWN = translate_arm(185)
    NOODLE_GRAB = translate_arm(75)
    NOODLE_LIFT = translate_arm(20)
    NOODLE_DELIVERY = translate_arm(96)

# class OldArm(ServoEnum):
#     port = ARM
#
#     VERTICAL = translate_arm(0)
#     HORIZONTAL = translate_arm(90)
#     FORTY_FIVE = translate_arm(45)
#     ONE_TEN = translate_arm(110)
#     SEVENTY = translate_arm(70)
#     SEVENTY_FIVE = translate_arm(75)
#     EIGHTY = translate_arm(80)
#     SIXTY_FIVE = translate_arm(65)
#     TWENTY_FIVE = translate_arm(25)
#     THIRTY = translate_arm(30)
#     THIRTY_FIVE = translate_arm(35)
#
#
# # Red and Blue have tested values
# class BackClaw(ServoEnum):
#     port = BACK_CLAW
#
#     UP = ROBOT.choose(
#         red=0,
#         blue=400,
#         yellow=750
#     )
#
#     DOWN = ROBOT.choose(
#         red=1230,
#         blue=1400,
#         yellow=1500
#     )
#
#     SUPERDOWN = ROBOT.choose(
#         red=1250,
#         blue=1400,
#         yellow=1800
#     )
