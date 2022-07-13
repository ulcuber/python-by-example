"""
Test output
"""

import unittest

from tests.case import TestCase


class Exercise1TestCase(TestCase):
    """
    Test outputs 'Hello, world!'
    """

    def test(self):
        """
        Checks
        """
        self.assertEqual(self.target.main(), None)
        self.assert_output("Hello, world!\n")


if __name__ == "__main__":
    unittest.main()
