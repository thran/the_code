from math import gcd

from tqdm import tqdm

class Moon:
    def __init__(self, x, y, z):
        self.sx, self.sy, self.sz = self.x, self.y, self.z = x, y, z
        self.dx, self.dy, self.dz = 0, 0, 0

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.z += self.dz

    def apply_gravity(self, moons):
        for moon in moons:
            if moon.x > self.x: self.dx += 1
            if moon.x < self.x: self.dx -= 1
            if moon.y > self.y: self.dy += 1
            if moon.y < self.y: self.dy -= 1
            if moon.z > self.z: self.dz += 1
            if moon.z < self.z: self.dz -= 1

    def __str__(self):
        return f'x:{self.x}, y:{self.y}, z:{self.z}'

    def is_returned(self, coordinate):
        return getattr(self, coordinate) == getattr(self, 's' + coordinate) and getattr(self, 'd' + coordinate) == 0

    def energy(self):
        return (abs(self.x) + abs(self.y) + abs(self.z)) * (abs(self.dx) + abs(self.dy) + abs(self.dz))


moons1 = [
    Moon(-1, 0, 2),
    Moon( 2, -10, -7),
    Moon( 4, -8, 8),
    Moon( 3, 5, -1),
]

moons2 = [
    Moon(-8, -10, 0),
    Moon( 5, 5, 10),
    Moon( 2, -7, 3),
    Moon( 9, -8, -3),
]

moons3 = [
    Moon(-10, -10, -13),
    Moon( 5, 5, -9),
    Moon( 3, 8, -16),
    Moon( 1, 3, -3),
]

moons = moons3
# steps = 1000
# for _ in range(steps):

i = 0
coordinates_cycle = {}
while len(coordinates_cycle) < 3:
    i += 1
    for moon in moons:
        moon.apply_gravity(moons)
    for moon in moons:
        moon.move()
    for coordinate in 'xyz':
        if coordinate in coordinates_cycle:
            continue
        if all([m.is_returned(coordinate) for m in moons]):
            coordinates_cycle[coordinate] = i
            print(coordinate, i)

# for moon in moons:
#     print(moon)

# print(sum(m.energy() for m in moons))
x, y, z = coordinates_cycle.values()
a = int(x * y / gcd(x, y))
b = a * z / gcd(a, z)
print(b)
