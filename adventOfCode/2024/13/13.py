from core import AdventOfCode
import parse


class Level(AdventOfCode):
    part_one_test_solution = 480
    part_two_test_solution = 875318608908

    def preprocess_input(self, lines):
        lines = iter(lines)
        machines = []
        while lines:
            machines.append(
                {
                    'a_button': tuple(parse.parse('Button A: X+{:d}, Y+{:d}', next(lines))),
                    'b_button': tuple(parse.parse('Button B: X+{:d}, Y+{:d}', next(lines))),
                    'prize': tuple(parse.parse('Prize: X={:d}, Y={:d}', next(lines))),
                }
            )
            if next(lines, None) is None:
                break

        return machines

    def part_one(self, machines, offset=0) -> int:
        result = 0
        for machine in machines:
            x, y = machine['prize'][0] + offset, machine['prize'][1] + offset
            xa, ya = machine['a_button']
            xb, yb = machine['b_button']
            b_top = y * xa - x * ya
            b_bottom = yb * xa - xb * ya
            if b_top % b_bottom != 0:
                continue
            b = b_top // b_bottom
            if (x - b * xb) % xa != 0:
                continue
            a = (x - b * xb) // xa
            result += 3 * a + b
        return result

    def part_two(self, machines) -> int:
        return self.part_one(machines, 10000000000000)


if __name__ == '__main__':
    Level().run()
