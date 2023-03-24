from drive import stop_motors
from kipr import msleep, push_button


def wait_for_button(text="waiting for button"):
    stop_motors()
    print(text)
    while not push_button():
        pass
    msleep(1000)
