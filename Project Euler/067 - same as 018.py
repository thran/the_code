
triangle = ([map(int, line.split()) for line in open("067_triangle.txt").readlines()])

# print triangle

maxs = [[0, triangle[0][0], 0]]
for line_number in range(1, len(triangle)):
    m_line = [0]
    for position in range(line_number+1):
        m = max(maxs[line_number-1][position], maxs[line_number-1][position+1])
        m_line.append(triangle[line_number][position] + m)

    maxs.append(m_line+[0])
print max(maxs[-1])
__author__ = 'xrihak1'
