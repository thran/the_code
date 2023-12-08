from core import AdventOfCode
from itertools import cycle
import math


class Level(AdventOfCode):
    part_one_test_solution = 6
    part_two_test_solution = 6
    skip_tests = True

    def preprocess_input(self, lines):
        instructions = lines[0]
        connections = {}
        for line in lines[2:]:
            connections[line[:3]] = (line[7:10], line[12:15])
        return instructions, connections

    def part_one(self, instructions, connections) -> int:
        position = 'AAA'
        for i, instruction in enumerate(cycle(instructions), start=1):
            position = connections[position][0 if instruction == 'L' else 1]
            # ic(i, instruction, state)
            if position == 'ZZZ':
                return i

    def find_cycle(self, position, instructions, connections):
        visited_states = {(position, 0): 0}
        solutions = []
        for i, instruction in enumerate(cycle(instructions), start=1):
            position = connections[position][0 if instruction == 'L' else 1]
            if position[-1] == 'Z':
                solutions.append(i)
            state = (position, i % len(instructions))
            if state in visited_states:
                return solutions, visited_states[state], i - visited_states[state]
            visited_states[state] = i

    def part_two(self, instructions, connections) -> int:
        cycles = []
        for position in connections:
            if position[-1] != 'A':
                continue
            solutions, cycle_start, cycle_length = self.find_cycle(position, instructions, connections)
            assert cycle_start < solutions[0], cycle_start
            assert len(solutions) == 1, solutions
            solution = solutions[0]
            assert solution == cycle_length
            cycles.append(cycle_length)
        return math.lcm(*cycles)


if __name__ == '__main__':
    Level().run()
