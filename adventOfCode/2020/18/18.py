# start 8:55, 1. 9:19, 2. 9:32
from math import prod
from pathlib import Path

with Path('input.txt').open() as file:
    expressions = [[int(c) if c.isdigit() else c for c in line.strip() if c != ' '] for line in file]


def find_start(sequence):
    assert sequence[-1] == ')'
    diff = 1
    for di, c in enumerate(sequence[:-1][::-1]):
        if c == ')':
            diff += 1
        if c == '(':
            diff -= 1
            assert diff >= 0
        if diff == 0:
            start = len(sequence) - di - 2
            assert sequence[start] == '('
            return start
    assert False


def eval_expression(sequence) -> int:
    last = sequence[-1]
    if len(sequence) == 1:
        assert type(last) is int
        return last

    if type(last) is int:
        first = eval_expression(sequence[:-2])
        operation = sequence[-2]
        if operation == '+':
            return first + last
        if operation == '*':
            return first * last

    if last == ')':
        start = find_start(sequence)
        last = eval_expression(sequence[start + 1:-1])
        if start == 0:
            return last
        return eval_expression(sequence[:start] + [last])


def eval_expression2(sequence) -> int:
    # resolve parenthesis
    if ')' in sequence:
        end = sequence.index(')')
        start = find_start(sequence[:end+1])
        return eval_expression2(
            sequence[:start] +
            [eval_expression2(sequence[start+1:end])] +
            sequence[end+1:]
        )

    # resolve +
    while '+' in sequence:
        position = sequence.index('+')
        sequence = sequence[:position - 1] + [sequence[position-1] + sequence[position+1]] + sequence[position + 2:]

    # resolve *
    return prod(c for c in sequence if type(c) is int)


print(sum(map(eval_expression, expressions)))
print(sum(map(eval_expression2, expressions)))
