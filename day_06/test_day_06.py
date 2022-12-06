import unittest

from day_06.main import first_puzzle, second_puzzle


class TestDay06(unittest.TestCase):

    def test_message_1(self):
        assert first_puzzle('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5

    def test_message_2(self):
        assert first_puzzle('nppdvjthqldpwncqszvftbrmjlhg') == 6

    def test_message_3(self):
        assert first_puzzle('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10

    def test_message_4(self):
        assert first_puzzle('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11

    def test_message_1_for_decoder_2(self):
        assert second_puzzle('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 19

    def test_message_2_for_decoder_2(self):
        assert second_puzzle('bvwbjplbgvbhsrlpgdmjqwftvncz') == 23

    def test_message_3_for_decoder_2(self):
        assert second_puzzle('nppdvjthqldpwncqszvftbrmjlhg') == 23

    def test_message_4_for_decoder_2(self):
        assert second_puzzle('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 29

    def test_message_5_for_decoder_2(self):
        assert second_puzzle('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 26
