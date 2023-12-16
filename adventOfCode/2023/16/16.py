from adventOfCode.utils import Search, array
from core import AdventOfCode


class BeamSearch(Search):
    DIRECTIONS = {
        'r': (0, 1),
        'l': (0, -1),
        'd': (1, 0),
        'u': (-1, 0),
    }

    REFLECTIONS = {
        'r': {'|': 'ud', '/': 'u', '\\': 'd'},
        'l': {'|': 'ud', '/': 'd', '\\': 'u'},
        'd': {'-': 'rl', '/': 'l', '\\': 'r'},
        'u': {'-': 'rl', '/': 'r', '\\': 'l'},
    }

    def __init__(self, contraption, init_states, **kwargs):
        super().__init__(init_states, **kwargs)
        self.contraption = contraption

    def next_states(self, state):
        position, direction = state
        for new_direction in self.REFLECTIONS[direction].get(self.contraption[position], direction):
            new_position = self.contraption.change_position(position, self.DIRECTIONS[new_direction])
            if self.contraption.is_valid_position(new_position):
                yield new_position, new_direction


class Level(AdventOfCode):
    part_one_test_solution = 46
    part_two_test_solution = 51

    def preprocess_input(self, lines):
        return array([list(l) for l in lines])

    def solve(self, contraption, xy, direction):
        search = BeamSearch(contraption, {(xy, direction)}, type_='BFS')
        search()
        return len({xy for xy, d in search.visited_states})

    def part_one(self, contraption) -> int:
        return self.solve(contraption, (0, 0), 'r')

    def part_two(self, contraption) -> int:
        solutions = []
        size = contraption.shape[0]
        assert size == contraption.shape[1]
        for i in range(size):
            solutions.append(self.solve(contraption, (0, i), 'd'))
            solutions.append(self.solve(contraption, (size - 1, i), 'u'))
            solutions.append(self.solve(contraption, (i, 0), 'r'))
            solutions.append(self.solve(contraption, (i, size - 1), 'l'))

        return max(solutions)


if __name__ == '__main__':
    Level().run()
