import numpy as np

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 13140
    part_two_test_solution = '?'

    def preprocess_input(self, lines):
        instructions = []
        for line in lines:
            match line.split():
                case 'noop',:
                    instructions.append(('noop',))
                case instruction, value if instruction.startswith('add'):
                    instructions.append(('add', instruction[3:], int(value)))

        return instructions

    def run_cpu(self, instructions):
        x = 1
        for instruction in instructions:
            match instruction:
                case 'noop',:
                    yield x
                case 'add', 'x', value:
                    yield x
                    yield x
                    x += value

    def part_one(self, instructions) -> int:
        signal_strengths = []
        for i, x in enumerate(self.run_cpu(instructions), start=1):
            if i % 40 == 20:
                signal_strengths.append(x * i)
        return sum(signal_strengths)

    def part_two(self, instructions) -> str:
        display = np.empty((6, 40), dtype=str)
        for i, x in enumerate(self.run_cpu(instructions)):
            display[i // 40, i % 40] = '#' if x - 1 <= i % 40 <= x + 1 else ' '

        for line in display:
            print(''.join(line))
        print()

        return '?'


Level().run()
