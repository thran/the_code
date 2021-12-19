from math import floor, ceil
from operator import attrgetter

from core import AdventOfCode

class Number:

    def __init__(self, source, parent=None):
        self.parent = parent

        if type(source) is int:
            self.value = source
            self.left, self.right = None, None
        else:
            self.value = None
            self.left, self.right = source
            if type(self.left) is not Number:
                self.left = Number(self.left, self)
            if type(self.right) is not Number:
                self.right = Number(self.right, self)

    @property
    def is_value(self):
        return self.value is not None

    def _value_generator(self):
        if self.is_value:
            yield self
            return
        yield from self.left._value_generator()
        yield from self.right._value_generator()

    @property
    def value_list(self):
        """ list of leaf values in order """
        return list(self._value_generator())

    @property
    def root(self):
        current = self
        while current.parent:
            current = current.parent
        return current

    def reduce(self):
        while True:
            if to_explode := self.find_pair_to_explode():
                to_explode.explode()
                continue
            if not self.find_and_split():
                break

    def find_and_split(self):
        if self.is_value:
            if self.value <= 9:
                return False
            new = Number([floor(self.value / 2), ceil(self.value / 2)], parent=self.parent)
            if self.parent.left == self:
                self.parent.left = new
            else:
                self.parent.right = new
            return True

        return self.left.find_and_split() or self.right.find_and_split()

    def find_pair_to_explode(self, current_depth=0):
        if self.is_value:
            return None
        if current_depth == 4 and not self.is_value:
            return self

        from_left = self.left.find_pair_to_explode(current_depth + 1)
        if from_left is not None:
            return from_left
        return self.right.find_pair_to_explode(current_depth + 1)

    def explode(self):
        new = Number(0, parent=self.parent)
        if self.parent.left == self:
            self.parent.left = new
        else:
            self.parent.right = new

        values = self.root.value_list
        position = values.index(new)
        if position > 0:
            values[position - 1].value += self.left.value
        if position < len(values) - 1:
            values[position + 1].value += self.right.value

    def __add__(self, other):
        number = Number([self, other])
        self.parent = number
        other.parent = number
        number.reduce()
        return number

    def __str__(self):
        if self.is_value:
            return f'{self.value}'
        return f'[{self.left},{self.right}]'

    def __repr__(self):
        return str(self)

    @property
    def magnitude(self):
        if self.is_value:
            return self.value

        return self.left.magnitude * 3 + self.right.magnitude * 2


class Level(AdventOfCode):
    part_one_test_solution = 4140
    part_two_test_solution = 3993

    def preprocess_input(self, lines):
        numbers = []
        for line in lines:
            numbers.append(eval(line))
        return numbers

    def part_one(self, numbers) -> int:
        numbers = [Number(n) for n in numbers]
        s = sum(numbers[1:], start=numbers[0])
        return s.magnitude

    def part_two(self, numbers) -> int:
        max_magnitude = 0
        for number1 in numbers:
            for number2 in numbers:
                if number1 == number2:
                    continue
                max_magnitude = max(max_magnitude, (Number(number1) + Number(number2)).magnitude)
        return max_magnitude


Level().run()
