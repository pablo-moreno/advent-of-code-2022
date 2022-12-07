import unittest

from day_07.main import first_puzzle, second_puzzle, Node

text_input = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""


class TestDay07(unittest.TestCase):

    def test_tree_size(self):
        tree = Node('/')
        node_a = tree.add_node('a')
        node_a.size = 400

        node_b = tree.add_node('b')
        node_b.size = 200

        node_c = node_a.add_node('c')
        node_c.size = 100

        node_d = node_b.add_node('d')
        node_d.size = 800

        assert node_a.get_node_size() == 500
        assert node_b.get_node_size() == 1000
        assert len(tree.get_children_nodes()) == 4

    def test_total_size_of_dirs_smaller_than_100000(self):
        assert first_puzzle(text_input) == 95437

    def test_total_size_of_dir_to_delete_to_allow_update(self):
        assert second_puzzle(text_input) == 24933642
