# pylint: disable-all
import unittest
from pathlib import Path

class TestTestsAreComplete(unittest.TestCase):
    def test_tests_are_complete(self):
        """Test that Tests have been defined for Cow"""
        path = Path("tests/test_euclidean.py")
        self.assertTrue(path.is_file(),
                        msg="You have not yet defined tests for Euclidean distance")
