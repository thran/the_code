import numpy as np

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 8
    part_two_test_solution = 2286

    def preprocess_input(self, lines):
        super().preprocess_input(lines)
        games = []
        for line in lines:
            parts = line.split(': ')
            game_numer = int(parts[0].split()[1])
            draws = []
            for draw in parts[1].strip().split(';'):
                cubes = [0] * 3
                for d in draw.split(','):
                    count, color = d.strip().split()
                    if color == 'red':
                        cubes[0] = int(count)
                    elif color == 'green':
                        cubes[1] = int(count)
                    elif color == 'blue':
                        cubes[2] = int(count)
                draws.append(cubes)
            games.append((game_numer, np.array(draws)))
        return games

    def part_one(self, games, maxims=(12, 13, 14)) -> int:
        result = 0
        for game_number, draws in games:
            if all(all(draw[i] <= maxims[i] for i in range(3)) for draw in draws):
                result += game_number
        return result

    def part_two(self, games) -> int:
        return sum(draws.max(axis=0).prod() for game_number, draws in games)


if __name__ == '__main__':
    Level().run()
