"Base test case"

import importlib
import io
import sys
import unittest


class TestCase(unittest.TestCase):
    "Common set up"

    target = None

    @classmethod
    def setUpClass(cls):
        try:
            exercise = int("".join(filter(str.isdigit, cls.__name__)))
            cls.target = importlib.import_module(f"src.exercise{exercise}")
        except ModuleNotFoundError as not_found:
            raise unittest.SkipTest(
                f"Exercise {exercise} not implemented yet"
            ) from not_found
        if not cls.target.main:
            raise unittest.SkipTest(f"Exercise {exercise} has no main method")

    @classmethod
    def tearDownClass(cls):
        cls.target = None

    def setUp(self) -> None:
        self.output = io.StringIO()
        sys.stdout = self.output
        return super().setUp()

    def tearDown(self) -> None:
        sys.stdout = sys.__stdout__
        return super().tearDown()

    def assert_output(self, output: str) -> None:
        """
        Asserts captured output equal to argument string
        """
        self.assertEqual(self.output.getvalue(), output)
