import unittest
from day_04.main import first_puzzle, second_puzzle

text_input = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


class TestDay04(unittest.TestCase):

    def test_assignments_fully_ranged(self):
        assert first_puzzle(text_input) == 2

    def test_assignments_overlapping(self):
        assert second_puzzle(text_input) == 4
