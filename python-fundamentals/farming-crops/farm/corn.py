"""Module: corn

Defines the Corn crop, a subclass of Crop."""

from farm.crop import Crop


class Corn(Crop):
    """A corn crop that gains 10 grains each time it is watered."""

    def water(self):
        """Add 10 grains to the corn crop."""
        self.grains += 10
