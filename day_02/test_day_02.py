import unittest
from day_02.main import first_puzzle, second_puzzle

first_input = """
A Y
B X
C Z
"""


class TestDay02(unittest.TestCase):

    def test_rock_scissors_paper_strategy_one(self):
        assert first_puzzle(first_input) == 15

    def test_rock_scissors_paper_strategy_two(self):
        assert second_puzzle(first_input) == 12
