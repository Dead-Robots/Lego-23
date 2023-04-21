from common import ROBOT
# motor ports
RIGHT_MOTOR = 0
LEFT_MOTOR = 3
SERVO_REPLACEMENT = 1

# servo ports
CLAW = 0
ARM = ROBOT.choose(red=2, blue=1, yellow=1)         # Red has issues with servo port 1, so it uses port 3 for the arm instead
BACK_CLAW = ROBOT.choose(red=1, blue=2, yellow=2)

# sensor ports
TOP_HAT = 0
