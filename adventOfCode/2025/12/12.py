import numpy as np

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 2
    part_two_test_solution = None
    skip_tests = True

    def preprocess_input(self, lines):
        shapes = []
        for i in range(6):
            assert lines[i * 5] == f'{i}:'
            shapes.append(np.array([[int(c == '#') for c in line] for line in lines[i * 5 + 1 : i * 5 + 4]]))

        regions = []
        for line in lines[30:]:
            size, counts = line.split(': ')
            regions.append((tuple(map(int, size.split('x'))), np.array(tuple(map(int, counts.split())))))
        return shapes, regions

    def part_one(self, shapes, regions) -> int:
        shape_sizes = np.array([s.sum() for s in shapes])
        count = 0
        for size, counts in regions:
            if (counts * shape_sizes).sum() > np.prod(size):
                ...
            elif (size[0] // 3) * (size[1] // 3) >= sum(counts):
                count += 1
            else:
                assert False

        return count

    def part_two(self, shapes, regions) -> int:
        ...


if __name__ == '__main__':
    Level().run()
