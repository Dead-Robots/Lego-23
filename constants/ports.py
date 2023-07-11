from common import ROBOT
# motor ports
RIGHT_MOTOR = 0
RAKE = 1
GRAYSON = 2
LEFT_MOTOR = 3

# servo ports
CLAW = ROBOT.choose(red=1, blue=0, yellow=0, green=1)
ARM = ROBOT.choose(red=3, blue=3, yellow=1, green=2)
WRIST = ROBOT.choose(red=0, blue=2, yellow=2, green=0)

# analog ports
LEFT_TOP_HAT = 0
RIGHT_TOP_HAT = 1
LIGHT_SENSOR = ROBOT.choose(red=5, green=5)
