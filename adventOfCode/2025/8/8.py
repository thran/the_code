import numpy as np

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 40
    part_two_test_solution = 25272

    def preprocess_input(self, lines):
        return np.array([list(map(int, line.split(','))) for line in lines])

    def get_closest_pairs(self, boxes):
        distances = np.linalg.norm(boxes[:, None] - boxes[None, :], axis=2)
        distances[np.tril_indices_from(distances)] = np.inf
        return np.array(np.unravel_index(np.argsort(distances, axis=None), distances.shape)).T

    def merge_circuits(self, box1, box2, circuits):
        circuit1, circuit2 = None, None
        for circuit in circuits:
            if box1 in circuit:
                circuit1 = circuit
            if box2 in circuit:
                circuit2 = circuit
            if circuit1 and circuit2:
                break
        if circuit1 == circuit2:
            return
        circuits.remove(circuit1)
        circuits.remove(circuit2)
        circuits.append(circuit1 | circuit2)

    def part_one(self, boxes) -> int:
        count = 1000 if len(boxes) > 100 else 10
        circuits = [{i} for i in range(len(boxes))]
        for box1, box2 in self.get_closest_pairs(boxes)[:count]:
            self.merge_circuits(box1, box2, circuits)

        return np.prod(sorted(map(len, circuits))[-3:])

    def part_two(self, boxes) -> int:
        circuits = [{i} for i in range(len(boxes))]
        for box1, box2 in self.get_closest_pairs(boxes):
            self.merge_circuits(box1, box2, circuits)
            if len(circuits) == 1:
                return boxes[box1][0] * boxes[box2][0]

        assert False


if __name__ == '__main__':
    Level().run()
