from common import ROBOT
# motor ports
RIGHT_MOTOR = 0
LEFT_MOTOR = 3

# servo ports
CLAW = 0
ARM = ROBOT.choose(red=3, blue=1, yellow=1)         # Red has issues with servo port 1, so it uses port 3 for the arm instead
BACK_CLAW = 2

# sensor ports
TOP_HAT = 0
