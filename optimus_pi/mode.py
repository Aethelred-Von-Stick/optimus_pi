"""Base mode functionality."""

import logging

import optimus_pi.constants as c


class Mode:  # pylint: disable=too-few-public-methods
    """Base mode class."""

    def __init__(self):
        self.event = None

    def handle_event(self, event):
        """Handle controller events.

        Args:
            event (~optimus_pi.event_handler.Event): Event to handle.

        """
        self.event = event
        try:
            getattr(self, c.EVENT_MAP[event.name])()
        except AttributeError:
            logging.info(
                "%s not handling %s event", self.__class__.__name__, event.name
            )
