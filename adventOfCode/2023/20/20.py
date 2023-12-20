from collections import deque, Counter
from functools import partial
from itertools import count
from math import lcm

from core import AdventOfCode


class Module:
    def __init__(self, name: str, outputs: list[str]):
        self.name = name
        self.outputs = outputs
        self.inputs = {}

    def set_input(self, name):
        self.inputs[name] = False

    def proces_pulse(self, source: str, pulse: bool) -> list[tuple[str, str, bool]]:
        ...

    def get_output_signals(self, pulse) -> list[tuple[str, str, bool]]:
        return [(self.name, o, pulse) for o in self.outputs]


class Broadcaster(Module):
    def proces_pulse(self, source: str, pulse):
        return self.get_output_signals(pulse)


class FlipFlop(Module):
    def __init__(self, *args):
        super().__init__(*args)
        self.state = False

    def proces_pulse(self, source: str, pulse: bool):
        if pulse:
            return []
        self.state = not self.state
        return self.get_output_signals(self.state)


class Conjunction(Module):
    def proces_pulse(self, source: str, pulse):
        self.inputs[source] = pulse
        if all(self.inputs.values()):
            return self.get_output_signals(False)
        return self.get_output_signals(True)


class Level(AdventOfCode):
    part_one_test_solution = 11687500
    part_two_test_solution = -1
    skip_tests = True

    def preprocess_input(self, lines):
        modules = {}
        for line in lines:
            module, outputs = line.split(' -> ')
            outputs = outputs.split(', ')
            if module == 'broadcaster':
                modules[module] = Broadcaster(module, outputs)
            operation, module = module[0], module[1:]
            if operation == '%':
                modules[module] = FlipFlop(module, outputs)
            if operation == '&':
                modules[module] = Conjunction(module, outputs)

        for module in modules.values():
            for output in module.outputs:
                if output in modules:
                    modules[output].set_input(module.name)
        return modules

    def simulate(self, modules, counter=None, signal_callback=None):
        signals = deque([('button', 'broadcaster', False)])
        while len(signals):
            source, target, pulse = signals.popleft()
            # print(f'{source} -{"high" if pulse else "low"}-> {target}')
            if counter is not None:
                counter[pulse] += 1
            if target not in modules:
                continue
            if signal_callback:
                signal_callback(source, target, pulse)
            signals.extend(modules[target].proces_pulse(source, pulse))

    def part_one(self, modules, iterations=1000) -> int:
        pulse_counter = Counter()
        for _ in range(iterations):
            self.simulate(modules, pulse_counter)
        return pulse_counter[False] * pulse_counter[True]

    def part_two(self, modules) -> int:
        final_module = [m for m in modules.values() if 'rx' in m.outputs][0]
        counters = {i: None for i in final_module.inputs}

        def _callback(i, source, _, pulse):
            if pulse and source in counters and counters[source] is None:
                counters[source] = i

        for i in count(1):
            self.simulate(modules, signal_callback=partial(_callback, i))
            if all(counters.values()):
                break

        return lcm(*counters.values())


if __name__ == '__main__':
    Level().run()
