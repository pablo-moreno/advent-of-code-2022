import unittest
from collections import OrderedDict

from day_05.main import first_puzzle, second_puzzle, parse_input

text_input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""


class TestDay05(unittest.TestCase):

    def test_parse_input(self):
        result = parse_input(text_input)
        assert result == OrderedDict({
            'stacks': OrderedDict({
                1: ['Z', 'N'],
                2: ['M', 'C', 'D'],
                3: ['P'],
            }),
            'rearrangements': [
                [1, 2, 1],
                [3, 1, 3],
                [2, 2, 1],
                [1, 1, 2],
            ]
        })

    def test_reordered_message(self):
        assert first_puzzle(text_input) == 'CMZ'
