#!/usr/bin/env python3

from pyPS4Controller.controller import Controller
from .manual_drive import ManualDrive
from .callibration import Callibration

class ModeSelect(Controller):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.modes = {
            "manual_drive": ManualDrive(interface="dev/input/js0"),
            "callibration": Callibration(interface="dev/input/js0"),
        }

    def stop_or_start_mode(self, mode):
        if self.modes[mode].stop:
            for mode in self.modes.values():
                mode.stop = True
            self.modes[mode].listen()
        else:
            self.modes[mode].stop = True

    def on_x_press(self):
        self.stop_or_start_mode("manual_drive")

    def on_share_press(self):
        self.stop_or_start_mode("callibration")
