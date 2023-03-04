from common import ROBOT
from common.core.enums import ServoEnum
from constants.ports import *


# Red (other than BackClaw) and Blue have tested values
class Arm(ServoEnum):
    port = ARM

    DOWN = ROBOT.choose(
        red=1500,
        blue=1900,
        yellow=1500,
        green=1900
    )

    GRAB = ROBOT.choose(
        red=675,
        blue=1075,
        yellow=400,
        green=675
    )

    STRAIGHT = ROBOT.choose(
        red=600,
        blue=1000,
        yellow=330,
        green=600
    )

    UP = ROBOT.choose(
        red=350,
        blue=650,
        yellow=0,
        green=350
    )


class Claw(ServoEnum):
    port = CLAW

    OPEN = ROBOT.choose(
        red=600,
        blue=0,
        yellow=300,
        green=200
    )

    CLOSED = ROBOT.choose(
        red=1230,
        blue=1570,
        yellow=1000,
        green=1000
    )

    GRAB = ROBOT.choose(
        red=1700,
        blue=1570,
        yellow=1500,
        green=1000
    )


# only setup for blue
class BackClaw(ServoEnum):
    port = BACK_CLAW

    UP = ROBOT.choose(
        red=700,
        blue=160,
        yellow=750,
        green=200
    )

    DOWN = ROBOT.choose(
        red=1700,
        blue=1050,
        yellow=1650,
        green=1000
    )
