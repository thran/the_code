from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 3
    part_two_test_solution = 14

    def preprocess_input(self, lines):
        fresh_ranges = set()
        ingredients = None
        for line in lines:
            if not line:
                ingredients = []
                continue
            if ingredients is None:
                fresh_ranges.add(tuple(map(int, line.split('-'))))
            else:
                ingredients.append(int(line))
        return ingredients, fresh_ranges

    def part_one(self, ingredients, fresh_ranges) -> int:
        return sum(any(s <= ingredient <= e for s, e in fresh_ranges) for ingredient in ingredients)

    def find_intersecting_ranges(self, ranges):
        for range1 in ranges:
            for range2 in ranges:
                if range1 == range2:
                    continue
                if range1[0] <= range2[0] <= range1[1] or range1[0] <= range2[1] <= range1[1]:
                    return range1, range2
        return None

    def part_two(self, _, fresh_ranges: set) -> int:
        while pair_to_join := self.find_intersecting_ranges(fresh_ranges):
            range1, range2 = pair_to_join
            fresh_ranges.remove(range1)
            fresh_ranges.remove(range2)
            fresh_ranges.add(
                (
                    min(range1[0], range2[0]),
                    max(range1[1], range2[1]),
                )
            )
        return sum(e - s + 1 for s, e in fresh_ranges)


if __name__ == '__main__':
    Level().run()
