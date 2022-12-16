import re
from functools import cache
from itertools import combinations

import networkx as nx

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 1651
    part_two_test_solution = 1707

    def preprocess_input(self, lines):
        valves = {}
        for line in lines:
            result = re.match(r'Valve (..) has flow rate=(\d+); tunnels? leads? to valves? (.*)', line)
            valve, flow, paths = result.groups()
            valves[valve] = {'flow': int(flow), 'paths': paths.split(', ')}

        cave = nx.from_edgelist((valve, path) for valve, info in valves.items() for path in info['paths'])

        self.valves = valves
        self.distances = dict(nx.all_pairs_shortest_path_length(cave))
        return list(valve for valve, info in valves.items() if info['flow'])

    @cache
    def max_pressure_released(self, current_valve, remaining_valves, remaining_time) -> int:
        if remaining_time <= 0 or not remaining_valves:
            return 0

        solutions = []
        for valve in remaining_valves:
            rt = remaining_time - self.distances[current_valve][valve] - 1
            if rt < 0:
                continue
            rv = tuple(v for v in remaining_valves if v != valve)
            solutions.append(rt * self.valves[valve]['flow'] + self.max_pressure_released(valve, rv, rt))

        if not solutions:
            return 0
        return max(solutions)

    def setup(self, valves):
        return tuple(valve for valve, info in valves.items() if info['flow'])

    def part_one(self, valves_to_open) -> int:
        return self.max_pressure_released('AA', tuple(valves_to_open), 30)

    def part_two(self, valves_to_open) -> int:

        solutions = []
        for r in range(1, len(valves_to_open)):
            for for_me in combinations(valves_to_open, r):
                for_him = tuple(v for v in valves_to_open if v not in for_me)
                solutions.append(
                    self.max_pressure_released('AA', for_me, 26) + self.max_pressure_released('AA', for_him, 26)
                )

        return max(solutions)


Level().run()
