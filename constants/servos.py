from common import ROBOT
from common.core.enums import ServoEnum
from constants.ports import *


# Red (other than BackClaw) and Blue have tested values
class Arm(ServoEnum):
    port = ARM

    DOWN = ROBOT.choose(
        red=1900,
        blue=1900,
        yellow=1900,
        green=1900
    )

    GRAB = ROBOT.choose(
        red=675,
        blue=1075,
        yellow=675,
        green=675
    )

    STRAIGHT = ROBOT.choose(
        red=600,
        blue=1000,
        yellow=600,
        green=600
    )

    UP = ROBOT.choose(
        red=350,
        blue=650,
        yellow=350,
        green=350
    )


class Claw(ServoEnum):
    port = CLAW

    OPEN = ROBOT.choose(
        red=200,
        blue=0,
        yellow=50,
        green=200
    )

    CLOSED = ROBOT.choose(
        red=1000,
        blue=1570,
        yellow=675,
        green=1000
    )


# only setup for blue
class BackClaw(ServoEnum):
    port = BACK_CLAW

    UP = ROBOT.choose(
        red=200,
        blue=160,
        yellow=635,
        green=200
    )

    DOWN = ROBOT.choose(
        red=1000,
        blue=1050,
        yellow=1730,
        green=1000
    )
