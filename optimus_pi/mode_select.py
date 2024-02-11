#!/usr/bin/env python3

"""Use a Dualshock4 controller for seting global modes."""

from .calibration import Calibration
from .manual_drive import ManualDrive
import optimus_pi.constants as c


class ModeSelect:
    """Select the mode to enter using a Dualshock4 controller."""

    def __init__(self, manual_drive, calibration):
        self.mode = None
        self.manual_drive = manual_drive
        self.calibration = calibration
        print("===========================")
        print("       Select Mode         ")
        print("===========================")
        print("[SQUARE] Manual Drive Mode.")
        print("[SHARE] Calibration Mode.  ")
        print("===========================")

    def on_square_press(self):
        """Enter or exit manual_drive mode."""
        if isinstance(self.mode, ManualDrive):
            print("Exiting Manual Drive Mode.")
            self.mode = None
        else:
            print("Entering Manual Drive Mode.")
            self.mode = self.manual_drive

    def on_share_press(self):
        """Enter or exit calibration mode."""
        if isinstance(self.mode, Calibration):
            print("Exiting Calibration Mode.")
            self.mode = None
        else:
            print("Entering Calibration Mode.")
            self.mode = self.calibration

    def handle_event(self, event):
        if event.name == c.SQUARE_PRESS:
            self.on_square_press()
        elif event.name == c.SHARE_PRESS:
            self.on_share_press()
        elif self.mode is not None:
            self.mode.handle_event(event)

