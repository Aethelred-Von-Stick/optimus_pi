#! /usr/bin/env python3

"""Control the robot from user input."""

import yaml
from gpiozero import Motor

import optimus_pi.constants as c

import logging


class ManualDrive:
    """Control the robot using the left and right joysticks on a Dualshock4 controller."""

    def __init__(self, config_file=c.DEFAULT_CONFIG_FILE):
        self.value = None
        with open(config_file, encoding="utf-8") as file_pointer:
            config = yaml.load(file_pointer, Loader=yaml.Loader)
        self.lmot = Motor(*config["left_pins"])
        self.rmot = Motor(*config["right_pins"])
        self.max_joystick_values = config["max_joystick_values"]

    def handle_event(self, event):
        """Handle controller events."""
        self.value = event.value
        try:
            getattr(self, c.EVENT_MAP[event.name])()
        except AttributeError:
            logging.info("ManualDrive not handling %s event", event.name)

    def on_L3_up(self):
        """Left motor forward."""
        self.lmot.forward(self.value / self.max_joystick_values["l3_up_max"])

    def on_L3_down(self):
        """Left motor backward."""
        self.lmot.backward(self.value / self.max_joystick_values["l3_down_max"])

    def on_L3_y_at_rest(self):
        """Left motor stop."""
        self.lmot.stop()

    def on_R3_up(self):
        """Right motor forward."""
        self.rmot.forward(self.value / self.max_joystick_values["r3_up_max"])

    def on_R3_down(self):
        """Right motor backward."""
        self.rmot.backward(self.value / self.max_joystick_values["r3_down_max"])

    def on_R3_y_at_rest(self):
        """Right motor stop."""
        self.rmot.stop()
