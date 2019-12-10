from intcode import IntCode

memory = list(map(int, open('input.txt').readlines()[0].split(',')))

computer = IntCode(memory)
print(computer.run(inputs=[2], debug=False))
