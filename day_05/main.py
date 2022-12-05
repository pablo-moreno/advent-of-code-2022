from collections import OrderedDict, defaultdict
from datetime import datetime
from pathlib import Path


def parse_input(text: str) -> dict:
    result = OrderedDict({
        'stacks': OrderedDict(),
        'rearrangements': [],
    })
    stacks, movements = text.replace('[', ' ').replace(']', ' ').split('\n\n')
    stacks = stacks.splitlines()[:-1]
    movements = movements.splitlines()

    for stack in stacks:
        values = list(stack)[1::4]
        for i, v in enumerate(values, 1):
            if not result.get('stacks').get(i):
                result['stacks'][i] = []

            if v != ' ':
                result['stacks'][i].append(v)

    for key in result['stacks'].keys():
        result['stacks'][key] = result['stacks'][key][::-1]

    for movement in movements:
        rearrangements = movement.replace('move', '').replace('from', '').replace('to', '').split(' ')
        rearrangements = [int(x) for x in rearrangements if x]
        result['rearrangements'].append(rearrangements)

    return result


def first_puzzle(text: str) -> str:
    parsed_input = parse_input(text)
    stacks, rearrangements = parsed_input.get('stacks'), parsed_input.get('rearrangements')

    for rearrangement in rearrangements:
        amount, move_from, move_to = rearrangement
        limit = len(stacks[move_from]) - amount

        stacks[move_to].extend(stacks[move_from][-amount:][::-1])
        stacks[move_from] = stacks[move_from][:limit]

    return ''.join(v[-1] for k, v in stacks.items())


def second_puzzle(text: str) -> str:
    parsed_input = parse_input(text)
    stacks, rearrangements = parsed_input.get('stacks'), parsed_input.get('rearrangements')

    for rearrangement in rearrangements:
        amount, move_from, move_to = rearrangement
        limit = len(stacks[move_from]) - amount

        stacks[move_to].extend(stacks[move_from][-amount:])
        stacks[move_from] = stacks[move_from][:limit]

    return ''.join(v[-1] for k, v in stacks.items())


def main():
    path = Path(__file__).resolve().parent / 'input.txt'
    with open(path) as f:
        text_input = f.read()

        before_puzzle_one = datetime.now()
        solution_first_puzzle = first_puzzle(text_input)
        after_puzzle_one = datetime.now() - before_puzzle_one

        print(f'The top crate result for default rearrangement system is... {solution_first_puzzle}!')
        print(f'{after_puzzle_one.microseconds} µs')

        before_puzzle_two = datetime.now()
        solution_second_puzzle = second_puzzle(text_input)
        after_second_puzzle = datetime.now() - before_puzzle_two

        print(f'The top crate result for CrateMover 9001 is... {solution_second_puzzle}!')
        print(f'{after_second_puzzle.microseconds} µs')


if __name__ == '__main__':
    main()
