from common import ROBOT
# motor ports
RIGHT_MOTOR = 0
LEFT_MOTOR = 3
SERVO_REPLACEMENT = 1

# servo ports
CLAW = ROBOT.choose(red=0, blue=0, yellow=0)
ARM = ROBOT.choose(red=1, blue=1, yellow=1)
# instead
BACK_CLAW = ROBOT.choose(red=2, blue=2, yellow=2)

# sensor ports
LEFT_TOP_HAT = 0
RIGHT_TOP_HAT = 1
