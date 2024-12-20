import numpy as np
from scipy.spatial.distance import cdist

from adventOfCode.utils import array, SmartArray
from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 44
    part_two_test_solution = 285

    def preprocess_input(self, lines):
        grid = array([tuple(line) for line in lines])
        start = tuple(map(lambda p: p[0], np.where(grid == 'S')))
        end = tuple(map(lambda p: p[0], np.where(grid == 'E')))
        grid[start] = '.'
        grid[end] = '.'
        return array(grid == '#'), start, end

    def find_distances(self, grid: SmartArray, start, end) -> dict[tuple, int]:
        distances = {end: 0}
        position = end
        distance = 0
        while position != start:
            candidates = [p for p in grid.direct_neighbors(position) if not grid[p] and p not in distances]
            assert len(candidates) == 1
            position = candidates[0]
            distance += 1
            distances[position] = distance
        return distances

    def find_shortcuts(self, grid: SmartArray, distances: dict[tuple, int]) -> dict[tuple[tuple, tuple], int]:
        shortcuts = {}
        for position, distance in distances.items():
            for delta in grid.direct_neighbors_deltas:
                new_position = grid.change_position(grid.change_position(position, delta), delta)
                if new_position not in distances:
                    continue
                new_distance = distances[new_position]
                if new_distance + 2 < distance:
                    shortcuts[position, delta] = distance - new_distance - 2

        return shortcuts

    def part_one(self, grid: SmartArray, start, end) -> int:
        limit = 0 if grid.shape[0] < 20 else 100
        distances = self.find_distances(grid, start, end)
        shortcuts = self.find_shortcuts(grid, distances)
        return len([1 for d in shortcuts.values() if d >= limit])

    def part_two(self, grid: SmartArray, start, end, cheat=20) -> int:
        limit = 50 if grid.shape[0] < 20 else 100
        distances = self.find_distances(grid, start, end)
        points = np.array(tuple(distances))
        shortcut_distances = cdist(points, points, metric='cityblock').astype(int)
        pathlib_distances = np.array(tuple(distances.values()))
        pathlib_distances = pathlib_distances[:, None] - pathlib_distances[None, :]
        return ((shortcut_distances <= cheat) & (pathlib_distances - shortcut_distances >= limit)).sum()


if __name__ == '__main__':
    Level().run()
