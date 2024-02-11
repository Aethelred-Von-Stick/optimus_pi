#!/usr/bin/env python3

"""Tests for calibration."""

import yaml

import optimus_pi.constants as c
from optimus_pi.event_handler import Event


def test_calibration(calibration, config_file, config_dict):
    """Test that the calibration file is written correctly."""
    expected_max_joystick_values = {
        "l3_up_max": 1,
        "l3_down_max": 2,
        "r3_up_max": 3,
        "r3_down_max": 4,
    }
    calibration.handle_event(Event(c.L3_UP, 1))
    calibration.handle_event(Event(c.L3_DOWN, 2))
    calibration.handle_event(Event(c.R3_UP, 3))
    calibration.handle_event(Event(c.R3_DOWN, 4))
    # The config file shouldn't be written to yet.
    assert yaml.load(config_file.read_text(), Loader=yaml.Loader) == config_dict
    calibration.handle_event(Event(c.X_PRESS))
    assert (
        yaml.load(config_file.read_text(), Loader=yaml.Loader)["max_joystick_values"]
        == expected_max_joystick_values
    )
