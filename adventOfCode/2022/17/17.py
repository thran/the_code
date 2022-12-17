from itertools import cycle

import numpy as np

from core import AdventOfCode


class Tower:
    ROCKS = list(
        map(
            np.array,
            [
                [[1, 1, 1, 1]],
                [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
                [[1, 1, 1], [0, 0, 1], [0, 0, 1]],
                [[1], [1], [1], [1]],
                [[1, 1], [1, 1]],
            ],
        )
    )

    def __init__(self, jets):
        self.jets = iter(cycle(enumerate(jets)))
        self.rocks = iter(cycle(self.ROCKS))
        self.chamber = np.zeros((100, 7), bool)
        self.last_jet_number = -1
        self.height = 0

    def valid_position(self, x, y, rock):
        if x < 0 or y < 0:
            return False
        if y + rock.shape[1] > 7:
            return False
        place = self.chamber[x - rock.shape[0] + 1 : x + 1, y : y + rock.shape[1]]
        return not (place & rock).any()

    def place_rock(self, x, y, rock):
        self.chamber[x - rock.shape[0] + 1 : x + 1, y : y + rock.shape[1]] = (
            self.chamber[x - rock.shape[0] + 1 : x + 1, y : y + rock.shape[1]] | rock
        )

    def get_tower_top_hash(self, top_size=100):
        return self.visualize_tower(self.chamber[max(0, self.height - top_size) : self.height])

    def simulate_with_cycle_detection(self, rock_count):
        states = {}
        rock_number = 0
        cycle_count = None
        cycle_height = None
        while rock_number < rock_count:
            self.simulate(1)
            state_hash = (self.get_tower_top_hash(), rock_number % len(self.ROCKS), self.last_jet_number)
            if cycle_height is None and state_hash in states:
                cycle_size = rock_number - states[state_hash][0]
                cycle_height = self.height - states[state_hash][1]
                cycle_count = (rock_count - rock_number - 1) // cycle_size
                rock_number += cycle_count * cycle_size
            else:
                states[state_hash] = (rock_number, self.height)
            rock_number += 1
        return self.height + cycle_height * cycle_count

    def simulate(self, rock_count):
        for _ in range(rock_count):
            rock = next(self.rocks)
            rock_y = 2
            rock_x = self.height + 3 + rock.shape[0] - 1
            if rock_x >= self.chamber.shape[0]:
                self.chamber = np.concatenate([self.chamber, np.zeros_like(self.chamber)])
            while True:
                self.last_jet_number, jet = next(self.jets)
                if jet == '>' and self.valid_position(rock_x, rock_y + 1, rock):
                    rock_y += 1
                if jet == '<' and self.valid_position(rock_x, rock_y - 1, rock):
                    rock_y -= 1
                if self.valid_position(rock_x - 1, rock_y, rock):
                    rock_x -= 1
                else:
                    self.place_rock(rock_x, rock_y, rock)
                    self.height = max(self.height, rock_x + 1)
                    break
        return self.height

    @staticmethod
    def visualize_tower(chamber):
        result = ''
        for row in chamber[::-1]:
            result += ''.join('#' if c else '.' for c in row) + '\n'
        return result.strip()

    def show(self):
        print(self.visualize_tower(self.chamber[: self.height]))


class Level(AdventOfCode):
    part_one_test_solution = 3068
    part_two_test_solution = 1514285714288

    def part_one(self, jets) -> int:
        tower = Tower(jets)
        return tower.simulate(2022)

    def part_two(self, jets) -> int:
        tower = Tower(jets)
        return tower.simulate_with_cycle_detection(1000000000000)


Level().run()
