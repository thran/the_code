from black.trans import defaultdict

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 21
    part_two_test_solution = 40

    def preprocess_input(self, lines):
        splitters = []
        for line in lines[1:]:
            splitters.append(set(i for i, s in enumerate(line) if s == '^'))
        return lines[0].index('S'), splitters

    def part_one(self, start, splitters) -> int:
        splits = 0
        beams = {start}
        for row in splitters:
            splitting = beams & row
            beams -= splitting
            for splitter in splitting:
                beams.add(splitter - 1)
                beams.add(splitter + 1)
                splits += 1
        return splits

    def part_two(self, start, splitters) -> int:
        paths = defaultdict(int)
        paths[start] = 1
        for row in splitters:
            for splitter in row:
                count = paths[splitter]
                paths[splitter] = 0
                paths[splitter - 1] += count
                paths[splitter + 1] += count
        return sum(paths.values())


if __name__ == '__main__':
    Level().run()
