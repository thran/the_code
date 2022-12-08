from itertools import product

import numpy as np

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 21
    part_two_test_solution = 8

    def preprocess_input(self, lines):
        return np.array([list(map(int, line)) for line in lines])

    def part_one(self, trees) -> int:
        def process_tree_line(tree_line):
            visible = np.zeros_like(tree_line, dtype=bool)
            from_left, from_right = -1, -1
            for i in range(len(tree_line)):
                if tree_line[i] > from_left:
                    visible[i] = True
                    from_left = tree_line[i]
                if tree_line[-i - 1] > from_right:
                    visible[-i - 1] = True
                    from_right = tree_line[-i - 1]
            return visible

        visible = np.zeros_like(trees, dtype=bool)
        for _ in range(2):
            for i in range(trees.shape[0]):
                visible[i] |= process_tree_line(trees[i])
            trees = trees.TA
            visible = visible.T

        return visible.sum()

    def part_two(self, trees) -> int:
        def get_score(x, y):
            score = 1
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                distance = 1
                visible_trees = 0
                while 0 <= x + dx * distance < trees.shape[0] and 0 <= y + dy * distance < trees.shape[1]:
                    visible_trees += 1
                    if trees[x + dx * distance, y + dy * distance] >= trees[x, y]:
                        break
                    distance += 1
                score *= visible_trees

            return score

        return max(get_score(x, y) for x, y in product(range(trees.shape[0]), range(trees.shape[1])))


Level().run()
