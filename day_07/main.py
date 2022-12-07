from datetime import datetime
from pathlib import Path
from typing import List


class Node:
    def __init__(self, value: str, parent: 'Node' = None):
        self.value = value
        self.nodes: List[Node] = []
        self.size: int = 0
        self.parent: Node = parent

    def add_node(self, value: str):
        node = Node(value, parent=self)
        self.nodes.append(node)
        return node

    def get_children_sizes(self) -> list:
        return [n.get_node_size() for n in self.nodes]

    def get_node_size(self) -> int:
        if not self.nodes:
            return self.size
        return self.size + sum(self.get_children_sizes())

    def get_children_nodes(self) -> List['Node']:
        nodes = []
        if not self.nodes:
            return []

        for node in self.nodes:
            nodes.append(node)
            nodes.extend(node.get_children_nodes())

        return nodes

    def __str__(self):
        return f'{self.value} - {self.size}'


class CLIParser:
    def __init__(self, log_output: list):
        self.log_output = log_output
        self.tree = None
        self.current_node = None

    def create_tree(self):
        for line in self.log_output:
            match line.split():
                case "$", "cd", "..":
                    self.current_node = self.current_node.parent
                case "$", "cd", directory:
                    if not self.tree:
                        self.tree = Node('/')
                        self.current_node = self.tree
                    else:
                        self.current_node = self.current_node.add_node(directory)
                case "$", _:
                    pass
                case "dir", _:
                    pass
                case size, _:
                    self.current_node.size += int(size)

        return self.tree


def first_puzzle(text: str) -> int:
    tree = CLIParser(text.strip().splitlines()).create_tree()
    sizes = [n.get_node_size() for n in tree.get_children_nodes()]
    return sum(s for s in sizes if s < 100_000)


def second_puzzle(text: str) -> int:
    tree = CLIParser(text.strip().splitlines()).create_tree()
    tree_size = tree.get_node_size()
    sizes = [n.get_node_size() for n in tree.get_children_nodes()]
    sizes.append(tree_size)
    max_available = 70_000_000
    minimum = 30_000_000
    free_space = max_available - tree_size
    minimum_to_delete = minimum - free_space
    return min(s for s in sizes if s > minimum_to_delete)


def main():
    path = Path(__file__).resolve().parent / 'input.txt'
    with open(path) as f:
        text_input = f.read()

        before_puzzle_one = datetime.now()
        solution_first_puzzle = first_puzzle(text_input)
        after_puzzle_one = datetime.now() - before_puzzle_one

        print(f'The sum of all directories with at least 100.000 bytes is... {solution_first_puzzle}!')
        print(f'{after_puzzle_one.microseconds} µs')

        before_puzzle_two = datetime.now()
        solution_second_puzzle = second_puzzle(text_input)
        after_second_puzzle = datetime.now() - before_puzzle_two

        print(f'The total size to delete to allow the update is... {solution_second_puzzle}!')
        print(f'{after_second_puzzle.microseconds} µs')


if __name__ == '__main__':
    main()
