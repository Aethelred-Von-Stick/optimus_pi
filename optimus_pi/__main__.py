#!/usr/bin/env python3

"""Start the robot by selecting a mode."""


from optimus_pi import Calibration, EventHandler, ManualDrive, ModeSelect


def main():
    """Main function to start the robot."""
    mode_select = ModeSelect(
        calibration=Calibration(),
        manual_drive=ManualDrive(),
    )
    event_handler = EventHandler(
        mode_select, interface="/dev/input/js0", connecting_using_ds4drv=False
    )
    event_handler.listen()


if __name__ == "__main__":
    main()
