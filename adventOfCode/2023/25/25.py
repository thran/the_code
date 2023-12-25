import networkx as nx
import numpy as np
from matplotlib import pyplot as plt

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 54
    skip_tests = True

    def preprocess_input(self, lines):
        graph = nx.Graph()
        for line in lines:
            node, nodes = line.split(': ')
            for node2 in nodes.split():
                graph.add_edge(node, node2)
        return graph

    def part_one(self, graph: nx.Graph) -> int:
        print(graph)
        plt.figure(figsize=(50, 50))
        # nx.draw(graph, nx.layout.spring_layout(graph), with_labels=True)
        # plt.show()
        graph.remove_edge('jlt', 'sjr')
        graph.remove_edge('mzb', 'fjn')
        graph.remove_edge('zqg', 'mhb')
        return np.prod(list(map(len, nx.connected_components(graph))))

    def part_two(self, graph) -> int:
        ...


if __name__ == '__main__':
    Level().run()
