from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 3
    part_two_test_solution = 6

    def preprocess_input(self, lines):
        return [(1 if line[0] == 'R' else -1, int(line[1:])) for line in lines]

    def part_one(self, instructions, position=50, size=100, part_two=False) -> int:
        zeros = 0
        for orientation, steps in instructions:
            position += orientation * steps
            position %= size
            if not part_two:
                if position == 0:
                    zeros += 1
            else:
                zeros += abs(steps // size)
                previous_position_raw = position - orientation * (steps % 100)
                if previous_position_raw > 100 or previous_position_raw < 0 or position == 0:
                    zeros += 1
        return zeros

    def part_two(self, instructions) -> int:
        return self.part_one(instructions, part_two=True)


if __name__ == '__main__':
    Level().run()
