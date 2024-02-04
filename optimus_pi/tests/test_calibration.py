#!/usr/bin/env python3

"""Tests for calibration."""

import yaml


def test_calibration(calibration, config_file, config_dict):
    """Test that the calibration file is written correctly."""
    expected_max_joystick_values = {
        "l3_up_max": 1,
        "l3_down_max": 2,
        "r3_up_max": 3,
        "r3_down_max": 4,
    }
    calibration.on_L3_up(1)
    calibration.on_L3_down(2)
    calibration.on_R3_up(3)
    calibration.on_R3_down(4)
    # The config file shouldn't be written to yet.
    assert yaml.load(config_file.read_text(), Loader=yaml.Loader) == config_dict
    calibration.on_x_press()
    assert (
        yaml.load(config_file.read_text(), Loader=yaml.Loader)["max_joystick_values"]
        == expected_max_joystick_values
    )
