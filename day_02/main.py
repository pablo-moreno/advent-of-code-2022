from datetime import datetime
from pathlib import Path

# A for Rock, B for Paper, and C for Scissors.
# X for Rock, Y for Paper, and Z for Scissors.
shape_mappings = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C',
}

# Rock beats scissors, paper beats rock, scissors beat paper
shape_beats = {
    'A': 'C',
    'B': 'A',
    'C': 'B',
}

score_mappings = {
    'win': 6,
    'draw': 3,
    'lose': 0,
}

shape_beats_reverse = {v: k for k, v in shape_beats.items()}


# 1 for Rock, 2 for Paper, and 3 for Scissors
shape_values = {
    'A': 1,
    'B': 2,
    'C': 3,
}


def first_puzzle(text: str) -> int:
    score = 0
    plays = text.strip().splitlines()

    for play in plays:
        opponent, me = play.split(' ')
        me = shape_mappings.get(me)

        if opponent == me:
            score += score_mappings.get('draw')
            score += shape_values.get(me)
            continue

        if shape_beats.get(opponent) != me:
            score += score_mappings.get('win')

        score += shape_values.get(me)

    return score


def second_puzzle(text: str) -> int:
    score = 0
    plays = text.strip().splitlines()

    for play in plays:
        opponent, result = play.split(' ')

        if result == 'X':
            score += score_mappings.get('lose')
            score += shape_values.get(shape_beats.get(opponent))

        elif result == 'Y':
            score += score_mappings.get('draw')
            score += shape_values.get(opponent)

        elif result == 'Z':
            score += score_mappings.get('win')
            score += shape_values.get(shape_beats_reverse.get(opponent))

    return score


def main():
    path = Path(__file__).resolve().parent / 'input.txt'
    with open(path) as f:
        text_input = f.read()

        before_puzzle_one = datetime.now()
        solution_first_puzzle = first_puzzle(text_input)
        after_puzzle_one = datetime.now() - before_puzzle_one

        print(f'Your final result in the rock, scissors tournament for strategy #1 is... {solution_first_puzzle}!')
        print(f'{after_puzzle_one.microseconds}  µs')

        before_puzzle_two = datetime.now()
        solution_second_puzzle = second_puzzle(text_input)
        after_second_puzzle = datetime.now() - before_puzzle_two

        print(f'Your final result in the rock, scissors tournament for strategy #2 is... {solution_second_puzzle}!')
        print(f'{after_second_puzzle.microseconds} µs')


if __name__ == '__main__':
    main()
