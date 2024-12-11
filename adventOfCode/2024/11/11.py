from functools import cache

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 55312
    part_two_test_solution = 65601038650482

    def preprocess_input(self, lines):
        return list(map(int, lines[0].split()))

    @cache
    def stone_count(self, number, steps) -> int:
        if steps == 0:
            return 1
        if number == 0:
            return self.stone_count(1, steps - 1)
        if len(str(number)) % 2 == 0:
            split = 10 ** (len(str(number)) // 2)
            return self.stone_count(number // split, steps - 1) + self.stone_count(number % split, steps - 1)
        return self.stone_count(number * 2024, steps - 1)

    def part_one(self, stones, steps=25) -> int:
        return sum(self.stone_count(stone, steps) for stone in stones)

    def part_two(self, stones) -> int:
        return self.part_one(stones, 75)


if __name__ == '__main__':
    Level().run()
