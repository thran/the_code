# start 9:02, 1. 9:17, 2. 9:28
from pathlib import Path

from interpreter import Interpreter

with Path('input.txt').open() as file:
    interpreter = Interpreter(file.readlines())

interpreter.run()
print(interpreter.accumulator)


instructions = interpreter.instructions

for i, (operation, argument) in enumerate(instructions):
    if operation == 'acc':
        continue

    instructions[i] = 'nop' if operation == 'jmp' else 'jmp', argument
    interpreter = Interpreter(instructions)
    if interpreter.run():
        print(interpreter.accumulator)
    instructions[i] = operation, argument
