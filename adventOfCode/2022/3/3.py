from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 157
    part_two_test_solution = 70

    @staticmethod
    def compute_priority(item):
        return ord(item.lower()) - ord('a') + 1 + 26 * item.isupper()

    def part_one(self, lines) -> int:
        priorities = 0
        for backpack in lines:
            backpack_size = len(backpack) // 2
            items = set(backpack[:backpack_size]) & set(backpack[backpack_size:])
            item = list(items)[0]
            priorities += self.compute_priority(item)
        return priorities

    def part_two(self, lines) -> int:
        priorities = 0
        for i in range(0, len(lines), 3):
            items = set(lines[i]) & set(lines[i + 1]) & set(lines[i + 2])
            item = list(items)[0]
            priorities += self.compute_priority(item)
        return priorities


Level().run()
