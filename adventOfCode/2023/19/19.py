from numpy import product

from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 19114
    part_two_test_solution = 167409079868000

    def preprocess_input(self, lines):
        workflows = {}
        while line := lines.pop(0):
            name, rest = line.split('{')
            rules = []
            for r in rest[:-1].split(','):
                if '<' in r or '>' in r:
                    rules.append((r[0], r[1], int(r[2:].split(':')[0]), r[2:].split(':')[1]))
                else:
                    rules.append(r)
            workflows[name] = rules

        parts = []
        for line in lines:
            parts.append({p[0]: int(p[2:]) for p in line[1:-1].split(',')})
        return workflows, parts

    @staticmethod
    def eval_workflow(part, workflow) -> str:
        for condition in workflow:
            if isinstance(condition, str):
                return condition
            d, operation, value, name = condition
            if operation == '>':
                if part[d] > value:
                    return name
            if operation == '<':
                if part[d] < value:
                    return f'{name}'
        assert False

    @staticmethod
    def eval_cube_workflow(cube, workflow) -> list[tuple[dict, str]]:
        new_cubes = []
        for condition in workflow:
            if isinstance(condition, str):
                new_cubes.append((cube, condition))
                break
            dim, operation, value, name = condition
            if operation == '>':
                if value < cube[dim][1]:
                    if value < cube[dim][0]:
                        new_cubes.append((cube, name))
                        break
                    new_cubes.append(({d: ((value + 1, v2) if d == dim else (v1, v2)) for d, (v1, v2) in cube.items()}, name))  # fmt: skip
                    cube = {d: ((v1, value) if d == dim else (v1, v2)) for d, (v1, v2) in cube.items()}
            if operation == '<':
                if value > cube[dim][0]:
                    if value > cube[dim][1]:
                        new_cubes.append((cube, name))
                        break
                    new_cubes.append(({d: ((v1, value - 1) if d == dim else (v1, v2)) for d, (v1, v2) in cube.items()}, name))  # fmt: skip
                    cube = {d: ((value, v2) if d == dim else (v1, v2)) for d, (v1, v2) in cube.items()}
        return new_cubes

    def part_one(self, workflows, parts) -> int:
        result = 0
        for part in parts:
            current = 'in'
            while (current := self.eval_workflow(part, workflows[current])) not in 'RA':
                pass
            if current == 'A':
                result += sum(part.values())
        return result

    def part_two(self, workflows, parts) -> int:
        to_process = [({'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}, 'in')]
        count = 0
        while to_process:
            cube, workflow_name = to_process.pop()
            if workflow_name == 'R':
                continue
            if workflow_name == 'A':
                count += product([b - a + 1 for a, b in cube.values()])
                continue
            to_process.extend(self.eval_cube_workflow(cube, workflows[workflow_name]))

        return count


if __name__ == '__main__':
    Level().run()
