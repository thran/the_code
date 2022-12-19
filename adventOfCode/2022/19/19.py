import math
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

    @staticmethod
    def can_build(blueprint, supplies, robot: str):
        return all(s >= cost for s, cost in zip(supplies, blueprint[robot]))

    def get_robot_creation_options(self, blueprint, supplies, robots, remaining_steps):
        options = []

        if self.can_build(blueprint, supplies, 'geode'):
            return [(0, 0, 0, 1)]
        if remaining_steps < 2:
            return

        if self.can_build(blueprint, supplies, 'obsidian'):
            options.append((0, 0, 1, 0))
            # if supplies[1] + 2 * robots[1] < 2 * blueprint['obsidian'][1] <= supplies[1] + 2 * robots[1] + 3:
            #     ic(supplies, robots, remaining_steps)
            # else:
            #     return options

        if remaining_steps < 3:
            return
        if self.can_build(blueprint, supplies, 'clay'):
            if supplies[1] < blueprint['obsidian'][1] * 2:
                options.append((0, 1, 0, 0))

        if remaining_steps < 4:
            return
        if robots[0] < max(c[0] for r, c in blueprint.items() if r != 'ore'):
            if self.can_build(blueprint, supplies, 'ore'):
                options.append((1, 0, 0, 0))
            options.append((0, 0, 0, 0))

        return options

    @cache
    def maximize_geodes(self, blueprint_index, robots, supplies, remaining_steps):
        # ic(robots, supplies, remaining_steps)
        if remaining_steps == 0:
            return supplies[-1]

        if remaining_steps == 1:
            return supplies[-1] + robots[-1]

        if (
            supplies[-1] == 0
            and supplies[-2] == 0
            and remaining_steps < self.blueprints[blueprint_index]['geode'][2] / 2
        ):

            return 0

        results = []
        for new_robots in self.get_robot_creation_options(
            self.blueprints[blueprint_index], supplies, robots, remaining_steps
        ) or [(0, 0, 0, 0)]:
            robots_cost = [0, 0, 0, 0]
            for material, robot_count in zip(self.MATERIALS, new_robots):
                for i, material_cost in enumerate(self.blueprints[blueprint_index][material]):
                    robots_cost[i] += material_cost * robot_count
            new_supplies = tuple(r + s - rc for r, s, rc in zip(robots, supplies, robots_cost))
            new_robots = tuple(r + nr for r, nr in zip(robots, new_robots))
            r = self.maximize_geodes(blueprint_index, new_robots, new_supplies, remaining_steps - 1)
            results.append(r)
        return max(results)

    def part_one(self, blueprints) -> int:
        quality = 0
        for i in blueprints:
            self.maximize_geodes.cache_clear()
            geodes = self.maximize_geodes(i, (1, 0, 0, 0), (0, 0, 0, 0), 24)
            ic(i, geodes)
            quality += i * geodes
        return quality

    def part_two(self, blueprints) -> int:
        quality = 1
        for i in range(1, min(3, len(blueprints)) + 1):
            self.maximize_geodes.cache_clear()
            geodes = self.maximize_geodes(i, (1, 0, 0, 0), (0, 0, 0, 0), 32)
            ic(i, geodes)
            quality *= geodes
        return quality


Level().run()
