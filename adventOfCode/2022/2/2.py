from itertools import starmap

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 15
    part_two_test_solution = 12

    def preprocess_input(self, lines):
        rounds = []
        for line in lines:
            opponent, you = line.split()
            rounds.append((
                ord(opponent) - ord('A'),
                ord(you) - ord('X'),
            ))
        return rounds

    # 0 - rock, 1 - paper, 2 - scissors
    # result: 0 - lost, 1 - draw, 2 - win

    def part_one(self, rounds) -> int:
        def get_score(opponent, you):
            result = (you - opponent + 1) % 3
            return result * 3 + you + 1

        return sum(starmap(get_score, rounds))

    def part_two(self, rounds) -> int:
        def get_score(opponent, result):
            you = (opponent + (result - 1)) % 3
            return result * 3 + you + 1

        return sum(starmap(get_score, rounds))


Level().run()
