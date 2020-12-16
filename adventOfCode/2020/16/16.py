# start 9:10, 1. 9:25, 2. 9:48
from pathlib import Path


fields = {}
tickets = []
with Path('input.txt').open() as file:
    while line := file.readline().strip():
        field, conditions = line.split(': ')
        conditions = conditions.split(' or ')
        fields[field] = [tuple(map(int, c.split('-'))) for c in conditions]

    file.readline()
    my_ticket = tuple(map(int, file.readline().strip().split(',')))
    file.readline()

    file.readline()
    while line := file.readline().strip():
        tickets.append(tuple(map(int, line.split(','))))


def valid_fields(value):
    for field, conditions in fields.items():
        for lower, higher in conditions:
            if lower <= value <= higher:
                yield field


print(sum([v for t in tickets for v in t if not any(valid_fields(v))]))


tickets = [t for t in tickets if all(any(valid_fields(v)) for v in t)]

possible_fields = [set(fields.keys()) for _ in my_ticket]
for ticket in tickets:
    for i, value in enumerate(ticket):
        s = set(valid_fields(value))
        possible_fields[i] &= set(valid_fields(value))


change = True
while change:
    change = False
    for i, ps in enumerate(possible_fields):
        if len(ps) == 1:
            field_to_remove = next(iter(ps))
            for j, pf in enumerate(possible_fields):
                if j != i and field_to_remove in pf:
                    pf.remove(field_to_remove)
                    change = True


total = 1
for field, value in zip(possible_fields, my_ticket):
    assert len(field) == 1
    if next(iter(field)).startswith('departure'):
        total *= value
print(total)
