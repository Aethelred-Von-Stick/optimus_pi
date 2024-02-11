"""Calls ``handle_event`` on downstream classes."""

import types
from dataclasses import dataclass
from typing import Optional

from pyPS4Controller.controller import Controller

import optimus_pi.constants as c


@dataclass
class Event:
    """Class containing controller event name and value."""

    name: str
    value: Optional[float] = None


class EventHandler(Controller):
    """Handles controller events, passing them to mode_select."""

    def __init__(self, mode_select, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mode_select = mode_select

    def __getattribute__(self, name):
        if name in c.INVERSE_EVENT_MAP:

            def on_event(self, value=None):
                event = Event(c.INVERSE_EVENT_MAP[name], value)
                self.mode_select.handle_event(event)

            return types.MethodType(on_event, self)
        return super().__getattribute__(name)
