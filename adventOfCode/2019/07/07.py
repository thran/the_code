from itertools import permutations
from operator import itemgetter

from intcode import IntCode

memory = list(map(int, open('input.txt').readlines()[0].split(',')))


results = {}
for settings in permutations(range(5)):
    signal = 0
    for s in settings:
        amplifier = IntCode(memory.copy())
        signal = amplifier.run(inputs=[s, signal], print_outputs=False, halt_on_output=True)

    results[settings] = signal

print(max(results.items(), key=itemgetter(1)))

results = {}
for settings in permutations(range(5, 10)):
    amplifiers = [IntCode(memory.copy()) for _ in range(5)]
    signal = 0
    ended = False
    first = True
    while not ended:
        for a, s in zip(amplifiers, settings):
            if first:
                output = a.run(inputs=[s, signal], halt_on_output=True)
            else:
                output = a.run(inputs=[signal], halt_on_output=True)
            if output is None:
                ended = True
                break
            signal = output
        first = False

    results[settings] = signal

print(max(results.items(), key=itemgetter(1)))
