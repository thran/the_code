from collections import defaultdict


severity = 0

with open('input.txt') as f:
    for line in f:
        layer, range = map(int, line.strip().split(': '))
        if layer % ((range - 1) * 2) == 0:
            severity += range * layer

print(severity)


layers = {}
with open('input.txt') as f:
    for line in f:
        layer, range = map(int, line.strip().split(': '))
        layers[layer] = range

delay = 0
items = sorted(layers.items(), key=lambda x: x[1])
while True:
    for layer, range in items:
        if (layer + delay) % ((range - 1) * 2) == 0:
            delay += 1
            break
    else:
        break

print(delay)

