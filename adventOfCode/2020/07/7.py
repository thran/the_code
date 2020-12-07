# start 11:10, 1. 11:42, 2: 11:51
from collections import defaultdict
from pathlib import Path
from parse import parse

rules = {}
reversed_map = defaultdict(set)
with Path('input.txt').open() as file:
    for line in file:
        result = parse('{outer} bags contain {inners}.', line.strip())

        inner_bags = {}
        for inner in result['inners'].split(', '):
            count, *name, _ = inner.split()
            if count == 'no':
                continue
            name = ' '.join(name)
            inner_bags[name] = int(count)
            reversed_map[name].add(result['outer'])
        rules[result['outer']] = inner_bags


to_explore = ['START']
explored = set()
found = []
while to_explore:
    bag = to_explore.pop()
    explored.add(bag)
    if bag in rules:
        found.append(bag)

    for b in reversed_map['shiny gold' if bag == 'START' else bag]:
        if b not in explored and b not in to_explore:
            to_explore.append(b)

print(len(found))


bags = {'shiny gold': 1}
total = -1
while bags:
    new_bags = defaultdict(int)
    for bag, count in bags.items():
        total += count
        for inner_bag, inner_count in rules[bag].items():
            new_bags[inner_bag] += inner_count * count
    bags = new_bags

print(total)