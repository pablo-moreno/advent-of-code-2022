import unittest
from day_02.main import first_puzzle, second_puzzle

first_input = """
A Y
B X
C Z
"""


class TestDay02(unittest.TestCase):

    def test_get_elf_with_most_calories_carried(self):
        assert first_puzzle(first_input) == 15

    def test_get_sum_of_first_three_elves_with_most_calories_carried(self):
        assert second_puzzle(first_input) == 12
