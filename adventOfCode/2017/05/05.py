jumps = []
with open('input.txt') as f:
    for line in f:
        jumps.append(int(line.strip()))

position = 0
steps = 0
while True:
    if position >= len(jumps):
        break
    steps += 1
    jump = jumps[position]
    if jump >= 3:
        jumps[position] -= 1
    else:
        jumps[position] += 1
    position += jump
    # print(position)

print(steps)
