import numpy as np

from adventOfCode.utils import BFS, SmartArray, array
from core import AdventOfCode


class Search(BFS):
    # state = steps, position

    def __init__(self, bytes, size):
        super().__init__([(0, (0, 0))])

        self.memory: SmartArray = array(np.zeros((size, size), dtype=bool))
        for b in bytes:
            self.memory[tuple(b)] = True
        self.end = (size - 1, size - 1)
        self.visited_positions = set()
        self.solution = None

    def next_states(self, state):
        steps, position = state
        if position in self.visited_positions:
            return
        self.visited_positions.add(position)
        for candidate in self.memory.direct_neighbors(position):
            if not self.memory[candidate]:
                yield steps + 1, candidate

    def end_condition(self, state) -> bool:
        if state[1] == self.end:
            self.solution = state[0]
            return True
        return False


class Level(AdventOfCode):
    part_one_test_solution = 22
    part_two_test_solution = '6,1'

    def preprocess_input(self, lines):
        bytes = np.array([tuple(map(int, l.split(','))) for l in lines])
        size = bytes.max() + 1
        return bytes, size, 12 if size == 7 else 1024

    def part_one(self, bytes, size, time) -> int:
        return Search(bytes[:time], size)().solution

    def part_two(self, bytes, size, time) -> str:
        lower, upper = time, len(bytes)
        while lower + 1 < upper:
            mid = (lower + upper) // 2
            if Search(bytes[:mid], size)().solution is None:
                upper = mid
            else:
                lower = mid
        return ','.join(map(str, bytes[upper - 1]))


if __name__ == '__main__':
    Level().run()
