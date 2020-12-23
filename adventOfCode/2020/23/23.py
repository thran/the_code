# start 8:36, 1. 9:06, 2. 9:16
from itertools import chain
from pathlib import Path


class Cups:
    def __init__(self, cups):
        self.next = {}
        self.max = 0

        self.current = None
        last = None
        for cup in cups:
            self.max = max(self.max, cup)
            if last is None:
                self.current = cup
            else:
                self.next[last] = cup
            last = cup
        self.next[cup] = self.current

    def __str__(self):
        r = f'( {self.current} )'
        cup = self.current
        while (cup := self.next[cup]) != self.current:
            r += f' {cup} '
        return r

    def take(self, n=3):
        cup = self.current
        taken = []
        for i in range(n):
            cup = self.next[cup]
            taken.append(cup)
        self.next[self.current] = self.next[cup]
        return taken

    def place(self, destination, cups):
        self.next[cups[-1]] = self.next[destination]
        self.next[destination] = cups[0]

    def decrease(self, cup):
        cup -= 1
        if cup == 0:
            cup = self.max
        return cup

    def move(self):
        taken = self.take()
        destination = self.current
        while (destination := self.decrease(destination)) in taken:
            pass
        self.place(destination, taken)
        self.current = self.next[self.current]

    def play(self, moves):
        for _ in range(moves):
            self.move()

    def result(self):
        r = ''
        cup = 1
        while (cup := self.next[cup]) != 1:
            r += str(cup)
        return r

    def result2(self):
        return self.next[1] * self.next[self.next[1]]


with Path('input.txt').open() as file:
    input_cups = list(map(int, file.readline().strip()))

cups = Cups(input_cups)
cups.play(100)
print(cups.result())

cups = Cups(chain(input_cups, range(10, 10 ** 6 + 1)))
cups.play(10 ** 7)
print(cups.result2())
