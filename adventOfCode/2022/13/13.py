from functools import cmp_to_key

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 13
    part_two_test_solution = 140

    def preprocess_input(self, lines):
        pairs = []
        lines = iter(lines)

        while True:
            pairs.append((eval(next(lines)), eval(next(lines))))
            if next(lines, True):
                break

        return pairs

    # 0 - equal, negative - correct order, positive - wrong order
    def compare(self, left, right) -> int:
        if type(left) is int and type(right) is int:
            return left - right

        if type(left) is list and type(right) is list:
            for le, re in zip(left, right):
                c = self.compare(le, re)
                if c != 0:
                    return c
            return len(left) - len(right)

        if type(left) is int:
            return self.compare([left], right)
        else:
            return self.compare(left, [right])

    def part_one(self, pairs) -> int:
        return sum(i for i, (left, right) in enumerate(pairs, start=1) if self.compare(left, right) < 0)

    def part_two(self, pairs) -> int:
        extra_packets = [[[2]], [[6]]]
        packets = sorted([p for pair in pairs for p in pair] + extra_packets, key=cmp_to_key(self.compare))

        decoder_key = 1
        for extra_packet in extra_packets:
            decoder_key *= packets.index(extra_packet) + 1

        return decoder_key


Level().run()
