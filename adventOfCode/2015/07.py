import re
from collections import defaultdict

import numpy as np

wires = {}
waiting = defaultdict(lambda: [])


def EQ(input, output):
    if input in wires:
        trigger(output, wires[input])
    else:
        waiting[input].append(lambda: EQ(input, output))


def NOT(input, output):
    if input in wires:
        trigger(output, ~wires[input] % 2 ** 16)
    else:
        waiting[input].append(lambda: NOT(input, output))


def AND(input1, input2, output):
    if input1 in wires and input2 in wires:
        trigger(output, wires[input1] & wires[input2])
    else:
        if input1 not in wires:
            waiting[input1].append(lambda: AND(input1, input2, output))
            return
        if input2 not in wires:
            waiting[input2].append(lambda: AND(input1, input2, output))


def OR(input1, input2, output):
    if input1 in wires and input2 in wires:
        trigger(output, wires[input1] | wires[input2])
    else:
        if input1 not in wires:
            waiting[input1].append(lambda: OR(input1, input2, output))
            return
        if input2 not in wires:
            waiting[input2].append(lambda: OR(input1, input2, output))


def LSHIFT(input1, input2, output):
    if input1 in wires:
        trigger(output, wires[input1] << input2 % 2 ** 16)
    else:
        waiting[input1].append(lambda: LSHIFT(input1, input2, output))


def RSHIFT(input1, input2, output):
    if input1 in wires:
        trigger(output, wires[input1] >> input2)
    else:
        waiting[input1].append(lambda: RSHIFT(input1, input2, output))


def trigger(wire, value):
    wires[wire] = value
    [w() for w in waiting[wire]]


with open("07.txt") as source:
    trigger("1", 1)
    for line in source.readlines():
        r = re.match(r'([a-z]+) -> (\w+)$', line)
        if r:
            EQ(r.group(1), r.group(2))

        r = re.match(r'(\d+) -> (\w+)$', line)
        if r:
            trigger(r.group(2), int(r.group(1)))

        r = re.match(r'NOT (\w+) -> (\w+)$', line)
        if r:
            NOT(r.group(1), r.group(2))

        r = re.match(r'(\w+) AND (\w+) -> (\w+)$', line)
        if r:
            AND(r.group(1), r.group(2), r.group(3))

        r = re.match(r'(\w+) OR (\w+) -> (\w+)$', line)
        if r:
            OR(r.group(1), r.group(2), r.group(3))

        r = re.match(r'(\w+) LSHIFT (\d+) -> (\w+)$', line)
        if r:
            LSHIFT(r.group(1), int(r.group(2)), r.group(3))

        r = re.match(r'(\w+) RSHIFT (\d+) -> (\w+)$', line)
        if r:
            RSHIFT(r.group(1), int(r.group(2)), r.group(3))

print wires["a"]
