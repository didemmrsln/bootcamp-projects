# pylint: disable=too-few-public-methods

"""Module: crop

Defines the base Crop class shared by all crop types."""


class Crop:
    """A generic crop that produces grains and can ripen."""

    def __init__(self):
        self.grains = 0

    def ripe(self):
        """Return True if the crop has at least 15 grains."""
        return self.grains >= 15
