import math


def value(w):
    val = 0
    for l in w:
        val += ord(l) - ord("A") + 1
    return val


def is_triangle_number(n):
    x = int(math.sqrt(2 * n))
    return x*(x+1)/2 == n

hits = 0
with open("042 - words.txt") as f:
    for w in f.readline().replace('"',"").split(","):
        if is_triangle_number(value(w)):
            hits += 1
            print w, value(w)

print hits
