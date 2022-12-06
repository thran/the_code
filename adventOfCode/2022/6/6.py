from collections import Counter

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 11
    part_two_test_solution = 26

    @staticmethod
    def find_marker(signal, size):
        buffer = Counter()
        for i, char in enumerate(signal, start=1):
            buffer[char] += 1
            if i < size:
                continue
            if i > size:
                buffer[signal[i - size - 1]] -= 1
            if max(buffer.values()) == 1:
                return i

    def part_one(self, signal) -> int:
        return self.find_marker(signal, 4)

    def part_two(self, signal) -> int:
        return self.find_marker(signal, 14)


Level().run()
