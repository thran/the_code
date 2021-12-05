from utils import memoize
from icecream import ic

leaders = {
    3: 18,
    6: 23,
    15: 30,
    27: 39,
    38: 53,
    34: 49,

    4: 1,
    22: 7,
    26: 12,
    35: 19,
    40: 24,
    45: 42,
    48: 32,
}

loss = {2, 11, 14, 21, 29, 27, 50, 51}


def solution_value(solution):
    return len(solution), sum(solution)


in_process = set()

@memoize
def solve(position, steps):
    if (position, steps) in in_process:
        return
    in_process.add((position, steps))

    solutions = []

    if position + steps >= 55:
        return (55 - position, )

    for step in list(range(1, steps + 1))[::-1]:
        new_position = position + step
        if new_position in leaders:
            new_position = leaders[new_position]
        solution = solve(new_position, steps + int(new_position in loss))
        if solution:
            solutions.append((step,) + solution)

    if not solutions:
        return
    best = min(solutions, key=solution_value)
    return best

print(sum(solve(0, 1)))
