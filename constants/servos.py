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


class Claw(ServoEnum):
    port = CLAW

    FORTY_FIVE = translate_claw(45)
    ZERO = translate_claw(0)


class Arm(ServoEnum):
    port = ARM

    ZERO = translate_arm(0)
    NINETY = translate_arm(90)
    FORTY_FIVE = translate_arm(45)
    ONE_TEN = translate_arm(110)
    SEVENTY = translate_arm(70)
    SEVENTY_FIVE = translate_arm(75)
    EIGHTY = translate_arm(80)
    SIXTY_FIVE = translate_arm(65)
    TWENTY_FIVE = translate_arm(25)
    THIRTY = translate_arm(30)
    THIRTY_FIVE = translate_arm(35)



# Red and Blue have tested values
class BackClaw(ServoEnum):
    port = BACK_CLAW

    UP = ROBOT.choose(
        red=0,
        blue=400,
        yellow=750
    )

    DOWN = ROBOT.choose(
        red=1230,
        blue=1400,
        yellow=1500
    )

    SUPERDOWN = ROBOT.choose(
        red=1250,
        blue=1400,
        yellow=1800
    )
