from itertools import product, permutations

import numpy as np
from scipy.spatial import distance_matrix

from core import AdventOfCode

OVERLAP = 12


all_rotations = []
identity = np.eye(3)
for transformations in product(
        (identity, np.diag([-1, 1, 1])),
        (identity, np.diag([1, -1, 1])),
        (identity, np.diag([1, 1, -1])),
        tuple(map(np.array, permutations(identity)))
):
    all_rotations.append(np.linalg.multi_dot(transformations))


class Scanner:
    def __init__(self, id_, beacons):
        self.id = id_
        self.position = np.zeros(3)
        self.beacons = np.array(beacons)
        self.distance_signatures = self.get_distance_signatures()

    def get_distance_signatures(self):
        distances = {}
        for i, beacon in enumerate(self.beacons):
            distances[i] = {
                tuple(sorted(distance))
                for distance in abs(self.beacons - beacon)
                if sum(distance) != 0
            }
        return distances

    def find_overlap(self, scanner: 'Scanner'):
        beacon_mapping = {}
        for beacon1, signature1 in self.distance_signatures.items():
            for beacon2, signature2 in scanner.distance_signatures.items():
                if len(signature1 & signature2) < OVERLAP - 1:
                    continue
                beacon_mapping[beacon1] = beacon2
        if len(beacon_mapping) < OVERLAP:
            return None
        assert len(beacon_mapping) == OVERLAP
        return beacon_mapping

    def align_according_to(self, scanner, beacon_mapping):
        assert (self.position == np.zeros(3)).all()
        pairs = np.array(list(beacon_mapping.items()))
        for rotation in all_rotations:
            distance_diffs = np.dot(self.beacons[pairs[:, 0]], rotation) - scanner.beacons[pairs[:, 1]]
            if (distance_diffs == distance_diffs[0]).all():
                self.transform(-distance_diffs[0], rotation)
                break
        else:
            assert False, 'alignment not found'

    def transform(self, translation, rotation):
        self.position += translation
        self.beacons = np.dot(self.beacons, rotation) + translation

    def __str__(self):
        return f'Scanner {self.id}'

    def __repr__(self):
        return str(self)


class Level(AdventOfCode):
    part_one_test_solution = 79
    part_two_test_solution = 3621

    def preprocess_input(self, lines):
        scanner = []
        scanners = [scanner]
        for line in lines:
            if line.startswith('---'):
                continue
            if not line:
                scanner = []
                scanners.append(scanner)
                continue
            scanner.append(eval(line))
        return [
            Scanner(i, scanner_data)
            for i, scanner_data in enumerate(scanners)
        ]

    def align_scanners(self, scanners):
        aligned_scanners = scanners[:1]
        unaligned_scanners = scanners[1:]
        while unaligned_scanners:
            leftover = []
            for scanner_to_align in unaligned_scanners:
                if not aligned_scanners:
                    aligned_scanners.append(scanner_to_align)
                    continue
                for scanner in aligned_scanners:
                    beacon_mapping = scanner_to_align.find_overlap(scanner)
                    if beacon_mapping:
                        scanner_to_align.align_according_to(scanner, beacon_mapping)
                        aligned_scanners.append(scanner_to_align)
                        break
                else:
                    leftover.append(scanner_to_align)
            unaligned_scanners = leftover

    def part_one(self, scanners: list[Scanner]) -> int:
        self.align_scanners(scanners)
        return len({tuple(beacon) for scanner in scanners for beacon in scanner.beacons})

    def part_two(self, scanners: list[Scanner]) -> int:
        self.align_scanners(scanners)
        scanner_positions = np.array([scanner.position for scanner in scanners])
        return int(distance_matrix(scanner_positions, scanner_positions, p=1).max())

Level().run()
