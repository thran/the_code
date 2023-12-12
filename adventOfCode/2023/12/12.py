from functools import cache

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 21
    part_two_test_solution = 525152

    def preprocess_input(self, lines):
        records = []
        for line in lines:
            springs, counts = line.split()
            records.append((tuple(springs), tuple(map(int, counts.split(',')))))
        return records

    @cache
    def count_solutions(self, springs, counts):
        for i, spring in enumerate(springs):
            if spring == '.':
                continue
            if spring == '#':
                if len(counts) == 0:
                    return 0
                count = counts[0]
                for j in range(i, i + count):
                    if j >= len(springs) or springs[j] == '.':
                        return 0
                if i + count < len(springs) and springs[i + count] == '#':
                    return 0
                return self.count_solutions(springs[i + count + 1 :], counts[1:])

            return (self.count_solutions(springs[i + 1:], counts)
                  + self.count_solutions(('#',) + springs[i + 1:], counts))  # fmt: skip
        return 1 if len(counts) == 0 else 0

    def part_one(self, records) -> int:
        return sum(self.count_solutions(springs, counts) for springs, counts in records)

    def part_two(self, records) -> int:
        return self.part_one([(((r + ('?',)) * 5)[:-1], c * 5) for r, c in records])


if __name__ == '__main__':
    Level().run()
