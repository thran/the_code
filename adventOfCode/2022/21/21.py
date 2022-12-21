from dataclasses import dataclass
from functools import cache

from core import AdventOfCode


@dataclass
class Monkey:
    name: str
    monkeys: dict[str, 'Monkey']
    number: int = None
    operand1: str = None
    operation: str = None
    operand2: str = None

    def get_value(self):
        if self.number is None:
            op1 = self.op1_monkey.get_value()
            op2 = self.op2_monkey.get_value()
            match self.operation:
                case '+':
                    self.number = op1 + op2
                case '*':
                    self.number = op1 * op2
                case '/':
                    self.number = int(op1 / op2)
                case '-':
                    self.number = op1 - op2

        return self.number

    def find_value(self, monkey, requested_result):
        if self.name == monkey:
            return requested_result

        match self.operation:
            case '+':
                if self.op1_monkey.count_dependencies(monkey):
                    return self.op1_monkey.find_value(monkey, requested_result - self.op2_monkey.get_value())
                else:
                    return self.op2_monkey.find_value(monkey, requested_result - self.op1_monkey.get_value())
            case '*':
                if self.op1_monkey.count_dependencies(monkey):
                    return self.op1_monkey.find_value(monkey, int(requested_result / self.op2_monkey.get_value()))
                else:
                    return self.op2_monkey.find_value(monkey, int(requested_result / self.op1_monkey.get_value()))
            case '/':
                if self.op1_monkey.count_dependencies(monkey):
                    return self.op1_monkey.find_value(monkey, requested_result * self.op2_monkey.get_value())
                else:
                    return self.op2_monkey.find_value(monkey, self.op1_monkey.get_value() / requested_result)
            case '-':
                if self.op1_monkey.count_dependencies(monkey):
                    return self.op1_monkey.find_value(monkey, requested_result + self.op2_monkey.get_value())
                else:
                    return self.op2_monkey.find_value(monkey, self.op1_monkey.get_value() - requested_result)

    @cache
    def count_dependencies(self, monkey):
        if self.number is not None:
            return 1 if self.name == monkey else 0
        return self.op1_monkey.count_dependencies(monkey) + self.op2_monkey.count_dependencies(monkey)

    @property
    def op1_monkey(self):
        return self.monkeys[self.operand1]

    @property
    def op2_monkey(self):
        return self.monkeys[self.operand2]

    def __hash__(self):
        return self.name.__hash__()


class Level(AdventOfCode):
    part_one_test_solution = 152
    part_two_test_solution = 301

    def preprocess_input(self, lines):
        monkeys = {}
        for line in lines:
            monkey, shout = line.split(': ')
            if shout.isnumeric():
                monkeys[monkey] = Monkey(monkey, monkeys, int(shout))
            else:
                monkeys[monkey] = Monkey(monkey, monkeys, None, *shout.split(' '))

        return monkeys

    def part_one(self, monkeys: dict[str, Monkey]) -> int:
        return monkeys['root'].get_value()

    def part_two(self, monkeys: dict[str, Monkey]) -> int:
        assert monkeys['root'].count_dependencies('humn') == 1
        left = monkeys['root'].op1_monkey
        right = monkeys['root'].op2_monkey

        unknown, known = (left, right.get_value()) if left.count_dependencies('humn') else (right, left.get_value())
        return unknown.find_value('humn', known)


Level().run()
