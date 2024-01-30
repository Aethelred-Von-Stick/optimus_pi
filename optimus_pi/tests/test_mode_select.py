#!/usr/bin/env python3

"""Tests for mode selection."""

from optimus_pi.manual_drive import ManualDrive
from optimus_pi.calibration import Calibration


def test_on_square_press(mode_select, manual_drive):
    """manual_drive mode should be on and it's attributes exposed."""
    assert mode_select.mode is None
    mode_select.on_square_press()
    assert isinstance(mode_select.mode, ManualDrive)
    # Test that attributes from ManualDrive take presidence over Controller.
    assert mode_select.on_R3_up is manual_drive.on_R3_up
    # Test that we have inhereted attributes from Controller.
    assert hasattr(mode_select, "listen")
    # Test that manual_drive mode is turned off.
    mode_select.on_square_press()
    assert mode_select.mode is None


def test_on_share_press(mode_select, calibration):
    """calibration mode should be on and it's attributes exposed."""
    assert mode_select.mode is None
    mode_select.on_share_press()
    assert isinstance(mode_select.mode, Calibration)
    # Test that attributes from Calibration take presidence over Controller.
    assert mode_select.on_R3_up is calibration.on_R3_up
    # Test that we have inhereted attributes from Controller.
    assert hasattr(mode_select, "listen")
    # Test that calibration mode is turned off.
    mode_select.on_share_press()
    assert mode_select.mode is None
