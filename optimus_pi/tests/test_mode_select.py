#!/usr/bin/env python3

"""Tests for mode selection."""

import optimus_pi.constants as c
from optimus_pi import Calibration, Event, ManualDrive


def test_on_square_press(mode_select):
    """manual_drive mode should be switched on."""
    assert mode_select.mode is None
    mode_select.handle_event(Event(c.SQUARE_PRESS))
    assert isinstance(mode_select.mode, ManualDrive)
    # Test that manual_drive mode is turned off.
    mode_select.handle_event(Event(c.SQUARE_PRESS))
    assert mode_select.mode is None


def test_on_share_press(mode_select):
    """calibration_mode should be switched on."""
    assert mode_select.mode is None
    mode_select.handle_event(Event(c.SHARE_PRESS))
    assert isinstance(mode_select.mode, Calibration)
    # Test that calibration mode is turned off.
    mode_select.handle_event(Event(c.SHARE_PRESS))
    assert mode_select.mode is None
