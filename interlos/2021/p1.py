import numpy as np

numbers = [
    '',
    'jedna',
    'dva',
    'tri',
    'ctyri',
    'pet',
    'sest',
    'sedm',
    'osm',
    'devet',
    'deset',
    'jedenact',
    'dvanact',
    'trinact',
    'ctrnact',
    'patnact',
    'sestnact',
    'sedmnact',
    'osmnact',
    'devatenact',
]

tens = [
    '',
    '',
    'dvacet',
    'tricet',
    'ctyricet',
    'padesat',
    'sedesat',
    'sedmdesat',
    'osmdesat',
    'devadesat',
]


def number_to_str(n):
    if n == 100:
        return 'jedno sto'

    if n < 20:
        return numbers[n]

    n = str(n)
    s = ''
    if len(n) == 4:
        if n[0] == '1':
            s += 'jeden tisic '
        else:
            s += numbers[int(n[0])] + ' tisice '
        n = n[1:]
    if len(n) == 3:
        if n[0] != '0':
            if n[0] == '1':
                s += 'sto '
            elif n[0] == '2':
                s += 'dve ste '
            elif n[0] in '34':
                s += numbers[int(n[0])] + ' sta '
            else:
                s += numbers[int(n[0])] + ' set '
        n = n[1:]
    if int(n) < 20:
        return s + '' + number_to_str(int(n))

    return s + tens[int(n[0])] + ' ' + numbers[int(n[1])]


N = 2618

# print(number_to_str(100))

names = [number_to_str(n) for n in range(1, N + 1)]
for i, s in enumerate(sorted(names)):
    print(i+1, s)

good = np.arange(N)[np.argsort(names) == np.arange(N)] + 1
print(good)
print(''.join(map(str, good)
              ))
