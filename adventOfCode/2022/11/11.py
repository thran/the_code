from math import prod

from core import AdventOfCode
from dataclasses import dataclass


@dataclass
class Monkey:
    items: list[int]
    operation: callable
    divisible: int
    throw: dict[bool, int]
    monkeys: dict[int, 'Monkey']

    inspections: int = 0

    def round(self, divide_by=None, simplify=None):
        for item in self.items:
            new = self.operation(item)
            if divide_by:
                new //= divide_by
            if simplify:
                new %= simplify
            target = self.throw[new % self.divisible == 0]
            self.monkeys[target].items.append(new)
            self.inspections += 1
        self.items = []


class Level(AdventOfCode):
    part_one_test_solution = 10605
    part_two_test_solution = 2713310158

    def preprocess_input(self, lines):
        monkeys = {}
        lines = iter(lines)
        while True:
            number = int(next(lines)[7:-1])
            items = list(map(int, next(lines).split(': ')[1].split(', ')))
            operation = eval('lambda old: ' + next(lines).split(' = ')[1])
            divisible = int(next(lines).split()[-1])
            throw = {True: int(next(lines).split()[-1]), False: int(next(lines).split()[-1])}
            monkeys[number] = Monkey(items, operation, divisible, throw, monkeys)
            if next(lines, -1) == -1:
                break
        return monkeys

    @staticmethod
    def simulate(monkeys, rounds, divide_by):
        lcm = prod(monkey.divisible for monkey in monkeys.values())
        for _ in range(rounds):
            for _, monkey in sorted(monkeys.items()):
                monkey.round(divide_by, lcm)

    @staticmethod
    def get_monkey_business(monkeys):
        inspections = sorted(monkey.inspections for monkey in monkeys.values())
        return inspections[-1] * inspections[-2]

    def part_one(self, monkeys) -> int:
        self.simulate(monkeys, 20, 3)
        return self.get_monkey_business(monkeys)

    def part_two(self, monkeys) -> int:
        self.simulate(monkeys, 10000, None)
        return self.get_monkey_business(monkeys)


Level().run()
