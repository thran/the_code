from dataclasses import dataclass, field

from core import AdventOfCode
from itertools import pairwise


@dataclass
class Cave:
    filled: set[tuple[int, int]]
    depth: int
    floor: int = None

    def add_floor(self):
        self.floor = self.depth + 2

    def is_empy(self, point):
        return not (point in self.filled or point[1] == self.floor)

    def drop_one(self, x=500, y=0):
        while y <= self.depth or self.floor:
            for new in [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]:
                if self.is_empy(new):
                    x, y = new
                    break
            else:
                break
        else:
            return None
        self.filled.add((x, y))
        return x, y

    def simulate(self):
        walls = len(self.filled)
        while True:
            destination = self.drop_one()
            if destination is None or destination == (500, 0):
                break
        return len(self.filled) - walls


class Level(AdventOfCode):
    part_one_test_solution = 24
    part_two_test_solution = 93

    def preprocess_input(self, lines):

        walls = set()
        for line in lines:
            points = [tuple(map(int, point.split(','))) for point in line.split(' -> ')]
            for points in pairwise(points):
                point1, point2 = sorted(points)
                delta = (0, 1) if point1[0] == point2[0] else (1, 0)

                point = point1
                walls.add(point)
                while point != point2:
                    point = point[0] + delta[0], point[1] + delta[1]
                    walls.add(point)

        return Cave(walls, max(y for _, y in walls))

    def part_one(self, cave) -> int:
        return cave.simulate()

    def part_two(self, cave) -> int:
        cave.add_floor()
        return cave.simulate()


Level().run()
