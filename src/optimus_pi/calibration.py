#!/usr/bin/env python3
import json

from pyPS4Controller.controller import Controller
from .config import CONTROLLER_CALIBRATION_FILE

class Calibration(Controller):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.max_joystick_values = {
            "l3_up_max": 0,
            "l3_down_max": 0,
            "r3_up_max": 0,
            "r3_down_max": 0,
        }

    def on_L3_up(self, value):
        if abs(value) > abs(max_joystick_values["l3_up_max"]):
            self.max_joystick_values["l3_up_max"] = value

    def on_L3_down(self, value):
        if abs(value) > abs(max_joystick_values["l3_down_max"]):
            self.max_joystick_values["l3_down_max"] = value

    def on_R3_up(self, value):
        if abs(value) > abs(max_joystick_values["r3_up_max"]):
            self.max_joystick_values["r3_up_max"] = value

    def on_R3_down(self, value):
        if abs(value) > abs(max_joystick_values["r3_down_max"]):
            self.max_joystick_values["r3_down_max"] = value

    def stop(self):
        with open(os.path.join(CONTROLLER_CALIBRATION_FILE), "w") as fp:
            json.dump(self.max_joystick_values, fp)
