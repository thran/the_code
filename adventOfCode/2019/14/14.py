from collections import defaultdict
from math import ceil

from utils import binary_search

prices = {}

with open('input.txt') as f:
    for line in f:
        inputs, output = line.strip().split('=>')

        output_amount, output_chem = output.strip().split()
        output_amount = int(output_amount)

        parts = inputs.split(',')
        inputs = {}
        for part in parts:
            amount, chem = part.strip().split()
            inputs[chem] = int(amount)

        prices[output_chem] = output_amount, inputs


def get_ore(fuel):
    missing = defaultdict(int, {'FUEL': fuel})
    leftover = defaultdict(int)

    while [c for c, a in missing.items() if a > 0] != ['ORE']:
        for missing_chem, missing_amount in missing.items():
            if missing_chem == 'ORE':
                continue
            leftover_amount = min(missing_amount, leftover[missing_chem])
            missing_amount -= leftover_amount
            missing[missing_chem] = missing_amount
            leftover[missing_chem] -= leftover_amount
            if missing_amount == 0:
                continue

            factor = ceil(missing_amount / prices[missing_chem][0])
            # print(missing_amount, prices[missing_chem][0], factor)
            print(f'getting {factor} x {prices[missing_chem][0]} {missing_chem}')
            leftover[missing_chem] += factor * prices[missing_chem][0] - missing_amount
            missing[missing_chem] = 0
            for new_chem, new_amount in prices[missing_chem][1].items():
                missing[new_chem] += new_amount * factor
            break

        print('missing', {c: a for c, a in missing.items() if a > 0})
        print('left', {c: a for c, a in leftover.items() if a > 0})
        print()
    return missing['ORE']


print(get_ore(1))
print(binary_search(get_ore, 10 ** 12, 1))
