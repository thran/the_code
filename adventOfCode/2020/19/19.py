# start 9:37, 1. 9:58, 2. 10:06
from pathlib import Path
from pyformlang.cfg import Production, Variable, Terminal, CFG


terminals = {}
non_terminals = {}


def trans(name):
    if type(name) is int:
        if name not in non_terminals:
            non_terminals[name] = Variable(name)
        return non_terminals[name]
    else:
        if name not in terminals:
            terminals[name] = Terminal(name)
        return terminals[name]


rules = set()
rules2 = set()
with Path('input.txt').open() as file:
    while line := file.readline().strip():
        left, rights = line.split(': ')
        for right in rights.split(' | '):
            rule = Production(trans(int(left)), list(map(trans, map(eval, right.split()))))
            rules.add(rule)
            rules2.add(rule)
            if left == '8':
                rules2.add(Production(trans(int(left)), list(map(trans, (42, 8)))))
            if left == '11':
                rules2.add(Production(trans(int(left)), list(map(trans, (42, 11, 31)))))

    words = [line.strip() for line in file.readlines()]

cfg = CFG(set(non_terminals.values()), set(terminals.values()), non_terminals[0], rules)
print(sum(cfg.contains(word) for word in words))

cfg2 = CFG(set(non_terminals.values()), set(terminals.values()), non_terminals[0], rules2)
print(sum(cfg2.contains(word) for word in words))
