import heapq

import numpy as np

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 40
    part_two_test_solution = 315

    def preprocess_input(self, lines):
        return np.array([list(map(int, line)) for line in lines])

    def neighbours(self, position, array):
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbour = position[0] + dx, position[1] + dy
            if not (0 <= neighbour[0] < array.shape[0] and 0 <= neighbour[1] < array.shape[1]):
                continue
            yield neighbour

    def find_path(self, floor) -> int:
        possible_visit_cost = np.empty_like(floor, dtype=float)
        possible_visit_cost.fill(np.inf)
        possible_visit_cost[0, 0] = 0
        visited = np.zeros_like(floor, dtype=bool)

        next_step_heap = []
        heapq.heappush(next_step_heap, (0, (0, 0)))

        target = floor.shape[0] - 1, floor.shape[1] - 1
        while not visited[target]:
            cost, visiting_position = heapq.heappop(next_step_heap)
            visited[visiting_position] = True

            for position in self.neighbours(visiting_position, floor):
                if visited[position]:
                    continue
                new_cost = cost + floor[position]
                if new_cost < possible_visit_cost[position]:
                    heapq.heappush(next_step_heap, (new_cost, position))
                    possible_visit_cost[position] = new_cost

        return int(possible_visit_cost[target])

    def part_one(self, floor) -> int:
        return self.find_path(floor)

    def part_two(self, floor) -> int:
        big_floor = []
        for i in range(5):
            tiles = []
            for j in range(5):
                tiles.append((floor + i + j - 1) % 9 + 1)
            big_floor.append(np.concatenate(tiles))
        big_floor = np.concatenate(big_floor, axis=1)
        return self.find_path(big_floor)


Level().run()
