import numpy as np
import os

from intcode import IntCode


class Arcade:
    def __init__(self):
        memory = list(map(int, open('input.txt').readlines()[0].split(',')))
        self.arcade = IntCode(memory)
        self.field = np.zeros((44, 21))
        self.score = None
        self.ball_x = None
        self.pad_x = None

    def step(self):
        input = 0
        if self.ball_x and self.ball_x > self.pad_x:
            input = 1
        elif self.ball_x and self.ball_x < self.pad_x:
            input = -1
        output = self.arcade.run(inputs=[input], halt_on_missing_input=True)
        for x, y, o in list(zip(output[::3], output[1::3], output[2::3])):
            if x == -1:
                self.score = o
            else:
                self.field[x, y] = o
                if o == 4:
                    self.ball_x = x
                if o == 3:
                    self.pad_x = x

    def run(self):
        self.step()
        while self.blocks() > 0:
            self.step()
            self.show()

    def show(self):
        for row in self.field.T:
            line = ''
            for o in row:
                if o == 0:
                    line += ' '
                elif o == 1:
                    line += '#'
                elif o == 2:
                    line += '%'
                elif o == 3:
                    line += '_'
                elif o == 4:
                    line += 'o'
            print(line)
        print(f'score: {self.score}')

    def blocks(self):
        return (self.field == 2).sum()

a = Arcade()
a.run()
