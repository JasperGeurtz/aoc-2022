import utils

m = utils.Opener.lines("input/d22.txt")
# m = utils.Opener.lines("input/d22_small.txt")

line = m[-1].split("R")
q = line[0].split("L")
qq = [q[0]]
for b in q[1:]:
    qq += ["L"] + [b]
commands = qq

for l in line[1:]:
    q = l.split("L")
    qq = [q[0]]
    for b in q[1:]:
        qq += ["L"] + [b]
    commands += ["R"] + qq
print(commands)

grid = {}

max_row = 0
max_col = 0
for row, line in enumerate(m[:-1]):
    max_row = max(row, max_row)
    for col, c in enumerate(line):
        max_col = max(col, max_col)
        if c != " ":
            grid[row, col] = c

position = min((i, j) for i, j in grid if i == 0)
d = 0

rotate = ((0, 1), (1, 0), (0, -1), (-1, 0))

cube_size = 50

cube_toplefts = []
for i in range(0, max_row, cube_size):
    for j in range(0, max_col, cube_size):
        if (i, j) in grid:
            cube_toplefts.append((i, j))

big_cubes = {
    (0, 50): {
        2: lambda r, c: (149 - r, 0, 0), # (ROW, COL, DIR)
        3: lambda r, c: (c+100, 0, 0),
    },
    (0, 100): {
        0: lambda r, c: (149-r, 99, 2),
        1: lambda r, c: (c-50, 99, 2),
        3: lambda r, c: (199, c - 100, 3),
    },
    (50, 50): {
        0: lambda r, c: (49, r+50, 3),
        2: lambda r, c: (100, r-50, 1),
    },
    (100, 0): {
        2: lambda r, c: (149-r, 50, 0),
        3: lambda r, c: (c+50, 50, 0),
    },
    (100, 50): {
        0: lambda r, c: (149-r, 149, 2),
        1: lambda r, c: (c+100, 49, 2),
    },
    (150, 0): {
        0: lambda r, c: (149, r-100, 3),
        1: lambda r, c: (0, c+100, 1),
        2: lambda r, c: (0, r-100, 1),
    },
}
def shift(i, j, d):
    for r, c in cube_toplefts:
        if r <= i < r + cube_size and c <= j < c + cube_size:
            res = big_cubes[r, c][d](i, j)
            return res
    raise Exception(f"Not implemented for: {(i, j, d)}")


for c in commands:
    if c == "R":
        d = (d + 1) % len(rotate)
    elif c == "L":
        d = d - 1
        if d == -1:
            d = 3
    else:
        n = int(c)
        p_row, p_col = position
        for i in range(n):
            pi, pj = p_row + rotate[d][0], p_col + rotate[d][1]
            if (pi, pj) not in grid:
                # based on cube rotation:
                gi, gj, gd = shift(p_row, p_col, d)
                if grid[gi, gj] == "#":
                    break
                else:
                    p_row, p_col, d = gi, gj, gd
            elif grid[pi, pj] == "#":
                break
            elif grid[pi, pj] == ".":
                p_row, p_col = pi, pj
            else:
                raise Exception(f"{n=}, {pi, pj}")

        position = p_row, p_col

print((position[0] + 1) * 1000 + (position[1] + 1) * 4 + d)
