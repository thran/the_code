from oauth2client.util import positional

DIRECTIONS = {
    ">": (0, 1),
    "<": (0, -1),
    "^": (1, 0),
    "v": (-1, 0),
}

position = (0,0)
robo_position = (0,0)
path = [position]
robo_path = [position]

with open("03.txt") as source:
    for i, move in enumerate(source.read()):
        direction = DIRECTIONS[move]
        if i % 2 == 0:
            position = position[0] + direction[0], position[1] + direction[1]
            path.append(position)
        else:
            robo_position = robo_position[0] + direction[0], robo_position[1] + direction[1]
            robo_path.append(robo_position)

print path
print robo_path
print len(path), len(set(path)), len(robo_path), len(set(robo_path))
print len(set(robo_path + path))
