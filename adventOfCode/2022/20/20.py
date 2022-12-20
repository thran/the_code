from dataclasses import dataclass

from core import AdventOfCode


@dataclass
class Number:
    value: int
    cycle_size: int
    next: 'Number' = None
    prev: 'Number' = None

    def move(self):
        if self.value % (self.cycle_size - 1) == 0:
            return

        left = self.n_next(self.value)
        right = left.next

        self.prev.next = self.next
        self.next.prev = self.prev

        left.next = self
        self.prev = left
        right.prev = self
        self.next = right

    def n_next(self, steps, with_itself=False):
        n = self
        correction = 0 if with_itself else -1
        for _ in range(steps % (self.cycle_size + correction)):
            n = n.next
        return n


class NumberCycle:
    def __init__(self, numbers):
        cycle_size = len(numbers)
        self.numbers = numbers
        self.first = last = Number(numbers[0], cycle_size)
        self.by_positions: list[Number] = [self.first]

        for n in numbers[1:]:
            no = Number(n, cycle_size, prev=last)
            self.by_positions.append(no)
            last.next = no
            last = no
            if n == 0:
                self.zero = no

        last.next = self.first
        self.first.prev = last

    def move_numbers(self):
        for number in self.by_positions:
            number.move()

    def get_solution(self):
        n = self.zero
        results = []
        for i in range(3):
            n = n.n_next(1000, with_itself=True)
            results.append(n.value)
        return sum(results)


class Level(AdventOfCode):
    part_one_test_solution = 3
    part_two_test_solution = 1623178306

    def part_one(self, numbers) -> int:
        nc = NumberCycle(numbers)
        nc.move_numbers()
        return nc.get_solution()

    def part_two(self, numbers) -> int:
        nc = NumberCycle([n * 811589153 for n in numbers])
        for _ in range(10):
            nc.move_numbers()
        return nc.get_solution()


Level().run()
