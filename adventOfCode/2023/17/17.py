import numpy as np

from adventOfCode.utils import PrioritySearch, array, SmartArray
from core import AdventOfCode


class PathSearch(PrioritySearch):
    """state: heat, position, direction, steps in line"""

    TURNS = {'r': 'ud', 'l': 'ud', 'u': 'lr', 'd': 'lr'}
    DELTAS = {'r': (0, 1), 'l': (0, -1), 'd': (1, 0), 'u': (-1, 0)}

    def __init__(self, city, init_states, min_steps=0, max_steps=3):
        super().__init__(init_states)
        self.city: SmartArray = city
        self.end_position = (self.city.shape[0] - 1, self.city.shape[1] - 1)
        self.min_steps = min_steps
        self.max_steps = max_steps

    def next_states(self, state):
        heat, position, direction, steps = state

        if direction == '':
            directions = 'rd'
        else:
            directions = ''
            if steps >= self.min_steps:
                directions += self.TURNS[direction]
            if steps < self.max_steps:
                directions += direction

        for new_direction in directions:
            new_position = self.city.change_position(position, self.DELTAS[new_direction])
            if self.city.is_valid_position(new_position):
                yield (
                    heat + self.city[new_position],
                    new_position,
                    new_direction,
                    steps + 1 if direction == new_direction else 1,
                )

    def end_condition(self, state) -> bool:
        return state[1] == self.end_position

    def get_state_hash(self, state):
        return state[1:]


class Level(AdventOfCode):
    part_one_test_solution = 102
    part_two_test_solution = 94

    def preprocess_input(self, lines):
        return array([tuple(map(int, l)) for l in lines])

    def part_one(self, city) -> int:
        search = PathSearch(city, [(0, (0, 0), '', 0)])
        search()
        return search.current_state[0]

    def part_two(self, city) -> int:
        search = PathSearch(city, [(0, (0, 0), '', 0)], min_steps=4, max_steps=10)
        search()
        return search.current_state[0]


if __name__ == '__main__':
    Level().run()
