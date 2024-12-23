from itertools import combinations

import networkx as nx

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 7
    part_two_test_solution = 'co,de,ka,ta'

    def preprocess_input(self, lines):
        return list((a, b) for a, b in map(lambda l: l.split('-'), lines))

    def part_one(self, connections) -> int:
        graph = nx.from_edgelist(connections)
        result = set()
        for clique in nx.find_cliques(graph):
            if len(clique) < 3:
                continue
            for clique3 in combinations(clique, 3):
                if any(c.startswith('t') for c in clique3):
                    result.add(tuple(sorted(clique3)))
        return len(result)

    def part_two(self, connections) -> str:
        graph = nx.from_edgelist(connections)
        return ','.join(sorted(max(nx.find_cliques(graph), key=len)))


if __name__ == '__main__':
    Level().run()
