#! /usr/bin/env python3

"""Control the robot from user input."""

import yaml

from gpiozero import Motor

class ManualDrive:
    """Control the robot using the left and right joysticks on a Dualshock4 controller."""
    def __init__(self):
        with open("config.yml", encoding="utf-8") as file_pointer:
            config = yaml.load(file_pointer, Loader=yaml.Loader)
        self.lmot = Motor(config["left_pins"]["pos"], config["left_pins"]["neg"])
        self.rmot = Motor(config["right_pins"]["pos"], config["left_pins"]["neg"])
        self.max_joystick_values = config["max_joystick_values"]

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
