"""
Test input
"""

import unittest
from unittest.mock import patch
from tests.case import TestCase


class Exercise2TestCase(TestCase):
    """
    Test outputs 'Hello, Username!'
    where Username comes from user input
    """

    @patch("builtins.input", return_value="Username")
    # pylint: disable=redefined-builtin,unused-argument
    def test(self, input):
        """
        Checks
        """
        self.assertEqual(self.target.main(), None)
        self.assert_output("Hello, Username!\n")


if __name__ == "__main__":
    unittest.main()
