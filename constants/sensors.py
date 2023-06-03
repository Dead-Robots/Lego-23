from kipr import gyro_z, msleep

from common import ROBOT

# sensor values
TOP_HAT_THRESHOLD_GREY = ROBOT.choose(
    red=3000,
    blue=3000,
    yellow=3400,
    green=3000
)

TOP_HAT_THRESHOLD = ROBOT.choose(
    red=2300,
    blue=2300,
    yellow=3000,
    green=2300
)

gyro_offset = 0


def gyroscope():
    return gyro_z() - gyro_offset


def calibrate_gyro():
    total = 0
    for x in range(50):
        total = total + gyro_z()
        msleep(10)
    global gyro_offset
    gyro_offset = total / 50
