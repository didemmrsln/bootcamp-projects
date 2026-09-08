"""Module: rice

Defines the Rice crop, a subclass of Crop."""

from farm.crop import Crop


class Rice(Crop):
    """A rice crop that gains 5 grains when watered and 10 when transplanted."""

    def water(self):
        """Add 5 grains to the rice crop."""
        self.grains += 5

    def transplant(self):
        """Add 10 grains to the rice crop."""
        self.grains += 10
