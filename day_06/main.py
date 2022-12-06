from datetime import datetime
from pathlib import Path


def decoder(text, length):
    for i in range(len(text)):
        count = len(set(text[i:i + length]))
        if count == length:
            return i + length


def first_puzzle(text: str) -> int:
    return decoder(text, 4)


def second_puzzle(text: str) -> str:
    return decoder(text, 14)


def main():
    path = Path(__file__).resolve().parent / 'input.txt'
    with open(path) as f:
        text_input = f.read()

        before_puzzle_one = datetime.now()
        solution_first_puzzle = first_puzzle(text_input)
        after_puzzle_one = datetime.now() - before_puzzle_one

        print(f'The first marker for 4 different characters is... {solution_first_puzzle}!')
        print(f'{after_puzzle_one.microseconds} µs')

        before_puzzle_two = datetime.now()
        solution_second_puzzle = second_puzzle(text_input)
        after_second_puzzle = datetime.now() - before_puzzle_two

        print(f'The first marker for 14 different characters is... {solution_second_puzzle}!')
        print(f'{after_second_puzzle.microseconds} µs')


if __name__ == '__main__':
    main()
