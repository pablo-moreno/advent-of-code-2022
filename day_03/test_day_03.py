import unittest
from day_03.main import first_puzzle, second_puzzle

first_input = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


class TestDay03(unittest.TestCase):

    def test_rucksacks_rearrangement(self):
        assert first_puzzle(first_input) == 157

    def test_rucksacks_rearrangement_by_groups(self):
        assert second_puzzle(first_input) == 70
