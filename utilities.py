from drive import stop_motors
from kipr import msleep, push_button


def wait_for_button():
    stop_motors()
    print("Waiting for button")
    while not push_button():
        pass
    msleep(1000)
