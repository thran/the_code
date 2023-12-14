import numpy as np

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 136
    part_two_test_solution = 64

    def preprocess_input(self, lines: list[str]):
        platform = []
        for line in lines:
            platform.append(tuple(line))
        return np.array(platform)

    @staticmethod
    def roll_row(row):
        def roll_part(part):
            return ''.join(sorted(part, reverse=True))

        return '#'.join(map(roll_part, ''.join(row).split('#')))

    def roll(self, platform, direction):
        if direction == 'north':
            return np.array([tuple(self.roll_row(column)) for column in platform.T]).T
        if direction == 'south':
            return self.roll(platform[::-1], 'north')[::-1]
        elif direction == 'east':
            return self.roll(platform.T, 'south').T
        elif direction == 'west':
            return self.roll(platform.T, 'north').T

    def get_weights(self, platform):
        return np.tile(np.arange(len(platform), 0, -1), platform.shape[1]).reshape(platform.shape).T

    def part_one(self, platform) -> int:
        platform = self.roll(platform, 'north')
        return (self.get_weights(platform) * (platform == 'O')).sum()

    def part_two(self, platform) -> int:
        visited_states = {}
        cycle = 0
        while cycle < 1000000000:
            for direction in ['north', 'west', 'south', 'east']:
                platform = self.roll(platform, direction)
            cycle += 1
            state = ''.join(platform.flatten())
            if state in visited_states:
                cycle_length = cycle - visited_states[state]
                cycle += (1000000000 - cycle) // cycle_length * cycle_length
            visited_states[state] = cycle
        return (self.get_weights(platform) * (platform == 'O')).sum()


if __name__ == '__main__':
    Level().run()
