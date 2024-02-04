#!/usr/bin/env python3

"""Start the robot by selecting a mode."""

from pyPS4Controller.controller import Controller

from optimus_pi import Calibration, ManualDrive, ModeSelect


def main():
    """Main function to start the robot."""
    mode_select = ModeSelect(
        controller=Controller(
            interface="/dev/input/js0", connecting_using_ds4drv=False
        ),
        calibration=Calibration(),
        manual_drive=ManualDrive(),
    )
    mode_select.listen()


if __name__ == "__main__":
    main()
