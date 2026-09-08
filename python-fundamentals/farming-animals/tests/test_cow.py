import unittest
from farm.cow import Cow


class TestCow(unittest.TestCase):

    def setUp(self):
        self.cow = Cow()

    def test_initialize_sets_milk_to_zero(self):
        """Test that Cow's milk is initialized to 0."""
        self.assertEqual(self.cow.milk, 0)

    def test_initialize_sets_energy_to_zero(self):
        """Test that Cow's energy is initialized to 0."""
        self.assertEqual(self.cow.energy, 0)

    def test_feed_extends_method(self):
        """Test that Cow has a feed method."""
        self.assertTrue(hasattr(self.cow, 'feed'))

    def test_feed_adds_milk(self):
        """Test that feeding a cow adds 2 liters of milk."""
        self.cow.feed()
        self.assertEqual(self.cow.milk, 2)
        self.cow.feed()
        self.assertEqual(self.cow.milk, 4)

    def test_feed_adds_energy(self):
        """Test that feeding a cow adds 1 energy."""
        self.cow.feed()
        self.assertEqual(self.cow.energy, 1)

    def test_talk_returns_correct_sound(self):
        """Test that the talk method returns 'moo'."""
        self.assertEqual(self.cow.talk(), "moo")
