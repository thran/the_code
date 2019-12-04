from intcode import intcode

def run(verb, noun):
    memory = list(map(int, open('input.txt').readlines()[0].split(',')))
    memory[1] = noun
    memory[2] = verb
    return intcode(memory)[0]

for verb in range(100):
    for noun in range(100):
        if run(verb, noun) == 19690720:
            print(100 * noun + verb)
