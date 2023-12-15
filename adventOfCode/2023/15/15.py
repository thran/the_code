from collections import defaultdict

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 1320
    part_two_test_solution = 145

    def preprocess_input(self, lines):
        return lines[0].split(',')

    @staticmethod
    def hash(string):
        current = 0
        for s in string:
            current += ord(s)
            current *= 17
            current %= 256
        return current

    def part_one(self, instructions) -> int:
        return sum(self.hash(i) for i in instructions)

    def part_two(self, instructions) -> int:
        boxes = defaultdict(dict)
        for instruction in instructions:
            if '-' in instruction:
                label = instruction[:-1]
                box = boxes[self.hash(label)]
                if label in box:
                    del box[label]
            else:
                label, lens = instruction.split('=')
                boxes[self.hash(label)][label] = int(lens)

        return sum(
            sum((1 + i) * j * l for j, l in enumerate(box.values(), start=1))
            for i, box in boxes.items()
        )  # fmt: skip


if __name__ == '__main__':
    Level().run()
