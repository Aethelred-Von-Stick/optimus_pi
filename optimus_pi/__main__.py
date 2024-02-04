#!/usr/bin/env python3

"""Start the robot by selecting a mode."""

from pyPS4Controller.controller import Controller

from optimus_pi import Calibration, ManualDrive, ModeSelect, EventHandler


def main():
    """Main function to start the robot."""
    mode_select = ModeSelect(
        calibration=Calibration(),
        manual_drive=ManualDrive(),
    )
    event_handler = EventHandler(mode_select, interface="/dev/input/js0", connecting_using_ds4drv=False)
    event_handler.listen()


if __name__ == "__main__":
    main()
