from collections import defaultdict
from math import ceil

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 1588
    part_two_test_solution = 2188189693529

    def preprocess_input(self, lines):
        lines = list(lines)
        seed = lines[0]
        polymer = defaultdict(int)
        for i in range(len(seed) - 1):
            polymer[seed[i:i+2]] += 1

        rules = {}
        for line in lines[2:]:
            pair, new = line.split(' -> ')
            rules[pair] = new
        return seed, polymer, rules

    def step(self, polymer, rules):
        new_polymer = defaultdict(int)
        for (left, right), count in polymer.items():
            middle = rules[left + right]
            new_polymer[left + middle] += count
            new_polymer[middle + right] += count
        return new_polymer

    def grow(self, polymer, rules, steps):
        for _ in range(steps):
            polymer = self.step(polymer, rules)

        return polymer

    def count_result(self, polymer, seed):
        counts = defaultdict(int)
        for (p1, p2), count in polymer.items():
            counts[p1] += count
            counts[p2] += count
        counts = {p: ceil(c / 2) for p, c in counts.items()}

        return max(counts.values()) - min(counts.values())

    def part_one(self, seed, polymer, rules) -> int:
        polymer = self.grow(polymer, rules, 10)
        return self.count_result(polymer, seed)

    def part_two(self, seed, polymer, rules) -> int:
        polymer = self.grow(polymer, rules, 40)
        return self.count_result(polymer, seed)


Level().run()
