
def is_wall(x, y, number=1364):
    if x < 0 or y < 0:
        return True
    n = x*x + 3*x + 2*x*y + y + y*y + number
    return sum([b == '1' for b in str(bin(n))[2:]]) % 2 == 1

visited = {(1, 1)}
current = [(1, 1)]

target = (31, 39)

for i in range(50):
    new = []
    for x, y in current:
        for dx, dy in [(1, 0), (0, -1),(0, 1),(-1, 0)]:
            nx, ny = x + dx, y + dy
            if not is_wall(nx, ny) and (nx, ny) not in visited:
                new.append((nx, ny))
                visited.add((nx, ny))
    current = new

print(len(visited))

# for y in range(40):
#     line = ''
#     for x in range(40):
#         line += '# ' if is_wall(x, y) else 'o ' if (x, y ) in visited else '. '
#     print(line)
