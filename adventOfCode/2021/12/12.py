from collections import defaultdict

from core import AdventOfCode



class Level(AdventOfCode):
    part_one_test_solution = 226
    part_two_test_solution = 3509

    def preprocess_input(self, lines):
        edges = defaultdict(set)
        for line in lines:
            cave1, cave2 = line.strip().split('-')
            edges[cave1].add(cave2)
            edges[cave2].add(cave1)
        return edges

    def extend_path(self, path, edges, part_two=False, double_used=False):
        if path[-1] == 'end':
            self.found_paths.append(path)
            return
        for next in edges[path[-1]]:
            in_path = next.islower() and next in path
            if next == 'start' or (double_used or not part_two) and in_path:
                continue
            self.extend_path(
                path + [next], edges,
                part_two=part_two,
                double_used=double_used or in_path
            )

    def search_paths(self, edges, part_two=False):
        self.found_paths = []
        self.extend_path(['start'], edges, part_two=part_two)
        return self.found_paths

    def part_one(self, edges) -> int:
        return len(self.search_paths(edges))

    def part_two(self, edges) -> int:
        return len(self.search_paths(edges, part_two=True))


Level().run()
