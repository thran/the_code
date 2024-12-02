from collections import Counter

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 11
    part_two_test_solution = 31

    def preprocess_input(self, lines):
        list1, list2 = [], []
        for line in lines:
            n1, n2 = line.split()
            list1.append(int(n1))
            list2.append(int(n2))
        return list1, list2

    def part_one(self, list1, list2) -> int:
        return sum(abs(n1 - n2) for n1, n2 in zip(sorted(list1), sorted(list2)))

    def part_two(self, list1, list2) -> int:
        list2 = Counter(list2)
        return sum(n * list2[n] for n in list1)


if __name__ == '__main__':
    Level().run()
