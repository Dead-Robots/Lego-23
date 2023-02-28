from common import ROBOT
from common.core.enums import ServoEnum
from constants.ports import *


# Red (other than BackClaw) and Blue have tested values
class Arm(ServoEnum):
    port = ARM_SERVO

    DOWN = ROBOT.choose(
        red=1900,
        blue=2040,
        yellow=1900,
        green=1900
    )
    STRAIGHT = ROBOT.choose(
        red=600,
        blue=1000,
        yellow=600,
        green=600
    )

    UP = ROBOT.choose(
        red=350,
        blue=760,
        yellow=350,
        green=350
    )


class Claw(ServoEnum):
    port = CLAW_SERVO

    OPEN = ROBOT.choose(
        red=200,
        blue=0,
        yellow=200,
        green=200
    )

    CLOSED = ROBOT.choose(
        red=1000,
        blue=1570,
        yellow=1000,
        green=1000
    )


# only setup for blue
class BackClaw(ServoEnum):
    port = BACK_CLAW_SERVO

    UP = ROBOT.choose(
        red=200,
        blue=160,
        yellow=200,
        green=200
    )

    DOWN = ROBOT.choose(
        red=1000,
        blue=1050,
        yellow=1000,
        green=1000
    )
