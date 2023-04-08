from common import ROBOT
from common.core.enums import ServoEnum
from constants.ports import *


#  Red and Blue have tested values
class Claw(ServoEnum):
    port = CLAW

    OPEN = ROBOT.choose(
        red=000,
        blue=430,
        yellow=000
    )

    CLOSED = ROBOT.choose(
        red=850,
        blue=1330,
        yellow=850
    )

    GRAB = ROBOT.choose(
        red=950,
        blue=1430,
        yellow=950
    )

    RED_NOODLE_GRAB_1 = ROBOT.choose(
        red=800,
        blue=1230,
        yellow=800
    )

    RED_NOODLE_GRAB_2 = ROBOT.choose(
        red=900,
        blue=1330,
        yellow=900
    )

    GREEN_NOODLE_GRAB = ROBOT.choose(
        red=840,
        blue=1270,
        yellow=840
    )

    GREEN_NOODLE_OPEN = ROBOT.choose(
        red=450,
        blue=880,
        yellow=450
    )


# Red and Blue have tested values
class Arm(ServoEnum):
    port = ARM

    DOWN = ROBOT.choose(
        red=1775,
        blue=2600,
        yellow=1775
    )

    GRAB = ROBOT.choose(
        red=720,
        blue=1100,
        yellow=720
    )

    STRAIGHT = ROBOT.choose(
        red=600,
        blue=1000,
        yellow=600
    )

    UP = ROBOT.choose(
        red=335,
        blue=680,
        yellow=335
    )

    RED_NOODLE_GRAB_1 = ROBOT.choose(
        red=1370,
        blue=1770,
        yellow=1370
    )

    RED_NOODLE_GRAB_2 = ROBOT.choose(
        red=1420,
        blue=1820,
        yellow=1420
    )

    GREEN_NOODLE_GRAB = ROBOT.choose(
        red=1310,
        blue=1710,
        yellow=1310
    )

    RING = ROBOT.choose(
        red=1530,
        blue=1930,
        yellow=1530
    )


# Red and Blue have tested values
class BackClaw(ServoEnum):
    port = BACK_CLAW

    UP = ROBOT.choose(
        red=630,
        blue=160,
        yellow=630
    )

    DOWN = ROBOT.choose(
        red=1600,
        blue=850,
        yellow=1600
    )

    SUPERDOWN = ROBOT.choose(
        red=1900,
        blue=1200,
        yellow=1900
    )
