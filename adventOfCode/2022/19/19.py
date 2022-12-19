from collections import defaultdict
from functools import cache

from parse import parse

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 33
    part_two_test_solution = 56 * 62

    MATERIALS = ('ore', 'clay', 'obsidian', 'geode')

    def preprocess_input(self, lines):
        self.blueprints = blueprints = {}
        for line in lines:
            result = parse(
                'Blueprint {id:d}: Each ore robot costs {ore_ore:d} ore. Each clay robot costs {clay_ore:d} ore. Each obsidian robot costs {obsidian_ore:d} ore and {obsidian_clay:d} clay. Each geode robot costs {geode_ore:d} ore and {geode_obsidian:d} obsidian.',
                line)  # fmt:skip
            blueprint = defaultdict(lambda: [0, 0, 0])
            for k, v in result.named.items():
                if k == 'id':
                    continue
                robot, material = k.split('_')
                blueprint[robot][self.MATERIALS.index(material)] = v
            blueprints[result['id']] = dict(blueprint)

        return blueprints

    def can_build(self, supplies, robot: str):
        return all(s >= cost for s, cost in zip(supplies, self.blueprint[robot]))

    def compute_supplies(self, supplies, robots, new_robot):
        if new_robot:
            robots_cost = self.blueprint[new_robot] + [0]
        else:
            robots_cost = (0, 0, 0, 0)
        return tuple(r + s - rc for r, s, rc in zip(robots, supplies, robots_cost))

    def get_robot_creation_options(self, supplies, robots, remaining_steps):
        options = []

        if self.can_build(supplies, 'geode'):
            options.append('geode')
            return options

        if remaining_steps < 3:
            return options

        if self.can_build(supplies, 'obsidian'):
            options.append('obsidian')

        if self.can_build(supplies, 'clay'):
            options.append('clay')

        if robots[0] < self.max_ore_price:
            if self.can_build(supplies, 'ore'):
                options.append('ore')
            options.append(None)

        return options

    @cache
    def maximize_geodes(self, robots, supplies, remaining_steps):
        if remaining_steps == 0:
            return supplies[-1]

        if remaining_steps == 1:
            return supplies[-1] + robots[-1]

        results = []
        for new_robot in self.get_robot_creation_options(supplies, robots, remaining_steps) or [None]:
            new_supplies = self.compute_supplies(supplies, robots, new_robot)
            new_robots = tuple(r + 1 if self.MATERIALS[i] == new_robot else r for i, r in enumerate(robots))
            r = self.maximize_geodes(new_robots, new_supplies, remaining_steps - 1)
            results.append(r)
        return max(results)

    def set_blueprint(self, blueprint):
        self.blueprint = blueprint
        self.max_ore_price = max(c[0] for r, c in blueprint.items() if r != 'ore')
        self.max_clay_price = max(c[1] for r, c in blueprint.items())
        self.maximize_geodes.cache_clear()

    def part_one(self, blueprints) -> int:
        quality = 0
        for i, blueprint in blueprints.items():
            self.set_blueprint(blueprint)
            geodes = self.maximize_geodes((1, 0, 0, 0), (0, 0, 0, 0), 24)
            quality += i * geodes
        return quality

    def part_two(self, blueprints) -> int:
        quality = 1
        for i in range(1, min(3, len(blueprints)) + 1):
            self.set_blueprint(blueprints[i])
            geodes = self.maximize_geodes((1, 0, 0, 0), (0, 0, 0, 0), 32)
            quality *= geodes
        return quality


Level().run()
