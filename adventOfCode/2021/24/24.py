from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 29
    part_two_test_solution = 18

    def preprocess_input(self, lines):
        instructions = []
        for line in lines:
            parts = line.split()
            instructions.append(tuple(int(p) if p.isnumeric() or p.startswith('-') else p for p in parts))
        return instructions

    def run_alu(self, instructions, input_):
        variables = {'x': 0, 'y': 0, 'z': 0, "w": 0}
        def get_value(var):
            if type(var) is int:
                return var
            return variables[var]

        input_read = 0
        for instruction in instructions:
            match instruction:
                case 'inp', a:
                    variables[a] = input_[input_read]
                    input_read += 1
                case 'add', a, b:
                    variables[a] = get_value(a) + get_value(b)
                case 'mul', a, b:
                    variables[a] = get_value(a) * get_value(b)
                case 'div', a, b:
                    variables[a] = int(get_value(a) / get_value(b))
                case 'mod', a, b:
                    variables[a] = get_value(a) % get_value(b)
                case 'eql', a, b:
                    variables[a] = int(get_value(a) == get_value(b))
        return variables

    # this is what blocks do
    def block(self, input_, z, v1, v2, v3):
        if v1 == 1:
            z = z * 26 + input_ + v3
        else:
            assert input_ == z % 26 + v2
            z = z // 26
        return z

    def block_as_list(self, input_, z, v1, v2, v3):
        if v1 == 1:
            z.append(input_ + v3)
        else:
            assert input_ == z.pop() + v2

    def find_pairs(self, instructions):
        block_length = 18
        block_count = len(instructions) // block_length
        blocks = [
            instructions[i * block_length: (i + 1) * block_length]
            for i in range(block_count)
        ]

        pairs = []
        stack = []
        for i, block in enumerate(blocks):
            v1, v2, v3 = block[4][-1], block[5][-1], block[15][-1]
            if v1 == 1:
                stack.append((i, v3))
            else:
                j, v = stack.pop()
                pairs.append((j, i, v + v2))
        assert not stack, stack
        return pairs

    def part_one(self, instructions) -> int:
        pairs = self.find_pairs(instructions)
        number = [0] * (len(pairs) * 2)
        for i, j, diff in pairs:
            n1 = min(9, 9 - diff)
            n2 = n1 + diff
            number[i] = n1
            number[j] = n2

        assert self.run_alu(instructions, number)['z'] == 0
        return int(''.join(map(str, number)))

    def part_two(self, instructions) -> int:
        pairs = self.find_pairs(instructions)
        number = [0] * (len(pairs) * 2)
        for i, j, diff in pairs:
            n2 = max(1, 1 + diff)
            n1 = n2 - diff
            number[i] = n1
            number[j] = n2

        assert self.run_alu(instructions, number)['z'] == 0
        return int(''.join(map(str, number)))


Level().run()
