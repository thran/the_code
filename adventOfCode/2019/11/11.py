from intcode import IntCode


class Robot:
    def __init__(self):
        memory = list(map(int, open('input.txt').readlines()[0].split(',')))
        self.program = IntCode(memory)
        self.direction = 0
        self.x, self.y = 0, 0
        self.colors = {(0, 0): 1}

    def run(self):
        while True:
            color = self.program.run(inputs=[self.colors[(self.x, self.y)]], halt_on_output=True)
            if color is None:
                break
            rotation = self.program.run(inputs=[], halt_on_output=True)
            self.colors[(self.x, self.y)] = color
            if rotation == 0:
                self.direction = (self.direction - 1) % 4
            else:
                self.direction = (self.direction + 1) % 4
            self.move()

    def move(self):
        if self.direction == 0:
            self.y -= 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y += 1
        elif self.direction == 3:
            self.x -= 1
        else:
            assert False, 'invalid direction'
        if (self.x, self.y) not in self.colors:
            self.colors[(self.x, self.y)] = 0

    def show(self):
        xs = [i for i, j in self.colors.keys()]
        ys = [j for i, j in self.colors.keys()]
        for y in range(min(ys), max(ys) + 1):
            row = ''
            for x in range(min(xs), max(xs) + 1):
                if x == self.x and y == self.y:
                    if self.direction == 0:
                        row += '^'
                    elif self.direction == 1:
                        row += '>'
                    elif self.direction == 2:
                        row += 'v'
                    elif self.direction == 3:
                        row += '<'
                else:
                    row += '.' if self.colors.get((x, y), 0) == 0 else '#'
            print(row)


robot = Robot()
robot.run()
robot.show()
print(len(robot.colors))
