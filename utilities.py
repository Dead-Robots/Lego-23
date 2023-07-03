from kipr import push_button, disable_servos, freeze
from time import sleep


def msleep(milliseconds):
    sleep(milliseconds/1000)


def debug():
    disable_servos()
    freeze(0)
    freeze(1)
    freeze(2)
    freeze(3)
    msleep(1000)
    print("stopping code for debug")
    exit(0)
