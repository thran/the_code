from collections import defaultdict

from tqdm import tqdm

tape = defaultdict(int)
cursor = 0

test = False
if test:
    state = 'A'
    steps = 6
    transition = {
        ('A', 0): (1, 1, 'B'),
        ('A', 1): (0, -1, 'B'),
        ('B', 0): (1, -1, 'A'),
        ('B', 1): (1, 1, 'A'),
    }
else:
    state = 'A'
    steps = 12586542
    transition = {
        ('A', 0): (1, 1, 'B'),
        ('A', 1): (0, -1, 'B'),

        ('B', 0): (0, 1, 'C'),
        ('B', 1): (1, -1, 'B'),

        ('C', 0): (1, 1, 'D'),
        ('C', 1): (0, -1, 'A'),

        ('D', 0): (1, -1, 'E'),
        ('D', 1): (1, -1, 'F'),

        ('E', 0): (1, -1, 'A'),
        ('E', 1): (0, -1, 'D'),

        ('F', 0): (1, 1, 'A'),
        ('F', 1): (1, -1, 'E'),
    }

for _ in tqdm(range(steps)):
    nt, dc, state = transition[state, tape[cursor]]
    tape[cursor] = nt
    cursor += dc

print(sum(tape.values()))
