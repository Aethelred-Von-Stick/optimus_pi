#!/usr/bin/env python3

"""Start the robot by selecting a mode."""

from .mode_select import ModeSelect

def main():
    """Main function to start the robot."""
    mode_select = ModeSelect(interface="/dev/input/js0", use_ds4_drv=False)
    mode_select.listen()

if __name__ == "__main__":
    main()
