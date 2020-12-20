# start 10:25, 1. 10:44, 2. 11:57
from collections import defaultdict
from math import prod
from pathlib import Path

from parse import parse
import numpy as np

tiles = {}
with Path('input.txt').open() as file:
    while file:
        line = file.readline().strip()
        if not line:
            break
        tile_id = parse('Tile {:d}:', line)[0]
        tile = []
        while line := file.readline().strip():
            tile.append([c == '#' for c in line])
        tiles[tile_id] = np.array(tile)

monster = '''
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
'''
monster = np.array([[c == '#' for c in line] for line in monster.split('\n') if line])


def canonize(border, keep_orientation=False):
    if not keep_orientation:
        border = sorted((list(border), list(border[::-1])))[0]
    return ''.join(['#' if c else '.' for c in border])


def get_borders(tile):
    return (
        canonize(tile[0, :]),
        canonize(tile[-1, :]),
        canonize(tile[:, 0]),
        canonize(tile[:, -1]),
    )


def get_rotations(tile):
    for _ in range(2):
        for _ in range(4):
            tile = np.rot90(tile)
            yield tile
        tile = np.flip(tile, 0)


def orient(tile, top=None, left=None, ignore_orientation=False):
    for rotation in get_rotations(tile):
        t = canonize(rotation[0, :], not ignore_orientation)
        b = canonize(rotation[:, 0], not ignore_orientation)
        if (top is None or top == t) and (left is None or left == b):
            return rotation
    assert False


def print_tile(tile):
    for row in tile:
        print(''.join(['#' if c else '.' for c in row]))


borders = defaultdict(list)
for tile_id, tile in tiles.items():
    for border in get_borders(tile):
        borders[border].append(tile_id)
edges = {b for b, tids in borders.items() if len(tids) == 1}

corners = []
for tile_id, tile in tiles.items():
    edges_count = sum(1 for border in get_borders(tile) if border in edges)
    if edges_count == 2:
        corners.append(tile_id)
print(prod(corners))


photo = []
while True:
    if len(photo) == 0:
        last_head_id = last_id = corners[0]
        corner = tiles[last_id]
        es = [b for b in get_borders(corner) if b in edges]
        assert len(es) == 2
        last_head = last = orient(corner, top=es[0], left=es[1], ignore_orientation=True)
    else:
        last_head_id = last_id = list(set(borders[canonize(last_head[-1, :])]) - {last_head_id})[0]
        last_head = last = orient(tiles[last_id], top=canonize(last_head[-1, :], keep_orientation=True))
    row = [last]

    while (right := canonize(last[:, -1])) not in edges:
        last_id = list(set(borders[right]) - {last_id})[0]
        last = orient(tiles[last_id], left=canonize(last[:, -1], keep_orientation=True))
        row.append(last)

    photo.append(row)
    if canonize(last[-1, :]) in edges:
        break

photo = [
    [t[1:-1, 1:-1] for t in row]
    for row in photo
]
photo = np.concatenate([np.concatenate(row, axis=1) for row in photo])


mx, my = monster.shape
px, py = photo.shape
monsters = 0
for photo in get_rotations(photo):
    for x in range(px - mx):
        for y in range(py - my):
            view = photo[x:x + mx, y:y + my]
            if np.all(~monster | view):
                monsters += 1
    if monsters:
        break

print(photo.sum() - monsters * monster.sum())
