from datetime import datetime
from pathlib import Path


def first_puzzle(text: str) -> int:
    elves_calories_str = text.strip().split('\n\n')

    max_calories = 0
    for item in elves_calories_str:
        elf_calories = sum(int(x) for x in item.split('\n'))

        if elf_calories > max_calories:
            max_calories = elf_calories

    return max_calories


def first_puzzle_one_liner(text: str) -> int:
    return max([sum(int(x) for x in item.splitlines()) for item in text.strip().split('\n\n')])


def second_puzzle(text: str) -> int:
    elves_calories_str = text.strip().split('\n\n')

    elves_calories_values = []
    for item in elves_calories_str:
        elf_calories = sum(int(x) for x in item.split('\n'))
        elves_calories_values.append(elf_calories)

    sorted_list = sorted(elves_calories_values, reverse=True)
    return sum(sorted_list[:3])


def second_puzzle_one_liner(text: str) -> int:
    return sum(sorted([sum(int(x) for x in i.splitlines()) for i in text.strip().split('\n\n')], reverse=True)[:3])


def main():
    path = Path(__file__).resolve().parent / 'input.txt'
    with open(path) as f:
        text_input = f.read()

        before_puzzle_one = datetime.now()
        solution_first_puzzle = first_puzzle(text_input)
        after_puzzle_one = datetime.now() - before_puzzle_one

        print(f'The elf with most calories is... {solution_first_puzzle} !!')
        print(f'{after_puzzle_one.microseconds}  µs')

        before_puzzle_two = datetime.now()
        solution_second_puzzle = second_puzzle(text_input)
        after_second_puzzle = datetime.now() - before_puzzle_two

        print(f'The sum of the three elves with most calories carried is... {solution_second_puzzle} !!')
        print(f'{after_second_puzzle.microseconds}  µs')


if __name__ == '__main__':
    main()
