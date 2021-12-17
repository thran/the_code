from collections import defaultdict

from parse import parse

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 45
    part_two_test_solution = 112
    
    def preprocess_input(self, lines):
        return tuple(parse('target area: x={:d}..{:d}, y={:d}..{:d}', lines[0]))

    def get_x_speeds(self, x_max, x_min):
        steps_to_speeds = defaultdict(set)
        for x_speed in range(1, x_max + 1):
            dx = x_speed
            x = 0
            steps = 0
            while x <= x_max and dx > 0:
                steps += 1
                x += dx
                dx -= 1
                if x_min <= x <= x_max:
                    steps_to_speeds[steps].add(x_speed)
                    if dx == 0:
                        # all larger steps work with this speed
                        steps_to_speeds[None].add((steps + 1, x_speed))
        return steps_to_speeds

    def find_solutions(self, x_steps_to_speeds, y_min, y_max):
        solutions = set()
        for y_speed in range(y_min - 1, -y_min):
            y = 0
            if y_speed <= 0:
                dy = y_speed
                steps = 0
            else:
                # skip up and down to zero
                dy = -y_speed - 1
                steps = y_speed * 2 + 1
            while y >= y_min:
                steps += 1
                y += dy
                dy -= 1
                if y_min <= y <= y_max:
                    for x_speed in x_steps_to_speeds[steps]:
                        solutions.add((x_speed, y_speed))
                    for min_steps, x_speed in x_steps_to_speeds[None]:
                        if min_steps <= steps:
                            solutions.add((x_speed, y_speed))

        return solutions

    def part_one(self, x_min, x_max, y_min, y_max) -> int:
        y_speed = -y_min - 1
        return y_speed * (y_speed + 1) // 2

    def part_two(self, x_min, x_max, y_min, y_max) -> int:
        solutions = self.find_solutions(self.get_x_speeds(x_max, x_min), y_min, y_max)
        return len(solutions)


Level().run()
