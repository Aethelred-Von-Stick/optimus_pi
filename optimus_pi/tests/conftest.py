#!/usr/bin/env python3

"""Fixtures for optimus_pi tests."""

from unittest import mock

import pytest
from pyPS4Controller.controller import Controller

from optimus_pi.calibration import Calibration
from optimus_pi.manual_drive import ManualDrive
from optimus_pi.mode_select import ModeSelect


@pytest.fixture(name="calibration")
def fixture_calibration():
    """Initialise a Calibration object."""
    return Calibration()

@pytest.fixture(name="manual_drive")
def fixture_manual_drive():
    """Initialise a ManualDrive object."""
    with mock.patch("optimus_pi.manual_drive.Motor"):
        yield ManualDrive()

@pytest.fixture(name="mode_select")
def fixture_mode_select(calibration, manual_drive):
    """Initialise a ModeSelect object."""
    controller = mock.MagicMock(spec=Controller)
    return ModeSelect(controller, manual_drive, calibration)
