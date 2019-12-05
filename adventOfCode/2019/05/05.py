from intcode import intcode


memory = list(map(int, open('input.txt').readlines()[0].split(',')))
# memory[1] = noun
# memory[2] = verb
print(intcode(memory))

