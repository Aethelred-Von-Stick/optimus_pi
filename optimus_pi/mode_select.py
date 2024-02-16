#!/usr/bin/env python3

"""Use a Dualshock4 controller for seting global modes."""

import optimus_pi.constants as c

from .calibration import Calibration
from .line_follower import LineFollower
from .manual_drive import ManualDrive


class ModeSelect:
    """Select the mode to enter using a Dualshock4 controller."""

    def __init__(self, manual_drive, calibration, line_follower):
        """Select the mode to enter using a Dualshock4 controller.

        Args:
            manual_drive (~optimus_pi.manual_drive.ManualDrive): A ManualDrive
                instance.
            calibration (~optimus_pi.calibration.Calibration): A Calibration
                instance.
            line_follower (~optimus_pi.line_follower.LineFollower): A line
                follower instance.

        """
        self.mode = None
        self.manual_drive = manual_drive
        self.calibration = calibration
        self.line_follower = line_follower
        print("==============================")
        print("         Select Mode          ")
        print("==============================")
        print("[SQUARE] Manual Drive Mode.   ")
        print("[SHARE] Calibration Mode.     ")
        print("[TRIANGLE] Line Follower Mode.")
        print("==============================")

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

    def on_triangle_press(self):
        """Enter or exit line following mode."""
        if isinstance(self.mode, LineFollower):
            print("Exiting Line Following Mode.")
            self.mode.finish()
            self.mode = None
        else:
            print("Entering Line Following Mode.")
            self.mode = self.line_follower
            self.mode.start()

    def handle_event(self, event):
        """Handle controller events."""
        if event.name == c.SQUARE_PRESS:
            self.on_square_press()
        elif event.name == c.SHARE_PRESS:
            self.on_share_press()
        elif self.mode is not None:
            self.mode.handle_event(event)
