import numpy as np

x = np.array([int(i) for i in open('input.txt').readlines()[0]])

# x = x.reshape((-1, 2, 2))
x = x.reshape((-1, 6, 25))
print(x.shape)

i = np.argmin((x == 0).sum(axis=(1, 2)))
print((x[i] == 1).sum() * (x[i] == 2).sum())


image = np.empty(x[0].shape, dtype=int)
image.fill(2)
for layer in x:
    image[image == 2] = layer[image == 2]

print(image)
