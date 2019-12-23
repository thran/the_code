class IntCode:
    def __init__(self, memory):
        self.memory = memory
        self.pointer = 0
        self.relative_base = 0
        self.steps = 0

    def get_value(self, index, mode):
        if mode == 0:
            index = self.memory[index]
        if mode == 2:
            index = self.relative_base + self.memory[index]
        if index >= len(self.memory):
            return 0
        return self.memory[index]

    def set_value(self, index, mode, value):
        if mode == 0:
            index = self.memory[index]
        if mode == 2:
            index = self.relative_base + self.memory[index]
        if index >= len(self.memory):
            self.memory += [0] * (index - len(self.memory) + 1)
        self.memory[index] = value

    def run(self, debug=False, inputs=None, print_outputs=False, halt_on_output=False, halt_on_missing_input=False):
        if inputs:
            inputs = iter(inputs)
        outputs = []
    
        while True:
            self.steps += 1
            instruction = self.memory[self.pointer]
            opcode = instruction % 100
            modes = list(map(int, str(instruction)[:-2][::-1])) + [0] * 3
            if opcode == 1:
                value = self.get_value(self.pointer + 1, modes[0]) + self.get_value(self.pointer + 2, modes[1])
                self.set_value(self.pointer + 3, modes[2], value)
                self.pointer += 4
            elif opcode == 2:
                value = self.get_value(self.pointer + 1, modes[0]) * self.get_value(self.pointer + 2, modes[1])
                self.set_value(self.pointer + 3, modes[2], value)
                self.pointer += 4
            elif opcode == 3:
                if inputs:
                    try:
                        value = next(inputs)
                    except StopIteration:
                        if halt_on_missing_input:
                            return outputs
                        raise Exception('Missing inputs')
                else:
                    value = int(input('Inser value: '))
                self.set_value(self.pointer + 1, modes[0], value)
                self.pointer += 2
            elif opcode == 4:
                output = self.get_value(self.pointer + 1, modes[0])
                if print_outputs:
                    print('output: ', output)
                self.pointer += 2
                if halt_on_output:
                    return output
                outputs.append(output)
            elif opcode == 5:
                if self.get_value(self.pointer + 1, modes[0]) != 0:
                    self.pointer = self.get_value(self.pointer + 2, modes[1])
                else:
                    self.pointer += 3
            elif opcode == 6:
                if self.get_value(self.pointer + 1, modes[0]) == 0:
                    self.pointer = self.get_value(self.pointer + 2, modes[1])
                else:
                    self.pointer += 3
            elif opcode == 7:
                value = 1 if self.get_value(self.pointer + 1, modes[0]) < self.get_value(self.pointer + 2, modes[1]) else 0
                self.set_value(self.pointer + 3, modes[2], value)
                self.pointer += 4
            elif opcode == 8:
                value = 1 if self.get_value(self.pointer + 1, modes[0]) == self.get_value(self.pointer + 2, modes[1]) else 0
                self.set_value(self.pointer + 3, modes[2], value)
                self.pointer += 4
            elif opcode == 9:
                self.relative_base += self.get_value(self.pointer + 1, modes[0])
                self.pointer += 2
            elif opcode == 99:
                if halt_on_output:
                    return None
                return outputs
            else:
                assert False, f'invalid opcode {opcode}'
            if debug:
                print(self.pointer, self.relative_base, self.memory)
