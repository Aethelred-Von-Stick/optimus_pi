#! /usr/bin/env python3

"""Settings for optimus pi."""

from pathlib import Path

LEFT_PINS = (8, 7)
RIGHT_PINS = (9, 10)

DEFAULT_MAX_CONTROLLER_VALUE = 2**16
DEFAULT_CONTROLLER_CALIBRATION = {
    "l3_up_max": -DEFAULT_MAX_CONTROLLER_VALUE,
    "l3_down_max": DEFAULT_MAX_CONTROLLER_VALUE,
    "r3_up_max": -DEFAULT_MAX_CONTROLLER_VALUE,
    "r3_down_max": DEFAULT_MAX_CONTROLLER_VALUE,
}

CACHE_DIR = Path(__file__).parent / ".cache"
CONTROLLER_CALIBRATION_FILE = CACHE_DIR / "max_controller_values.json"
