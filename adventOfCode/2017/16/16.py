from tqdm import tqdm

dancers = list('abcdefghijklmnop')

with open('input.txt') as f:
    commands = f.readline().strip().split(',')

states = set()
for i in tqdm(range((10 ** 9) % 36)):
    state = ''.join(dancers)
    if state in states:
        print(i, state)
        break
    states.add(state)
    for command in commands:
        c, ps = command[0], command[1:]
        if c == 's':
            dancers = dancers[-int(ps):] + dancers[:-int(ps)]
        if c == 'x':
            p1, p2 = map(int, ps.split('/'))
            dancers[p1], dancers[p2] = dancers[p2], dancers[p1]
        if c == 'p':
            p1, p2 = ps.split('/')
            p1, p2 = dancers.index(p1), dancers.index(p2)
            dancers[p1], dancers[p2] = dancers[p2], dancers[p1]
        # print(command, dancers)

print(''.join(dancers))
