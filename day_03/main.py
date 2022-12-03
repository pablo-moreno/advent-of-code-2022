import string
from datetime import datetime
from pathlib import Path

item_values = dict()
item_values.update(zip(string.ascii_lowercase, range(1, 27)))
item_values.update(zip(string.ascii_uppercase, range(27, 53)))


def first_puzzle(text: str) -> int:
    rucksacks = text.strip().splitlines()
    value = 0

    for rucksack in rucksacks:
        length = int(len(rucksack) / 2)
        a, b = set(rucksack[:length]), set(rucksack[length:])
        repeated = a.intersection(b)
        for repeated_item in repeated:
            value += item_values.get(repeated_item)

    return value


def second_puzzle(text: str) -> int:
    rucksack_groups = text.strip().splitlines()
    groups = (rucksack_groups[i:i + 3] for i in range(0, len(rucksack_groups), 3))
    value = 0

    for a, b, c in groups:
        repeated = set(a).intersection(set(b)).intersection(set(c))
        for repeated_item in repeated:
            value += item_values.get(repeated_item)

    return value


def main():
    path = Path(__file__).resolve().parent / 'input.txt'
    with open(path) as f:
        text_input = f.read()

        before_puzzle_one = datetime.now()
        solution_first_puzzle = first_puzzle(text_input)
        after_puzzle_one = datetime.now() - before_puzzle_one

        print(f'The total value #1 is... {solution_first_puzzle}!')
        print(f'{after_puzzle_one.microseconds} µs')

        before_puzzle_two = datetime.now()
        solution_second_puzzle = second_puzzle(text_input)
        after_second_puzzle = datetime.now() - before_puzzle_two

        print(f'The total value #2 is... {solution_second_puzzle}!')
        print(f'{after_second_puzzle.microseconds} µs')


if __name__ == '__main__':
    main()
