from dataclasses import dataclass
from typing import Optional
import types

from pyPS4Controller.controller import Controller

import optimus_pi.constants as c

@dataclass
class Event:
    name: str
    value: Optional[float] = None

class EventHandler(Controller):
#    for name in c.INVERSE_EVENT_MAP:
#        def on_event(self, value=None):
#            event = Event(name, value)
#            self.mode_select.handle_event(event)
#        setattr(EventHandler, name, on_event)

    def __init__(self, mode_select, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mode_select = mode_select

    def __getattribute__(self, name):
        if name in c.INVERSE_EVENT_MAP:
            def on_event(self, value=None):
                event = Event(name, value)
                self.mode_select.handle_event(event)
            return types.MethodType(self, on_event)
        else:
            return super().__getattribute__(name)
        
