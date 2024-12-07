import numpy as np
from tqdm import tqdm

from adventOfCode.utils import array, SmartArray
from core import AdventOfCode


class LevelSlow(AdventOfCode):
    part_one_test_solution = 41
    part_two_test_solution = 6

    DELTAS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def preprocess_input(self, lines):
        plan = np.array([list(l) for l in lines])
        [x], [y] = np.where(plan == '^')
        plan[x, y] = '.'
        return array(plan == '#'), (x, y)

    def go(self, plan, starting_position, direction):
        visited_positions = set()
        position = starting_position
        while True:
            if (position, direction) in visited_positions:
                looped = True
                break
            visited_positions.add((position, direction))
            new_position = SmartArray.change_position(position, self.DELTAS[direction])
            if not plan.is_valid_position(new_position):
                looped = False
                break
            if not plan[new_position]:
                position = new_position
            else:
                direction = (direction + 1) % 4
        return visited_positions, looped

    def part_one(self, plan: SmartArray, starting_position, direction=0) -> int:
        positions, looped = self.go(plan, starting_position, direction)
        assert not looped
        return len({p for p, d in positions})

    def part_two(self, plan: SmartArray, starting_position, direction=0) -> int:
        positions, _ = self.go(plan, starting_position, direction)

        result = 0
        for obstacle in tqdm({p for p, d in positions}):
            plan[obstacle] = True
            _, looped = self.go(plan, starting_position, direction)
            plan[obstacle] = False
            if looped:
                result += 1
        return result


class Level(LevelSlow):
    def find_end(self, plan, position, direction) -> tuple[int, int] | None:
        while True:
            new_position = SmartArray.change_position(position, self.DELTAS[direction])
            if not plan.is_valid_position(new_position):
                return
            if plan[new_position]:
                return position
            position = new_position

    def find_steps_for_obstacle(self, plan, obstacle):
        steps = {}
        for d, delta in enumerate(self.DELTAS):
            position = plan.change_position(obstacle, delta)
            if plan.is_valid_position(position):
                direction = (d - 1) % 4
                end = self.find_end(plan, position, direction)
                if end is not None:
                    steps[position, direction] = end, (direction + 1) % 4
        return steps

    def find_steps(self, plan, starting_position, direction):
        steps = {
            (starting_position, direction): (
                self.find_end(plan, starting_position, direction),
                (direction + 1) % 4,
            )
        }
        for obstacle in zip(*np.where(plan)):
            steps.update(self.find_steps_for_obstacle(plan, obstacle))

        return steps

    def part_two(self, plan: SmartArray, starting_position, direction=0) -> int:
        steps = self.find_steps(plan, starting_position, direction)
        positions, _ = self.go(plan, starting_position, direction)

        result = 0
        for obstacle in {p for p, d in positions}:
            tmp_steps = self.find_steps_for_obstacle(plan, obstacle)
            for i, d in enumerate(self.DELTAS):
                p = obstacle
                while True:
                    p = plan.change_position(p, d)
                    if plan.get(p, True):
                        break
                    possible_obs = plan.change_position(p, self.DELTAS[(i + 1) % 4])
                    if plan.get(possible_obs, False) or p == starting_position and i == 2:
                        tmp_steps[p, (i + 2) % 4] = (plan.change_position(obstacle, d), (i - 1) % 4)

            position = starting_position, direction
            visited = {position}
            while True:
                position = tmp_steps.get(position, steps.get(position))
                if position is None:
                    break
                if position in visited:
                    result += 1
                    break
                visited.add(position)

        return result


if __name__ == '__main__':
    Level().run()
