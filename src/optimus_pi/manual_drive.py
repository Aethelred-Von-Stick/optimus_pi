#! /usr/bin/env python3

"""Control the robot from user input."""

import json

from pyPS4Controller.controller import Controller
from gpiozero import Motor

from .config import (
    LEFT_PINS,
    RIGHT_PINS,
    DEFAULT_CONTROLLER_CALIBRATION,
    CONTROLLER_CALIBRATION_FILE,
)


class ManualDrive(Controller):
    """Control the robot using the left and right joysticks on a Dualshock4 controller."""
    def __init__(self, **kwargs):
        print(kwargs)
        super().__init__(**kwargs)
        self.lmot = Motor(*LEFT_PINS)
        self.rmot = Motor(*RIGHT_PINS)

        if CONTROLLER_CALIBRATION_FILE.exists():
            self.max_joystick_values = json.loads(
                CONTROLLER_CALIBRATION_FILE.read_text()
            )
        else:
            self.max_joystick_values = DEFAULT_CONTROLLER_CALIBRATION

    def start(self):
        """Start listening to controller events."""
        self.listen()

    def end(self):
        """Set the stop attribute to stop listening."""
        self.stop = True

    def on_L3_up(self, value):
        self.lmot.forward(value / self.max_joystick_values["l3_up_max"])

    def on_L3_down(self, value):
        self.lmot.backward(value / self.max_joystick_values["l3_down_max"])

    def on_L3_y_at_rest(self):
        self.lmot.stop()

    def on_R3_up(self, value):
        self.rmot.forward(value / self.max_joystick_values["r3_up_max"])

    def on_R3_down(self, value):
        self.rmot.backward(value / self.max_joystick_values["r3_down_max"])

    def on_R3_y_at_rest(self):
        self.rmot.stop()


if __name__ == "__main__":
    controller = ManualDrive(interface="/dev/input/js0", connecting_using_ds4drv=False)
    controller.listen()
