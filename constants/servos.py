from common import ROBOT
from common.core.enums import ServoEnum
from constants.ports import *


#  Red and Blue have tested values
class Claw(ServoEnum):
    port = CLAW

    OPEN = ROBOT.choose(
        red=000,
        blue=430,
        yellow=950
    )

    CLOSED = ROBOT.choose(
        red=880,
        blue=1430,
        yellow=1950
    )

    GRAB = ROBOT.choose(
        red=900,
        blue=1470,
        yellow=2047
    )

    RED_NOODLE_GRAB_1 = ROBOT.choose(
        red=800,
        blue=1330,
        yellow=1900
    )

    RED_NOODLE_GRAB_2 = ROBOT.choose(
        red=900,
        blue=1360,
        yellow=1900
    )

    GREEN_NOODLE_GRAB = ROBOT.choose(
        red=840,
        blue=1270,
        yellow=1950
    )

    NOODLE_OPEN = ROBOT.choose(
        red=450,
        blue=880,
        yellow=1550
    )


# Red and Blue have tested values
class Arm(ServoEnum):
    port = ARM

    DOWN = ROBOT.choose(
        red=1775,
        blue=2700,
        yellow=1325
    )

    GRAB = ROBOT.choose(
        red=720,
        blue=1100,
        yellow=370
    )

    STRAIGHT = ROBOT.choose(
        red=600,
        blue=970,
        yellow=250
    )

    START = ROBOT.choose(
        red=600,
        blue=1010,
        yellow=250
    )

    UP = ROBOT.choose(
        red=335,
        blue=680,
        yellow=0
    )

    RED_NOODLE_GRAB_1 = ROBOT.choose(
        red=1370,
        blue=1730,
        yellow=1020
    )

    RED_NOODLE_GRAB_2 = ROBOT.choose(
        red=1420,
        blue=1775,
        yellow=1070
    )

    GREEN_NOODLE_GRAB = ROBOT.choose(
        red=1310,
        blue=1720,
        yellow=960
    )

    RING = ROBOT.choose(
        red=1530,
        blue=1900,
        yellow=1075
    )


# Red and Blue have tested values
class BackClaw(ServoEnum):
    port = BACK_CLAW

    UP = ROBOT.choose(
        red=0,
        blue=650,
        yellow=750
    )

    DOWN = ROBOT.choose(
        red=1000,
        blue=1400,
        yellow=1500
    )

    SUPERDOWN = ROBOT.choose(
        red=1250,
        blue=1700,
        yellow=1800
    )
