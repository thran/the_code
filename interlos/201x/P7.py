import numpy as np


mat = np.zeros((3125, 2673))

# with open("in.txt") as f:
#     for x, line in enumerate(f.readlines()):
#         print x
#         for y, p in enumerate(line[:-2]):
#             mat[x, y] = ord(p) - 65
#
# np.save(open("mat.npy", "w"), mat)
# [p=='*' for p in l]
letters = [list(l) for l in
           [
".*.**..*.**.******",
"*.**.**.**.**..*..",
"*****.*..*.***.**.",
"*.**.**.**.**..*..",
"*.***..*.**.****..",]
]

letters = np.array(letters) == "*"

def let(l, letters):
    for i in range(6):
        for j in range(6):
            if np.all(letters[:,j*3:j*3+3] == (l==i)):
                return j

mat = np.load("mat.npy")

while min(mat.shape) > 1:
    new = np.zeros((mat.shape[0]/5, mat.shape[1]/3))

    for x in range(0, mat.shape[0]/5):
        print x
        for y in range(0, mat.shape[1]/3):
            l = mat[5*x:5*x+5, 3*y:3*y+3]
            new[x,y] = let(l, letters)
    print new.shape
    mat = new

print mat
