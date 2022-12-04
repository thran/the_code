from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 24000
    part_two_test_solution = 45000

    def preprocess_input(self, lines):
        elves = [[]]
        for line in lines:
            if line.isnumeric():
                elves[-1].append(int(line))
            else:
                assert line == ''
                elves.append([])
        return elves

    def part_one(self, elves) -> int:
        return max(sum(elv) for elv in elves)

    def part_two(self, elves) -> int:
        return sum(sorted(sum(elv) for elv in elves)[-3:])


Level().run()
