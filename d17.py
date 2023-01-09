import utils

m = utils.Opener.lines()
# m = utils.Opener.lines("input/d17_small.txt")

instructions = m[0]

shapes = [
    [(0, 2), (0, 3), (0, 4), (0, 5)],  # line
    [(2, 3), (1, 2), (1, 3), (1, 4), (0, 3)],  # cross
    [(0, 2), (0, 3), (0, 4), (1, 4), (2, 4)],  # L
    [(0, 2), (1, 2), (2, 2), (3, 2)],  # vert. line
    [(0, 2), (0, 3), (1, 2), (1, 3)],  # block
]


def fallen_rocks(until, grid=None):
    if grid is None:
        grid = {}

    def check_y(new_pos):
        return all(0 <= y <= 6 and (x, y) not in grid for (x, y) in new_pos)

    def check_x(new_pos):
        return all(x >= 0 and (x, y) not in grid for (x, y) in new_pos)

    highest = 0
    idx = 0
    fallen_rocks = 0
    s = 0
    pos = [(3 + highest + x, y) for x, y in shapes[s]]

    while fallen_rocks < until:  # + 245:  # 2565
        instr = instructions[idx]
        idx = (idx + 1) % len(instructions)
        if instr == ">":
            new_pos = [(x, y + 1) for x, y in pos]
            if check_y(new_pos):
                pos = new_pos
        if instr == "<":
            new_pos = [(x, y - 1) for x, y in pos]
            if check_y(new_pos):
                pos = new_pos

        new_pos = [(x - 1, y) for x, y in pos]
        if check_x(new_pos):
            pos = new_pos
        else:
            for (x, y) in pos:
                grid[x, y] = "#"
                highest = max(x + 1, highest)
            s = (s + 1) % len(shapes)
            pos = [(3 + highest + x, y) for x, y in shapes[s]]
            fallen_rocks += 1
    return highest

# star 1
print(fallen_rocks(2022))


# star 2 (using logic)

grid = {}
# < 1630 => 2581
# < 3365 => 5362
# < 5100 => 8143
print(fallen_rocks(5100, grid))
idxs = []  # (start, length)
for gx, gy in ((gx, gy) for gx, gy in grid if gy == 0):
    if idxs and idxs[-1][0] + idxs[-1][1] == gx:
        idxs[-1][1] += 1
    else:
        idxs.append([gx, 1])

ns = [(s, n) for s, n in idxs if n == 10] # pattern appears at n == 10

print(ns)  # => 2565
for i in range(1, len(ns)):
    print(ns[i][0] - ns[i-1][0])  # 2781
# every 1735 blocks, gains 2781 height

# < 1630 => 2581
# < 3365 => 5362
# < 5100 => 8143
# every 1735 blocks, gains 2781 height

target_rocks = 1_000_000_000_000

start_height = 2581
start = 1630

middle_height = ((target_rocks - 1630) // 1735) * 2781

end = (target_rocks - 1630) % 1735
first_stop = 3365
# fallen_rock(3365+end) - fallen_rock(3365)
# 5753 - 5362
end_height = fallen_rocks(first_stop + end) - fallen_rocks(first_stop)

print(start_height + middle_height + end_height)

