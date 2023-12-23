from collections import defaultdict

import networkx as nx
import numpy as np
import pylab as plt

from adventOfCode.utils import array, SmartArray, SearchAll
from core import AdventOfCode


class SearchPart(SearchAll):
    SLIPS = {'R': (0, 1), 'D': (1, 0)}

    def __init__(self, maze, start, no_slip):
        super().__init__([([start], start)])
        self.maze: SmartArray = maze
        self.no_slip = no_slip
        self.found_paths = []
        self.run()

    def next_states(self, state):
        path, current_position = state
        if not self.no_slip and self.maze[current_position] in self.SLIPS:
            new_position = self.maze.change_position(current_position, self.SLIPS[self.maze[current_position]])
            yield path + [new_position], new_position
            return

        for delta in self.maze.direct_neighbors_deltas:
            position = self.maze.change_position(current_position, delta)
            if position in path:
                continue
            if self.maze[position] == '#':
                continue
            if not self.no_slip:
                if self.maze[position] == 'R' and delta != self.SLIPS['R']:
                    continue
                if self.maze[position] == 'D' and delta != self.SLIPS['D']:
                    continue

            yield path + [position], position

    def end_condition(self, state):
        return self.maze[state[1]] in self.SLIPS or state[1] == self.maze.END

    def on_found(self, state):
        self.found_paths.append(state)


class LongestPathSearch(SearchAll):
    def __init__(self, edges, start, end):
        self.edges = edges
        self.start = start
        self.end = end
        self.found_lengths = set()
        super().__init__([({start}, start, 0)])
        self.run()

    def next_states(self, state):
        path, position, length = state
        for new_position, l in self.edges[position].items():
            if new_position not in path:
                yield path | {new_position}, new_position, length + l

    def end_condition(self, state) -> bool:
        path, node, length = state
        if node == self.end:
            return True
        return False

    def on_found(self, state):
        self.found_lengths.add(state[2])


class Level(AdventOfCode):
    part_one_test_solution = 94
    part_two_test_solution = 154

    def preprocess_input(self, lines):
        rows = []
        for line in lines:
            rows.append([{'>': 'R', 'v': 'D', '.': '.', '#': '#'}[char] for char in line])
        maze = array(rows)
        maze.START = (0, 1)
        maze[maze.START] = '#'
        maze.END = (maze.shape[0] - 1, maze.shape[1] - 2)
        return maze

    def part_one(self, maze: SmartArray, no_slip=False) -> int:
        nodes = [maze.START, maze.END] + list(zip(*np.where((maze == 'D') | (maze == 'R'))))
        edges = defaultdict(dict)
        for start in nodes:
            if start == maze.END:
                continue
            for path, end in SearchPart(maze, start, no_slip).found_paths:
                if edges[start].get(end, 0) < len(path) - 1:
                    edges[start][end] = len(path) - 1

        graph = nx.DiGraph()
        for node, es in edges.items():
            for n, l in es.items():
                graph.add_edge(node, n, l=l)

        components = nx.connected_components(
            nx.Graph(graph.edge_subgraph((u, v) for u, v, d in graph.edges(data=True) if d['l'] == 2))
        )
        components = [{maze.START}] + list(components) + [{maze.END}]
        crossroads = {}
        for i, component in enumerate(components):
            for node in component:
                crossroads[node] = i

        simple_edges = defaultdict(dict)
        for node, es in edges.items():
            for n, l in es.items():
                if l == 2:
                    assert crossroads[node] == crossroads[n]
                else:
                    simple_edges[crossroads[node]][crossroads[n]] = l + (2 if n != maze.END else 0)

        return max(LongestPathSearch(simple_edges, 0, len(components) - 1).found_lengths)

    def part_two(self, maze) -> int:
        return self.part_one(maze, no_slip=True)


if __name__ == '__main__':
    Level().run()
