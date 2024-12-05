from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 143
    part_two_test_solution = 123

    def preprocess_input(self, lines):
        lines = iter(lines)
        rules = []
        while line := next(lines):
            rules.append(tuple(map(int, line.split('|'))))

        updates = []
        for line in lines:
            updates.append(tuple(map(int, line.split(','))))
        return rules, updates

    def is_valid(self, update, rules) -> bool:
        update = {v: i for i, v in enumerate(update)}
        for a, b in rules:
            if a in update and b in update and update[a] > update[b]:
                return False
        return True

    def fix(self, update, rules) -> list[int]:
        update = set(update)
        rules_to_use = [(a, b) for a, b in rules if a in update and b in update]

        ordered = []
        while len(rules_to_use):
            not_restricted = update - {b for a, b in rules_to_use} - set(ordered)
            assert len(not_restricted) == 1
            not_restricted = tuple(not_restricted)[0]
            ordered.append(not_restricted)
            rules_to_use = [(a, b) for a, b in rules_to_use if a != not_restricted]
        rest = update - set(ordered)
        assert len(rest) == 1

        return ordered

    def part_one(self, rules, updates) -> int:
        result = 0
        for update in updates:
            if self.is_valid(update, rules):
                result += update[len(update) // 2]
        return result

    def part_two(self, rules, updates) -> int:
        result = 0
        for update in updates:
            if not self.is_valid(update, rules):
                result += self.fix(update, rules)[len(update) // 2]
        return result


if __name__ == '__main__':
    Level().run()
