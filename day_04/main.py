from datetime import datetime
from pathlib import Path


def first_puzzle(text: str) -> int:
    count = 0
    lines = text.strip().splitlines()

    for line in lines:
        first, second = line.split(',')
        first = [int(x) for x in first.split('-')]
        second = [int(x) for x in second.split('-')]

        first_left, first_right = first
        second_left, second_right = second

        first, second = list(range(first_left, first_right + 1)), list(range(second_left, second_right + 1))
        if set(first).issubset(second) or set(second).issubset(first):
            count += 1
    return count


def second_puzzle(text: str) -> int:
    count = 0
    lines = text.strip().splitlines()

    for line in lines:
        first, second = line.split(',')
        first = [int(x) for x in first.split('-')]
        second = [int(x) for x in second.split('-')]

        first_left, first_right = first
        second_left, second_right = second

        first, second = list(range(first_left, first_right + 1)), list(range(second_left, second_right + 1))
        if not set(first).isdisjoint(second) or not set(second).isdisjoint(first):
            count += 1
    return count


def main():
    path = Path(__file__).resolve().parent / 'input.txt'
    with open(path) as f:
        text_input = f.read()

        before_puzzle_one = datetime.now()
        solution_first_puzzle = first_puzzle(text_input)
        after_puzzle_one = datetime.now() - before_puzzle_one

        print(f'The total fully ranged assignments is... {solution_first_puzzle}!')
        print(f'{after_puzzle_one.microseconds} µs')

        before_puzzle_two = datetime.now()
        solution_second_puzzle = second_puzzle(text_input)
        after_second_puzzle = datetime.now() - before_puzzle_two

        print(f'The total overlapped assignments is... {solution_second_puzzle}!')
        print(f'{after_second_puzzle.microseconds} µs')


if __name__ == '__main__':
    main()
