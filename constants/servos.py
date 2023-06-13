from common import ROBOT
from common.core.enums import ServoEnum
from constants.ports import *


def translate_arm(angle):
    position = int(angle / 175 * 2047 + 549)
    if position < 0 or position > 2047:
        raise Exception("Resulting position invalid " + str(position))
    return position


def translate_claw(angle):
    position = int(-angle / 175 * 2047 + 976)
    if position < 0 or position > 2047:
        raise Exception("Resulting position invalid " + str(position))
    return position


class Wrist(ServoEnum):
    port = 0

    VERTICAL = 540
    DIAGONAL_VERTICAL = 835
    DIAGONAL = 1110
    DIAGONAL_HORIZONTAL = 1385
    HORIZONTAL = 1650


class Claw(ServoEnum):
    port = 1

    CLOSE = 1300
    OPEN = 450
    SUPEROPEN = 275
    PUSH_RET = 850


class Arm(ServoEnum):
    port = 2

    # RET Values
    DOWN = 1700
    LOW_LOW_DOWN = 1569
    LOW_DOWN = 1463
    HIGH_LOW_DOWN = 1356
    LOW = 1250
    LOW_MIDDLE_LOW = 1118
    MIDDLE_LOW = 985
    HIGH_MIDDLE_LOW = 853
    MIDDLE = 720
    LOW_MIDDLE_HIGH = 578
    MIDDLE_HIGH = 435
    HIGH_MIDDLE_HIGH = 293
    HIGH = 150

    # Everything Else
    START = 1875
    HORIZONTAL = 900

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

