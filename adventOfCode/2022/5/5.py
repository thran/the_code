from core import AdventOfCode
from parse import parse


class Level(AdventOfCode):
    part_one_test_solution = 'CMZ'
    part_two_test_solution = 'MCD'

    strip_lines = False

    def preprocess_input(self, lines):
        crate_lines = []
        while line := lines.pop(0):
            if '[' in line:
                crate_lines.append(line)
            else:
                stacks = {int(s): [] for s in line.split()}

        for crate_line in crate_lines[::-1]:
            for stack_number, stack in stacks.items():
                positions = 4 * stack_number - 3
                if positions >= len(crate_line):
                    continue
                crate = crate_line[positions]
                if crate != ' ':
                    stack.append(crate)

        instructions = []
        for instruction in lines:
            instructions.append(tuple(parse('move {:d} from {:d} to {:d}', instruction)))

        return stacks, instructions

    @staticmethod
    def get_top_crates(stacks):
        return ''.join(s[-1] for n, s in sorted(stacks.items()))

    def part_one(self, stacks, instructions) -> str:
        for count, from_, to_ in instructions:
            for _ in range(count):
                stacks[to_].append(stacks[from_].pop())

        return self.get_top_crates(stacks)

    def part_two(self, stacks, instructions) -> str:
        for count, from_, to_ in instructions:
            stacks[to_] += stacks[from_][-count:]
            stacks[from_] = stacks[from_][:-count]

        return self.get_top_crates(stacks)


Level().run()
