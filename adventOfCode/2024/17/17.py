from itertools import count

from tqdm import tqdm

from adventOfCode.utils import PrioritySearch, DFS
from core import AdventOfCode


class Program:
    def __init__(self, program, a, b, c):
        self.program = program
        self.a = a
        self.b = b
        self.c = c

        self.pointer = 0
        self.outputs = []

        self.run()

    def run(self):
        while self.pointer < len(self.program):
            opcode, value = self.program[self.pointer], self.program[self.pointer + 1]
            self.pointer += 2
            self.eval_operation(opcode, value)
        return self

    def eval_operation(self, opcode, value):
        match opcode:
            case 0:
                self.a = self.a // 2 ** self.combo(value)
            case 1:
                self.b ^= value
            case 2:
                self.b = self.combo(value) % 8
            case 3:
                if self.a != 0:
                    self.pointer = value
            case 4:
                self.b ^= self.c
            case 5:
                self.outputs.append(self.combo(value) % 8)
            case 6:
                self.b = self.a // 2 ** self.combo(value)
            case 7:
                self.c = self.a // 2 ** self.combo(value)

    def combo(self, value):
        match value:
            case value if value <= 3:
                return value
            case 4:
                return self.a
            case 5:
                return self.b
            case 6:
                return self.c
            case _:
                assert False, f'Invalid combo value {value}'


def list_to_number(numbers):
    return sum(p * 8**i for i, p in enumerate(reversed(numbers)))


class Search(DFS):
    # state = result, to_generate

    def __init__(self, program):
        super().__init__([(tuple(), program)])

        self.program = program
        self.solutions = []

    def next_states(self, state):
        result, to_generate = state
        if not to_generate:
            return
        for candidate in range(8):
            new_result = result + (candidate,)
            outputs = Program(self.program, list_to_number(new_result), 0, 0).outputs
            if outputs[0] == to_generate[-1]:
                yield new_result, to_generate[:-1]

    def on_state_visit(self, state):
        result, to_generate = state
        if len(to_generate) == 0:
            self.solutions.append(result)


class Level(AdventOfCode):
    part_one_test_solution = '5,7,3,0'
    part_two_test_solution = 117440

    def preprocess_input(self, lines):
        program = tuple(map(int, lines[4].split()[-1].split(',')))
        return program, int(lines[0].split()[-1]), int(lines[1].split()[-1]), int(lines[2].split()[-1])

    def part_one(self, program, *registers) -> str:
        return ','.join(map(str, Program(program, *registers).outputs))

    def part_two(self, program, a, *_) -> int:
        if len(program) == 6:
            return list_to_number(program[::-1]) * 8

        search = Search(program)
        search.run()
        result = min(map(list_to_number, search.solutions))
        assert Program(program, result, 0, 0).outputs == list(program)
        return result


if __name__ == '__main__':
    assert Program([2, 6], 0, 0, 9).b == 1
    assert Program([5, 0, 5, 1, 5, 4], 10, 0, 0).outputs == [0, 1, 2]
    assert Program([0, 1, 5, 4, 3, 0], 2024, 0, 0).outputs == [4, 2, 5, 6, 7, 7, 7, 7, 3, 1, 0]
    assert Program([1, 7], 0, 29, 0).b == 26
    assert Program([4, 0], 0, 2024, 43690).b == 44354

    Level().run()
