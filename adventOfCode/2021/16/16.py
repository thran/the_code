import numpy as np

from core import AdventOfCode


class Packet:
    def __init__(self, data, pointer=0):
        self.data = data
        self.pointer = pointer
        self.version = None
        self.type = None
        self.payload = None
        self.parse()

    def _read(self, bits):
        read = self.data[self.pointer:self.pointer + bits]
        self.pointer += bits
        return int(read, 2)

    def parse(self):
        self.version = self._read(3)
        self.type = self._read(3)

        if self.type == 4:
            number = 0
            while True:
                end_bit = self._read(1)
                number = number * 2**4 + self._read(4)
                if end_bit == 0:
                    break
            self.payload = number
        else:
            self.payload = []
            self.lenght_type = self._read(1)
            if self.lenght_type == 0:
                length = self._read(15)
                while length:
                    sub_packet = Packet(self.data, self.pointer)
                    self.payload.append(sub_packet)
                    length -= sub_packet.pointer - self.pointer
                    self.pointer = sub_packet.pointer
            else:
                for _ in range(self._read(11)):
                    sub_packet = Packet(self.data, self.pointer)
                    self.payload.append(sub_packet)
                    self.pointer = sub_packet.pointer

    def value(self):
        if self.type == 4:
            return self.payload

        values = [p.value() for p in self.payload]

        match self.type:
            case 0:
                return sum(values)
            case 1:
                return np.product(values)
            case 2:
                return min(values)
            case 3:
                return max(values)
            case 5:
                return int(values[0] > values[1])
            case 6:
                return int(values[0] < values[1])
            case 7:
                return int(values[0] == values[1])

    def version_sum(self):
        if self.type == 4:
            return self.version
        else:
            return self.version + sum(p.version_sum() for p in self.payload)


class Level(AdventOfCode):
    part_one_test_solution = 20
    part_two_test_solution = 1

    def preprocess_input(self, lines):
        hex = lines[0]
        number = bin(int(hex, 16))[2:]
        zeros = '0' * (4 * len(hex) - len(number))
        return zeros + number

    def part_one(self, data) -> int:
        return Packet(data).version_sum()

    def part_two(self, data) -> int:
        return Packet(data).value()


Level().run()


