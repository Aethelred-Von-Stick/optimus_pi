#!/usr/bin/env python3
import json

from pyPS4Controller.controller import Controller
from .config import CONTROLLER_CALIBRATION_FILE

class Calibration:
    """Class for calibrating Dualshock4 joystick input."""
    def __init__(self):
        self.max_joystick_values = {
            "l3_up_max": 0,
            "l3_down_max": 0,
            "r3_up_max": 0,
            "r3_down_max": 0,
        }

    def on_x_press(self):
        """Save the maximum joystick values to the calibration file."""
        with CONTROLLER_CALIBRATION_FILE.open("w") as file_pointer:
            json.dump(self.max_joystick_values, file_pointer)

    def _assign_high_input(self, joystick_key, value):
        if abs(value) > abs(self.max_joystick_values[joystick_key]):
            self.max_joystick_values[joystick_key] = value

    def on_L3_up(self, value):
        self._assign_high_input("l3_up_max", value)

    def on_L3_down(self, value):
        self._assign_high_input("l3_down_max", value)

    def on_R3_up(self, value):
        self._assign_high_input("r3_up_max", value)

    def on_R3_down(self, value):
        self._assign_high_input("r3_down_max", value)

