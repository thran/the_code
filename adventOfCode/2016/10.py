import re
from collections import defaultdict

from functools import reduce
from operator import mul

with open('10.txt') as f:
    instructions = f.readlines()

initial = []
rules = {}
bots = defaultdict(lambda: [])
outputs = defaultdict(lambda: [])

for ins in instructions:
    if ins.startswith('value'):
        g = re.search('value (\d+) goes to bot (\d+)', ins).groups()
        initial.append((int(g[0]), g[1]))
    else:
        g = re.search('bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)', ins).groups()
        rules[g[0]] = (g[1][0] == 'o', g[2]), (g[3][0] == 'o', g[4])


# compare = ['2', '5']
compare = [17, 61]


def move(chip, bot, output=False):
    if output:
        outputs[bot].append(chip)
        return
    bots[bot].append(chip)
    if len(bots[bot]) == 2:
        if sorted(bots[bot]) == compare:
            print(bot)
        move(min(bots[bot]), rules[bot][0][1], rules[bot][0][0])
        move(max(bots[bot]), rules[bot][1][1], rules[bot][1][0])
        bots[bot] = []

for ini in initial:
    move(ini[0], ini[1])

print(reduce(mul, outputs['0'] + outputs['1'] + outputs['2'], 1))
