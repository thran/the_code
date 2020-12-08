from parse import parse


class Interpreter:

    def __init__(self, instructions):
        if type(instructions[0]) is str:
            self.instructions = self.parse_instructions(instructions)
        else:
            self.instructions = instructions
        self.position = 0
        self.accumulator = 0

        self.visited_positions = set()

    @staticmethod
    def parse_instructions(lines):
        instructions = []
        for line in lines:
            result = parse('{operation} {argument:d}', line.strip())
            instructions.append((
                result['operation'],
                result['argument']
            ))
        return instructions

    def reset(self):
        self.position = 0
        self.accumulator = 0
        self.visited_positions = set()

    def run(self, reset=False):
        if reset:
            self.reset()
        while True:
            if self.position in self.visited_positions:
                return False
            if self.position == len(self.instructions):
                return True
            self.visited_positions.add(self.position)
            self.step()

    def step(self):
        operation, argument = self.instructions[self.position]
        if operation == 'acc':
            self.accumulator += argument
            self.position += 1
            return

        if operation == 'jmp':
            self.position += argument
            return

        if operation == 'nop':
            self.position += 1
            return
