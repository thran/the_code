from collections import defaultdict, deque

import numpy as np

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 1928
    part_two_test_solution = 2858

    def preprocess_input(self, lines):
        files, spaces = [], []
        for i, n in enumerate(lines[0]):
            if i % 2 == 0:
                files.append((i // 2, int(n)))
            else:
                spaces.append(int(n))
        return files, spaces

    def part_one(self, files, spaces) -> int:
        def _gen_from_back():
            for fid, size in reversed(files):
                for _ in range(size):
                    yield fid

        def _gen_disk():
            from_back = _gen_from_back()
            for (fid, size), space_size in zip(files, spaces):
                for _ in range(size):
                    yield fid
                for _ in range(space_size):
                    yield next(from_back)

        result = 0
        disk = _gen_disk()
        for i in range(sum(s for fid, s in files)):
            result += i * next(disk)

        return result

    def part_two(self, files, spaces) -> int:
        disk = np.zeros(sum(s for fid, s in files) + sum(spaces), dtype=int)
        free_spaces = deque()
        file_positions = {}
        position = 0
        for (fid, size), space_size in zip(files, spaces + [0]):
            disk[position : position + size] = fid
            if space_size:
                free_spaces.append((space_size, position + size))
            file_positions[fid] = position, size
            position += size + space_size

        for fid, (position, size) in reversed(tuple(file_positions.items())):
            free_spaces_to_return = deque()
            while free_spaces:
                free_size, free_position = free_spaces.popleft()
                free_spaces_to_return.appendleft((free_size, free_position))
                if free_position >= position:
                    break
                if free_size < size:
                    continue
                disk[free_position : free_position + size] = fid
                disk[position : position + size] = 0
                free_spaces_to_return.popleft()
                if free_size > size:
                    free_spaces_to_return.appendleft((free_size - size, free_position + size))
                break
            free_spaces.extendleft(free_spaces_to_return)

        return (disk * np.arange(len(disk))).sum()


if __name__ == '__main__':
    Level().run()
