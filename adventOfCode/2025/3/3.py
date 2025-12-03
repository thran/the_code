from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 357
    part_two_test_solution = 3121910778619

    def preprocess_input(self, lines):
        return [list(map(int, line)) for line in lines]

    def joltage(self, bank, size=2):
        joltage = [None] * size
        for i, digit in enumerate(bank):
            for p, j in enumerate(joltage):
                if len(bank) - i < size - p:
                    continue
                if j is None:
                    joltage[p] = digit
                    break
                if digit > j:
                    joltage[p] = digit
                    for k in range(p + 1, size):
                        joltage[k] = None
                    break
        return sum(j * 10 ** (size - i - 1) for i, j in enumerate(joltage))

    def part_one(self, banks) -> int:
        return sum(self.joltage(bank) for bank in banks)

    def part_two(self, banks) -> int:
        return sum(self.joltage(bank, size=12) for bank in banks)


if __name__ == '__main__':
    Level().run()
