import numpy as np
from parse import parse
from tqdm import tqdm

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 26
    part_two_test_solution = 56000011

    def preprocess_input(self, lines):

        readings = []
        for line in lines:
            sx, sy, bx, by = parse('Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}', line)
            readings.append(((sx, sy), (bx, by), abs(sx - bx) + abs(sy - by)))

        return readings, 10 if readings[0][0] == (2, 18) else 2000000

    @staticmethod
    def join_intervals(intervals):
        intersected_intervals = []
        in_intervals = set()
        current_interval_start = None
        for point in sorted({p for interval in intervals for p in interval}):
            for interval in intervals:
                if point == interval[0]:
                    in_intervals.add(interval)
                    if current_interval_start is None:
                        if intersected_intervals and intersected_intervals[-1][1] + 1 == point:
                            current_interval_start = intersected_intervals[-1][0]
                            intersected_intervals = intersected_intervals[:-1]
                        else:
                            current_interval_start = point

            for interval in intervals:
                if point == interval[1]:
                    in_intervals.remove(interval)
                    if not in_intervals:
                        intersected_intervals.append((current_interval_start, point))
                        current_interval_start = None
        return intersected_intervals

    @staticmethod
    def get_covered_intervals(readings, y):
        covered_intervals = set()
        for (sx, sy), _, distance in readings:
            interference = distance - abs(sy - y)
            if interference >= 0:
                covered_intervals.add((sx - interference, sx + interference))
        return Level.join_intervals(covered_intervals)

    def part_one(self, readings, y) -> int:
        covered_intervals = self.get_covered_intervals(readings, y)
        covered_beacons = {
            (bx, by) for s, (bx, by), d in readings if by == y and any(s <= bx <= e for s, e in covered_intervals)
        }
        return sum(e - s + 1 for s, e in covered_intervals) - len(covered_beacons)

    # runs in ~90s
    def part_two_slow(self, readings, y) -> int:
        self.get_covered_intervals(readings, 7)
        max_coordinate = 2 * y
        for row in tqdm(range(max_coordinate)):
            covered_intervals = self.get_covered_intervals(readings, row)
            if len(covered_intervals) > 1:
                assert len(covered_intervals) == 2
                assert covered_intervals[0][1] + 2 == covered_intervals[1][0]
                return row + (covered_intervals[0][1] + 1) * 4000000

    # runs really fast
    def part_two(self, readings, y) -> int:
        # lets rotate rotate 45˚
        new_base = np.array([[1, 1], [-1, 1]])
        boxes = []
        for s, _, distance in readings:
            cx, cy = new_base.dot(s)
            boxes.append((cx - distance, cx + distance, cy - distance, cy + distance))

        # find empty lines between boxes which are nearly touching
        y_lines, x_lines = [], []  # y_line = (x, (y_start, y_end))
        for b1 in boxes:
            for b2 in boxes:
                if b1[1] + 2 == b2[0]:
                    y_lines.append((b1[1] + 1, (max(b1[2], b2[2]), min(b1[3], b2[3]))))
                if b1[3] + 2 == b2[2]:
                    x_lines.append((b1[3] + 1, (max(b1[0], b2[0]), min(b1[1], b2[1]))))

        # find intersection
        for xl in x_lines:
            for yl in y_lines:
                if yl[1][0] <= xl[0] <= yl[1][1] and xl[1][0] <= yl[0] <= xl[1][1]:
                    place = np.linalg.inv(new_base).dot((yl[0], xl[0]))
                    return int(place[1] + place[0] * 4000000)


Level().run()
