# 1.:    0:11
# 2.:    0:22

from core import AdventOfCode
from permutations import permutations


class Level(AdventOfCode):
    part_one_test_solution = 26
    part_two_test_solution = 61229

    digits = {
        'abcefg': 0,
        'cf': 1,
        'acdeg': 2,
        'acdfg': 3,
        'bcdf': 4,
        'abdfg': 5,
        'abdefg': 6,
        'acf': 7,
        'abcdefg': 8,
        'abcdfg': 9,
    }

    def preprocess_input(self, lines):
        result = []
        for line in lines:
            key, value = line.strip().split(' | ')
            result.append((
                list(map(set, key.split())),
                list(map(set, value.split()))
            ))

        return result

    def part_one(self, lines) -> int:
        count = 0
        for _, numbers in lines:
            for number in numbers:
                if len(number) in {2, 4, 3, 7}:
                    count += 1
        return count

    def convert_digit(self, digit, mapping):
        return ''.join(sorted(map(mapping.get, digit)))


    def find_mapping(self, digits):
        for permutation in permutations(list('abcdefg')):
            mapping = dict(zip('abcdefg', permutation))
            if all(
                self.convert_digit(digit, mapping) in self.digits
                for digit in digits
            ):
                return mapping

    def part_two(self, lines) -> int:
        result = 0
        for key, digits in lines:
            mapping = self.find_mapping(key)
            display = ''
            for digit in digits:
                display += str(self.digits[self.convert_digit(digit, mapping)])
            result += int(display)
        return result


Level().run()
