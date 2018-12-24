import re

from tqdm import tqdm


class Group:
    def __init__(self, type, units, hits, attack, attack_type, initiative, weaknesses, immunities, groups):
        self.type = type
        self.units = units
        self.hits = hits
        self.attack = attack
        self.attack_type = attack_type
        self.initiative = initiative
        self.weaknesses = weaknesses
        self.immunities = immunities

        self.selected = False
        self.attack_to: Group = None
        self.groups = groups

    @property
    def power(self):
        return self.units * self.attack

    def select_target(self, verbose=False):
        if verbose:
            print(f'{self} \n')
        candidates = [
            (group.get_dgm_from(self), group.power, group.initiative, group)
            for group in self.groups
            if self.type != group.type and not group.selected
        ]
        if not candidates:
            if verbose:
                print('   no target')
            self.attack_to = None
            return
        best = max(candidates)
        if best[0] <= 0:
            if verbose:
                print('   zero dmg')
            self.attack_to = None
            return
        self.attack_to = best[-1]
        self.attack_to.selected = True
        if verbose:
            print(f'   target {self.attack_to}')

    def action(self):
        if self.attack_to is None or self.units <= 0:
            return

        dmg = self.attack_to.get_dgm_from(self)
        self.attack_to.units -= dmg // self.attack_to.hits
        if self.attack_to.units <= 0:
            del self.groups[self.groups.index(self.attack_to)]

    def get_dgm_from(self, group):
        if group.attack_type in self.immunities:
            return 0
        if group.attack_type in self.weaknesses:
            return group.power * 2
        return group.power

    def __str__(self):
        return f'{self.type}: {self.power} EP; {self.units} units; {self.hits} HP; {self.attack} attack ({self.attack_type}); IM {self.immunities}; WEAK {self.weaknesses}'

def test(boost):
    groups = []
    with open('input.txt') as f:
        t = None
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.endswith(':'):
                t = line[:-1]
                continue

            units, hits, WI, attack, attack_type, initiative = re.match(r'(\d+) units each with (\d+) hit points \((.*)\) with an attack that does (\d+) (\w+) damage at initiative (\d+)', line).groups()
            weaknesses = set()
            immunities = set()
            for s in WI.split('; '):
                if s.startswith('weak to'):
                    for w in s[8:].split(', '):
                        weaknesses.add(w)
                elif s.startswith('immune to'):
                    for w in s[10:].split(', '):
                        immunities.add(w)

            group = Group(t, int(units), int(hits), int(attack), attack_type, int(initiative), weaknesses, immunities, groups)
            groups.append(group)

    for group in [g for g in groups if g.type == 'Immune System']:
        group.attack += boost

    ls = 0
    while True:
        # target selection
        for group in groups:
            group.selected = False
        for group in sorted(groups, key=lambda g: (-g.power, -g.initiative)):
            group.select_target()

        # attack
        for group in sorted(groups, key=lambda g: (-g.initiative)):
            group.action()


        if len({g.type for g in groups}) < 2:
            break
        # print(len(groups))

        if sum([g.units for g in groups]) == ls:
            break
        ls = sum([g.units for g in groups])

    # for group in groups:
    #     print(group)
    return sum([g.units for g in groups]), {g.type for g in groups} == {'Immune System'}


print(test(0))

boost = 1
IS_win = False

while not IS_win:
    boost *= 2
    r, IS_win = test(boost)
    print(boost, r, IS_win)

while IS_win:
    r, IS_win = test(boost)
    boost -= 1
    print(boost, r, IS_win)

boost += 2

print(boost, test(boost))
