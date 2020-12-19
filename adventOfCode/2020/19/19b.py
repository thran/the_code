from collections import defaultdict
from pathlib import Path

from utils import memoize

rules = defaultdict(set)
with Path('input.txt').open() as file:
    while line := file.readline().strip():
        left, rights = line.split(': ')
        for right in rights.split(' | '):
            rules[int(left)].add(tuple(list(map(eval, right.split()))))

    words = [line.strip() for line in file.readlines()]


@memoize
def is_rewritable(word, non_terminal=0):
    for rule in rules[non_terminal]:

        if len(rule) == 3:
            for i in range(1, len(word) - 2):
                for j in range(i + 1, len(word) - 1):
                    if \
                            is_rewritable(word[:i], rule[0]) and \
                            is_rewritable(word[j:], rule[2]) and \
                            is_rewritable(word[i:j], rule[1]):
                        return True

        if len(rule) == 1:
            if type(rule[0]) is str and len(word) == 1 and word == rule[0]:
                return True
            if type(rule[0]) is int:
                if is_rewritable(word, rule[0]):
                    return True
        if len(rule) == 2 and len(word) >= 2:
            for i in range(1, len(word)):
                if is_rewritable(word[:i], rule[0]) and is_rewritable(word[i:], rule[1]):
                    return True

    return False


print(sum(is_rewritable(word) for word in words))

is_rewritable.clear()
rules[8].add((42, 8))
rules[11].add((42, 11, 31))
print(sum(is_rewritable(word) for word in words))
