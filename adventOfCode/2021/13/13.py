import numpy as np
from parse import parse
from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 17
    part_two_test_solution = 0

    def preprocess_input(self, lines):
        dots = []
        instructions = []
        for line in lines:
            if line.startswith('fold along'):
                axis, position = parse('fold along {}={:d}', line)
                instructions.append((axis, position))
            if ',' in line:
                x, y = parse('{:d},{:d}', line)
                dots.append((x, y))

        dots = np.array(dots)
        paper = np.zeros(dots.max(axis=0) + 1, dtype=bool)
        for dot in dots:
            paper[tuple(dot)] = True

        return paper, instructions

    def fold(self, paper, axis, position):
        if axis == 'x':
            half = paper.shape[0] // 2
            part = paper[half + 1:, :]
            return paper[:half, :] | np.flip(part, axis=0)
        else:
            half = paper.shape[1] // 2
            part = paper[:, half + 1:]
            return paper[:, :half] | np.flip(part, axis=1)

    def part_one(self, paper, instructions) -> int:
        axis, position = instructions[0]
        return self.fold(paper, axis, position).sum()

    def part_two(self, paper, instructions) -> int:
        for axis, position in instructions:
            paper = self.fold(paper, axis, position)
        for line in paper.T:
            print(''.join('#' if x else ' ' for x in line))
        return 0


Level().run()
