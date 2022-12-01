from pathlib import Path


def first_puzzle(text: str) -> int:
    elves_calories_str = text.strip().split('\n\n')

    max_calories = 0
    for item in elves_calories_str:
        elf_calories = 0
        calories_per_elf = item.split('\n')

        for calories_value in calories_per_elf:
            elf_calories += int(calories_value)

        if elf_calories > max_calories:
            max_calories = elf_calories

    return max_calories


def second_puzzle(value: str) -> int:
    elves_calories_str = value.strip().split('\n\n')

    elves_calories_values = []

    for item in elves_calories_str:
        elf_calories = 0
        calories_per_elf = item.split('\n')

        for calories_value in calories_per_elf:
            elf_calories += int(calories_value)

        elves_calories_values.append(elf_calories)

    sorted_list = sorted(elves_calories_values, reverse=True)
    return sum(sorted_list[:3])


if __name__ == '__main__':
    path = Path(__file__).resolve().parent / 'input_01.txt'

    with open(path) as f:
        text_input = f.read()
        solution_first_puzzle = first_puzzle(text_input)
        print(f'The elf with most calories is... {solution_first_puzzle} !!')

        solution_second_puzzle = second_puzzle(text_input)
        print(f'The sum of the three elves with most calories carried is... {solution_second_puzzle} !!')
