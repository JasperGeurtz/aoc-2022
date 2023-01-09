import utils

m = utils.Opener.lines("input/d22.txt")
# m = utils.Opener.lines("input/d22_small.txt")

line = m[-1].split("R")
q = line[0].split("L")
qq = [q[0]]
for b in q[1:]:
    qq += ["L"] + [b]
commands = qq
# print(commands)
# exit()
for l in line[1:]:
    q = l.split("L")
    qq = [q[0]]
    for b in q[1:]:
        qq += ["L"] + [b]
    commands += ["R"] + qq
print(commands)

# exit()

grid = {}
for row, line in enumerate(m[:-1]):
    for col, c in enumerate(line):
        if c != " ":
            grid[row, col] = c

position = min((i, j) for i, j in grid if i == 0)
d = 0

# utils.print_grid(grid)
print(position)
print(commands)

rotate = ((0, 1), (1, 0), (0, -1), (-1, 0))

for c in commands:
    print(c)
    if c == "R":
        d = (d + 1) % len(rotate)
    elif c == "L":
        d = d - 1
        if d == -1:
            d = 3
    else:
        n = int(c)
        print(f'{n=}')
        p_row, p_col = position
        for i in range(n):
            pi, pj = p_row + rotate[d][0],  p_col + rotate[d][1]
            if (pi, pj) not in grid:
                # based on rotation:
                if d == 0:
                    gi, gj = min((i, j) for i, j in grid if i == pi)
                elif d == 1:
                    gi, gj = min((i, j) for i, j in grid if j == pj)
                elif d == 2:
                    gi, gj = max((i, j) for i, j in grid if i == pi)
                elif d == 3:
                    gi, gj = max((i, j) for i, j in grid if j == pj)
                else:
                    raise Exception("not implemented")
                if grid[gi, gj] == "#":
                    break
                else:
                    p_row, p_col = gi, gj
            elif grid[pi, pj] == "#":
                break
            elif grid[pi, pj] == ".":
                p_row, p_col = pi, pj
            else:
                raise Exception(f"{n=}, {pi, pj}")

            print(pi, pj)
        position = p_row, p_col
        print(f"{position=}")
        # exit()
            # grid[]

# print()
print((position[0] + 1) * 1000 + (position[1] + 1) * 4 + d)