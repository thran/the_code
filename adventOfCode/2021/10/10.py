from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 26397
    part_two_test_solution = 288957

    pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }
    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    points2 = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }

    def process_line(self, line, illegal=False):
        stack = []
        for char in line:
            if char in self.pairs:
                stack.append(char)
                continue
            if self.pairs[stack.pop()] != char:
                if illegal:
                    return self.points[char]
                return
        if illegal:
            return 0

        score = 0
        for i, char in enumerate(stack):
            score += 5 ** i * self.points2[self.pairs[char]]
        return score

    def part_one(self, lines) -> int:
        points = 0
        for line in lines:
            points += self.process_line(line, illegal=True)
        return points

    def part_two(self, lines) -> int:
        scores = []
        for line in lines:
            score = self.process_line(line)
            if score:
                scores.append(score)
        assert len(scores) % 2 == 1
        return sorted(scores)[len(scores) // 2]


Level().run()
