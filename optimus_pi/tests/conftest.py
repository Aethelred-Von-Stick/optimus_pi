#!/usr/bin/env python3

"""Fixtures for optimus_pi tests."""

from unittest import mock

import pytest
import yaml

from optimus_pi.calibration import Calibration
from optimus_pi.manual_drive import ManualDrive
from optimus_pi.mode_select import ModeSelect


@pytest.fixture(name="config_dict")
def fixture_config_dict():
    """Set up a dictionary with configuration parameters."""
    return {
        "left_pins": [8, 7],
        "right_pins": [9, 10],
        "max_joystick_values": {
            "l3_up_max": -0x10000,
            "l3_down_max": 0x10000,
            "r3_up_max": -0x10000,
            "r3_down_max": 0x10000,
        },
    }


@pytest.fixture(name="config_file")
def fixture_config_file(tmp_path, config_dict):
    """Set up a YAML config file."""
    config_file = tmp_path / "config.yml"
    with config_file.open("w", encoding="utf-8") as file_pointer:
        yaml.dump(config_dict, file_pointer, Dumper=yaml.Dumper)
    return config_file


@pytest.fixture(name="calibration")
def fixture_calibration(config_file):
    """Initialise a Calibration object."""
    return Calibration(config_file=config_file)


@pytest.fixture(name="manual_drive")
def fixture_manual_drive():
    """Initialise a ManualDrive object."""
    with mock.patch("optimus_pi.manual_drive.Motor"):
        yield ManualDrive()


@pytest.fixture(name="mode_select")
def fixture_mode_select(calibration, manual_drive):
    """Initialise a ModeSelect object."""
    return ModeSelect(manual_drive, calibration)
