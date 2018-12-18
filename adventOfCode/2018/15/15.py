from copy import deepcopy
from itertools import count

ADJS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


class Map:
    def __init__(self, attack_power):
        self.map = []
        self.units = []
        self.ended = False
        with open('input.txt') as f:
            for x, line in enumerate(f):
                row = []
                for y, field in enumerate(line.strip()):
                    if field in ['E', 'G']:
                        unit = Unit(self, field, x, y)
                        if field == 'E':
                            unit.attack_power = attack_power
                        self.units.append(unit)
                        field = '.'
                    row.append(field)
                self.map.append(row)

    def round(self):
        for unit in self.sorted_units():
            if unit.hit_points > 0:
                unit.turn()

    def sorted_units(self):
        return sorted(self.units, key=lambda u: (u.x, u.y))

    def get_targets(self, type):
        targets = set()
        for unit in self.units:
            if type != unit.type:
                continue
            for dx, dy in ADJS:
                if self.is_empty(unit.x + dx, unit.y + dy):
                    targets.add((unit.x + dx, unit.y + dy))
        return targets

    def is_empty(self, x, y):
        if self.map[x][y] != '.':
            return False
        for unit in self.units:
            if x == unit.x and y == unit.y:
                return False
        return True

    def run(self):
        round = 0
        print(self)
        while self.has_enemies() and not self.ended:
            round += 1
            print(round)
            self.round()
            print(self)
        print(round - 1, sum(u.hit_points for u in self.units), (round - 1) * sum(u.hit_points for u in self.units), )
        print(round, sum(u.hit_points for u in self.units), (round) * sum(u.hit_points for u in self.units), )
        return not self.ended

    def has_enemies(self):
        return len([u for u in self.units if u.type == 'G']) * len([u for u in self.units if u.type == 'E']) > 0

    def __str__(self):
        r = ''
        for x, row in enumerate(self.map):
            for y, field in enumerate(row):
                for unit in self.units:
                    if unit.is_in_position(x, y):
                        r += str(unit)
                        break
                else:
                    r += field
            r += '\n'
        return r


class Unit:
    def __init__(self, map: Map, type, x, y):
        self.map = map
        self.type = type
        self.x = x
        self.y = y
        self.hit_points = 200
        self.attack_power = 3

    def is_in_position(self, x, y):
        return self.x == x and self.y == y

    def turn(self):
        if not self.in_range():
            self.move()
        in_range = self.in_range()
        if in_range:
            unit = min(in_range, key=lambda u: (u.hit_points, u.x, u.y))
            # print('attack', self.x, self.y, '-->', unit.x, unit.y)
            unit.hit(self.attack_power)

    def move(self):
        targets = self.map.get_targets('E' if self.type == 'G' else 'G')
        # print(self.x, self.y, targets)
        if len(targets) == 0:
            return
        paths, target = self.get_paths(targets)
        if target is None:
            return
        d, (x, y) = paths[target[0]][target[1]]
        # print(self.x, self.y, paths, target)
        if d == 1:
            self.x, self.y = target
        else:
            while d > 2:
                d, (x, y) = paths[x][y]
            self.x = x
            self.y = y

    def in_range(self):
        in_range = set()
        for unit in self.map.units:
            if self.type == unit.type:
                continue
            for dx, dy in ADJS:
                if self.x + dx == unit.x and self.y + dy == unit.y:
                    in_range.add(unit)
        return in_range

    def get_paths(self, targets):
        changed = True
        paths = deepcopy(self.map.map)
        paths[self.x][self.y] = 0, None
        distance = 0
        while changed:
            changed = False
            distance += 1
            new = set()
            for x, row in enumerate(paths):
                for y, field in enumerate(row):
                    if not self.map.is_empty(x, y) or paths[x][y] != '.':
                        continue
                    adjs = [(x + dx, y + dy) for dx, dy in ADJS if type(paths[x + dx][y + dy]) == tuple and paths[x + dx][y + dy][0] == distance - 1]
                    if adjs:
                        changed = True
                        paths[x][y] = distance, min(adjs)
                        new.add((x, y))
            if targets & new:
                break
        if not new:
            return paths, None
        return paths, min(targets & new)

    def hit(self, attack_power):
        self.hit_points -= attack_power
        if self.hit_points <= 0:
            self.map.units.remove(self)
            if self.type == 'E':
                self.map.ended = True
                print('Elf dead')

    def __str__(self):
        return self.type


for ap in count(4):
    m = Map(ap)
    if m.run():
        break

