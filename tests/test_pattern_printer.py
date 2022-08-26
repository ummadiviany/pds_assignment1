import unittest
from tasks.pattern_printer import print_pattern

from .get_func_output import return_func_output


class TestPatternPrinter(unittest.TestCase):
    def test_pattern_printer(self):
        self.assertEqual(return_func_output(print_pattern, 3), "----c----\n--c-b-c--\nc-b-a-b-c\n--c-b-c--\n----c----\n")

    def test_pattern_printer_2(self):
        self.assertEqual(return_func_output(print_pattern, 2), "--b--\nb-a-b\n--b--\n")