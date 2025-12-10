from itertools import product
from scipy.optimize import linprog

import numpy as np

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 7
    part_two_test_solution = 33

    def preprocess_input(self, lines):
        machines = []
        for line in lines:
            lights, *buttons_list, joltage = line.split()
            lights = np.array([l == '#' for l in lights[1:-1]])
            buttons = np.zeros((len(buttons_list), len(lights)), dtype=int)
            for i, b in enumerate(buttons_list):
                buttons[i, tuple(map(int, b[1:-1].split(',')))] = 1
            joltage = np.array(list(map(int, joltage[1:-1].split(','))))
            machines.append((lights, buttons, joltage))
        return machines

    def part_one(self, machines) -> int:
        s = 0
        for lights, buttons, _ in machines:
            for c in sorted(product(*[[0, 1]] * len(buttons)), key=sum):
                if (np.dot(np.array(c), buttons) % 2 == lights).all():
                    s += sum(c)
                    break
        return s

    def solve_slow(self, buttons, joltage):
        if (joltage == 0).all():
            return np.zeros(len(buttons), dtype=int)
        if not len(buttons):
            return None
        interesting_positions = buttons.sum(axis=0) > 0
        if (joltage[~interesting_positions] > 0).any():
            return None

        if len(buttons) <= (interesting_positions).sum():
            if not interesting_positions.all() and joltage[~interesting_positions].max() > 0:
                return None
            A = buttons[:, interesting_positions].T[: len(buttons)]
            b = joltage[interesting_positions][: len(buttons)]
            try:
                solution = np.linalg.solve(A, b)
                int_solution = np.round(solution).astype(int)
                if (int_solution < 0).any() or (buttons.T @ int_solution != joltage).any():
                    return None
                return int_solution
            except np.linalg.LinAlgError:
                if np.linalg.matrix_rank(A) < np.linalg.matrix_rank(np.column_stack((A, b))):
                    return None

        if (buttons.sum(axis=0) == 1).any():
            position = (buttons.sum(axis=0) == 1).argmax()
            button_index = buttons[:, position].argmax()
            presses = joltage[position]
            if (joltage - presses * buttons[button_index] < 0).any():
                return None
            presses_options = [presses]
        else:
            positions_to_handle = buttons.sum(axis=0) == buttons.sum(axis=0).min()
            possible_buttons = buttons[:, positions_to_handle].sum(axis=1) > 0
            button_index = (buttons.sum(axis=1) * possible_buttons).argmax()
            presses_options = range(joltage[buttons[button_index] == 1].min(), -1, -1)

        solutions = []
        new_buttons = np.delete(buttons, button_index, axis=0)

        for presses in presses_options:
            new_joltage = joltage - presses * buttons[button_index]
            solution = self.solve_slow(new_buttons, new_joltage)
            if solution is not None:
                solution = np.insert(solution, button_index, presses)
                solutions.append(solution)

        if solutions:
            return min(solutions, key=np.sum)

        return None

    def solve(self, buttons, joltage):
        return (
            linprog(
                c=np.ones(len(buttons)),
                A_eq=buttons.T,
                b_eq=joltage,
                bounds=(0, None),
                integrality=1,
                options={"presolve": False}
                # method='simplex',
            )
            .x.round()
            .astype(int)
        )

    def part_two(self, machines) -> int:
        return sum(self.solve(buttons, joltage).sum() for _, buttons, joltage in machines)


if __name__ == '__main__':
    Level().run()


# 16278 low
# 18202 high
