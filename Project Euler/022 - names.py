names = open("022 - names.txt").readline().replace("\"", "").split(',')
names.sort()


def to_number(letter):
    return ord(letter.lower()) - ord("a") + 1

suma = 0
for i, name in enumerate(names):
    suma += sum(map(to_number, name)) * (i+1)

print suma
