#!/usr/bin/env python3

"""Use a Dualshock4 controller for seting global modes."""

from .calibration import Calibration
from .manual_drive import ManualDrive


class ModeSelect:
    """Select the mode to enter using a Dualshock4 controller."""
    def __init__(self, controller, manual_drive, calibration):
        self.mode = None
        self.controller = controller
        self.manual_drive = manual_drive
        self.calibration = calibration

    def on_square_press(self):
        """Enter or exit manual_drive mode."""
        if isinstance(self.mode, ManualDrive):
            self.mode = None
        else:
            self.mode = self.manual_drive

    def on_share_press(self):
        """Enter or exit calibration mode."""
        if isinstance(self.mode, Calibration):
            self.mode = None
        else:
            self.mode = self.calibration

    def __getattr__(self, name):
        try:
            getattr(self.mode, name)
        except AttributeError:
            getattr(self.controller, name)
