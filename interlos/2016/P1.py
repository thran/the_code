import math
import matplotlib.pylab as plt


def shift(angel, lenght):
    return math.cos(angel) * lenght, math.sin(angel) * lenght


def get_position(wheels):
    x, y = 0, 0
    for wheel in wheels:
        s = shift(angel=wheel[2], lenght=wheel[1])
        x += s[0]
        y += s[1]
    return x, y


def rotate(wheels, tick=0.02):
    for wheel in wheels:
        wheel[2] += wheel[0] * tick

wheels = []

with open('P1-input.txt') as f:
    for line in f.readlines():
        wheels.append(map(float, line[:-1].split(',')))

xs, ys = [], []

for step in range(1000):
    x, y = get_position(wheels)
    xs.append(x)
    ys.append(y)
    rotate(wheels)

plt.plot(xs, ys)
plt.show()
