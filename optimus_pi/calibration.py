#!/usr/bin/env python3

"""Module for calibration, editing the config.yml file."""

import yaml

import optimus_pi.constants as c
from optimus_pi.mode import Mode


class Calibration(Mode):
    """Class for calibrating Dualshock4 joystick input."""

    def __init__(self, config_file=c.DEFAULT_CONFIG_FILE):
        super().__init__()
        self.config_file = config_file
        with open(self.config_file, encoding="utf-8") as file_pointer:
            self.config = yaml.load(file_pointer, Loader=yaml.Loader)
        self.config["max_joystick_values"] = {
            "l3_up_max": 0,
            "l3_down_max": 0,
            "r3_up_max": 0,
            "r3_down_max": 0,
        }

    def _assign_high_input(self, joystick_key):
        if abs(self.event.value) > abs(
            self.config["max_joystick_values"][joystick_key]
        ):
            self.config["max_joystick_values"][joystick_key] = self.event.value

    def on_x_press(self):
        """Save the maximum joystick values to the calibration file."""
        print("Saving Configuration")
        print(self.config)
        with open(self.config_file, "w", encoding="utf-8") as file_pointer:
            yaml.dump(self.config, file_pointer)

    def on_L3_up(self):
        """Update the config with the highest value from the controller."""
        self._assign_high_input("l3_up_max")

    def on_L3_down(self):
        """Update the config with the highest value from the controller."""
        self._assign_high_input("l3_down_max")

    def on_R3_up(self):
        """Update the config with the highest value from the controller."""
        self._assign_high_input("r3_up_max")

    def on_R3_down(self):
        """Update the config with the highest value from the controller."""
        self._assign_high_input("r3_down_max")
