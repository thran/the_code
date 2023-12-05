from core import AdventOfCode


def batched(iterable, n: int):
    batch = []
    for element in iterable:
        batch.append(element)
        if len(batch) >= n:
            yield batch
            batch = []
    if len(batch) > 0:
        yield batch


class Level(AdventOfCode):
    part_one_test_solution = 35
    part_two_test_solution = 46

    def preprocess_input(self, lines):
        lines = iter(lines)
        seeds = list(map(int, next(lines).split(': ')[1].split()))
        next(lines)

        maps = []
        while True:
            if (map_name := next(lines, None)) is None:
                break
            ranges = []
            while lines and (line := next(lines, None)):
                destination, source, length = map(int, line.split())
                ranges.append((source, source + length - 1, destination - source))
            maps.append((map_name, ranges))

        return seeds, maps

    def part_one(self, seeds, maps) -> int:
        for _, ranges in maps:
            new_seeds = []
            for seed in seeds:
                for source_from, source_to, offset in ranges:
                    if source_from <= seed <= source_to:
                        new_seeds.append(seed + offset)
                        break
                else:
                    new_seeds.append(seed)
            seeds = new_seeds
        return min(seeds)

    def part_two(self, seeds, maps) -> int:
        seeds = list(batched(seeds, 2))
        seed_ranges = [(seed_from, seed_from + length - 1) for seed_from, length in seeds]
        for _, ranges in maps:
            new_seed_ranges = []
            while seed_ranges:
                seed_from, seed_to = seed_ranges.pop(0)
                for source_from, source_to, offset in ranges:
                    intersection_from, intersection_to = max(seed_from, source_from), min(seed_to, source_to)
                    if intersection_from > intersection_to:
                        continue
                    new_seed_ranges.append((intersection_from + offset, intersection_to + offset))
                    if seed_from < intersection_from:
                        seed_ranges.append((seed_from, intersection_from - 1))
                    if seed_to > intersection_to:
                        seed_ranges.append((intersection_to + 1, seed_to))
                    break
                else:
                    new_seed_ranges.append((seed_from, seed_to))
            seed_ranges = new_seed_ranges
        return min(seed_from for seed_from, seed_to in seed_ranges)


if __name__ == '__main__':
    Level().run()
