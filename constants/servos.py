from common import ROBOT
from common.core.enums import ServoEnum
from constants.ports import *


class Claw(ServoEnum):
    port = CLAW

    OPEN = ROBOT.choose(
        red=000,
        blue=430,
        yellow=300
    )

    CLOSED = ROBOT.choose(
        red=850,
        blue=1330,
        yellow=1000
    )

    GRAB = ROBOT.choose(
        red=950,
        blue=1430,
        yellow=1500
    )

    NOODLE_GRAB = ROBOT.choose(
        red=840,
        blue=1270,
        yellow=840
    )

    NOODLE_OPEN = ROBOT.choose(
        red=450,
        blue=880,
        yellow=450
    )


# Red (other than BackClaw) and Blue have tested values
class Arm(ServoEnum):
    port = ROBOT.choose(
        red=3,
        blue=ARM,
        yellow=ARM
    )

    DOWN = ROBOT.choose(
        red=1775,
        blue=2040,
        yellow=1500
    )

    GRAB = ROBOT.choose(
        red=720,
        blue=1100,
        yellow=400
    )

    STRAIGHT = ROBOT.choose(
        red=600,
        blue=1000,
        yellow=330
    )

    UP = ROBOT.choose(
        red=335,
        blue=680,
        yellow=0
    )

    NOODLE = ROBOT.choose(
        red=1200,
        blue=1600,
        yellow=930
    )

    RING = ROBOT.choose(
        red=1530,
        blue=1930,
        yellow=1260
    )


# only setup for blue, red
class BackClaw(ServoEnum):
    port = BACK_CLAW

    UP = ROBOT.choose(
        red=630,
        blue=160,
        yellow=750
    )

    DOWN = ROBOT.choose(
        red=1600,
        blue=850,
        yellow=1650
    )

    SUPERDOWN = ROBOT.choose(
        red=1900,
        blue=1200,
        yellow=1850
    )
