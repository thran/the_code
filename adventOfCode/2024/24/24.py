from core import AdventOfCode


class Level(AdventOfCode):
    part_one_test_solution = 2024
    part_two_test_solution = 0
    skip_tests = True

    def preprocess_input(self, lines):
        split = lines.index('')
        inputs = {k: bool(int(v)) for k, v in map(lambda l: l.split(': '), lines[:split])}
        gates = {
            gr: (op, tuple(sorted((g1, g2)))) for g1, op, g2, _, gr in map(lambda l: l.split(' '), lines[split + 1 :])
        }
        return inputs, gates

    def eval(self, gates, inputs, outputs, return_values=False) -> int:
        values: dict[str, bool] = inputs

        def _get_value(gate) -> bool:
            if gate in values or gate[0] in 'xy':
                return values[gate]
            op, (input1, input2) = gates[gate]
            if op == 'OR':
                values[gate] = _get_value(input1) or _get_value(input2)
            elif op == 'AND':
                values[gate] = _get_value(input1) and _get_value(input2)
            elif op == 'XOR':
                values[gate] = _get_value(input1) ^ _get_value(input2)
            return values[gate]

        number = int(''.join(str(int(_get_value(g))) for g in reversed(outputs)), 2)
        if return_values:
            return number, values
        return number

    def part_one(self, inputs, gates) -> int:
        return self.eval(gates, inputs, [g for g in sorted(gates) if g[0] == 'z'])

    def part_two(self, inputs, gates) -> int:
        gate_names = {v: k for k, v in gates.items()}

        gates_sum = [None] * 45
        gates_sum_c = [None] * 45
        gates_z = [None] * 45
        gates_carry_c = [None] * 45
        gates_carry = [None] * 45

        swapped = set()

        def swap_gates(name1, name2):
            gate1, gate2 = gates[name1], gates[name2]
            gate_names[gate1], gate_names[gate2] = gate_names[gate2], gate_names[gate1]
            swapped.add(name1)
            swapped.add(name2)

        def find_gate(op, gate1, gate2):
            if type(gate1) is str:
                name1 = gate1
            else:
                name1 = gate_names[gate1]
            if type(gate2) is str:
                name2 = gate2
            else:
                name2 = gate_names[gate2]
            new_gate = (op, tuple(sorted((name1, name2))))
            if new_gate in gate_names:
                return new_gate

            candidates = []
            for (o, (g1, g2)), g in gate_names.items():
                if o == op and (g1 in new_gate[1] or g2 in new_gate[1]):
                    s1, s2 = {name1, name2}, {g1, g2}
                    candidates.append((tuple(s1 - s2)[0], tuple(s2 - s1)[0]))
            assert len(candidates) == 1
            swap_gates(*candidates[0])
            return find_gate(op, gate1, gate2)

        gates_z[0] = find_gate('XOR', f'x00', f'y00')
        assert gate_names[gates_z[0]] == 'z00'
        gates_carry[0] = find_gate('AND', 'x00', 'y00')
        for i in range(1, 44 + 1):
            gates_sum[i] = find_gate('XOR', f'x{i:02d}', f'y{i:02d}')
            gates_sum_c[i] = find_gate('AND', f'x{i:02d}', f'y{i:02d}')
            gates_z[i] = find_gate('XOR', gates_sum[i], gates_carry[i - 1])
            if gate_names[gates_z[i]] != f'z{i:02d}':
                swap_gates(gate_names[gates_z[i]], f'z{i:02d}')
            gates_carry_c[i] = find_gate('AND', gates_sum[i], gates_carry[i - 1])
            gates_carry[i] = find_gate('OR', gates_sum_c[i], gates_carry_c[i])
        assert gate_names[gates_carry[44]] == 'z45'

        assert len(swapped) == 8
        return ','.join(sorted(swapped))


if __name__ == '__main__':
    Level().run()
