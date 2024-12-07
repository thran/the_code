from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 3749
    part_two_test_solution = 11387

    def preprocess_input(self, lines):
        equations = []
        for line in lines:
            result, numbers = line.split(':')
            numbers = tuple(map(int, numbers.split()))
            equations.append((int(result), numbers))

        return equations

    def can_be_valid(self, result, numbers, third=False) -> bool:
        sub_results = [numbers[0]]
        for n in numbers[1:]:
            new_sub_results = []
            for sr in sub_results:
                for nsr in (sr + n, sr * n):
                    if nsr <= result:
                        new_sub_results.append(nsr)
                if third:
                    join = int(str(sr) + str(n))
                    if join <= result:
                        new_sub_results.append(join)
            sub_results = new_sub_results
        return result in sub_results

    def part_one(self, equations, third=False) -> int:
        solution = 0
        for result, numbers in equations:
            if self.can_be_valid(result, numbers, third):
                solution += result
        return solution

    def part_two(self, equations) -> int:
        return self.part_one(equations, True)


if __name__ == '__main__':
    Level().run()
