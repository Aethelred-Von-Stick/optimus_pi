#!/usr/bin/env python3

"""Use a Dualshock4 controller for seting global modes."""

from pyPS4Controller.controller import Controller
from .manual_drive import ManualDrive
from .calibration import Calibration

class ModeSelect(Controller):
    """Select the mode to enter using a Dualshock4 controller."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.modes = {
            "manual_drive": ManualDrive(interface=self.interface),
            "calibration": Calibration(interface=self.interface),
        }

    def stop_or_start_mode(self, mode):
        """Start or stop a mode. If starting, ensure all other modes are stopped.

        Args:
            mode (str): The key to a mode to be stopped.

        """
        if self.modes[mode].stop:
            for control_mode in self.modes.values():
                control_mode.end()
            self.modes[mode].start()
        else:
            self.modes[mode].end()

    def on_square_press(self):
        self.stop_or_start_mode("manual_drive")

    def on_share_press(self):
        self.stop_or_start_mode("calibration")

    def on_x_press(self):
        if not self.modes["calibration"].stop:
            self.modes["calibration"].save()
