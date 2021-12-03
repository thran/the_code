# start: 9:32
# 1.:    9:45 - Bára
# 2.:   10:14 - Bára

from collections import defaultdict

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 198
    part_two_test_solution = 230

    def preprocess_input(self, lines):
        return[int(line, 2) for line in lines]


    def part_one(self, numbers) -> int:
        bit = 0
        gamma = 0
        epsilon = 0
        while True:
            bit_counts = defaultdict(int)
            for number in numbers:
                bit_counts[int(number & 2 ** bit > 0)] += 1
            if bit_counts[1] == 0:
                break
            if bit_counts[1] > bit_counts[0]:
                gamma += 2 ** bit
            else:
                epsilon += 2 ** bit
            bit += 1

        return gamma * epsilon

    def filter_numbers_once(self, numbers, bit, co2=False):
        bit_counts = defaultdict(list)
        for number in numbers:
            bit_counts[number & 2 ** bit > 0].append(number)
        ones = len(bit_counts[True])
        zeros = len(bit_counts[False])
        if ones >= zeros:
            return bit_counts[not co2]
        else:
            return bit_counts[co2]

    def filter_numbers(self, numbers, co2=False):
        bit = len(bin(max(numbers))) - 3
        while len(numbers) != 1:
            numbers = self.filter_numbers_once(numbers, bit, co2)
            bit -= 1
        return numbers[0]

    def part_two(self, numbers) -> int:
        oxygen = self.filter_numbers(numbers)
        co2 = self.filter_numbers(numbers, True)

        return oxygen * co2

Level().run()
