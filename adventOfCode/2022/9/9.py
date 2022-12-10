from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 88
    part_two_test_solution = 36

    def preprocess_input(self, lines):
        DIRECTION_MAP = {
            "L": (-1, 0),
            "R": (1, 0),
            "U": (0, 1),
            "D": (0, -1),
        }
        motions = []
        for line in lines:
            direction, steps = line.split()
            motions.append((DIRECTION_MAP[direction], int(steps)))
        return motions

    @staticmethod
    def follow(head, tail):
        if abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1:
            return

        for d in (0, 1):
            if abs(head[d] - tail[d]) > 0:
                tail[d] += 1 if head[d] > tail[d] else -1

    def part_one(self, motions) -> int:
        return self.part_two(motions, 2)

    def part_two(self, motions, knots=10) -> int:
        knots = [[0, 0] for _ in range(knots)]
        visited = {tuple(knots[-1])}
        for diff, steps in motions:
            for _ in range(steps):
                knots[0][0] += diff[0]
                knots[0][1] += diff[1]
                for i in range(len(knots) - 1):
                    self.follow(knots[i], knots[i + 1])
                visited.add(tuple(knots[-1]))
        return len(visited)


Level().run()
