import unittest
from day_01.main import first_puzzle, second_puzzle

first_input = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


class TestDay01(unittest.TestCase):

    def test_get_elf_with_most_calories_carried(self):
        assert first_puzzle(first_input) == 24000

    def test_get_sum_of_first_three_elves_with_most_calories_carried(self):
        assert second_puzzle(first_input) == 45000
