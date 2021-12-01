# start: :
# 1.:    :
# 2.:    :

from core import AdventOfCode


class Level(AdventOfCode):

    @property
    def part_one_test_solution(self):
        return None

    @property
    def part_two_test_solution(self):
        return None

    def part_one(self, depths) -> int:
        ...

    def part_two(self, depths) -> int:
        ...


Level().run()
