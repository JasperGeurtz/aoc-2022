import utils

m = utils.Opener.lines()

cave = {}

for line in m:
    coords = list(map(eval, line.split(" -> ")))
    for i in range(1, len(coords)):
        prev, curr = coords[i - 1:i + 1]
        t = 1 if prev[0] == curr[0] else 0
        d = 1 if prev[t] < curr[t] else -1
        for q in range(0, curr[t] - prev[t] + d, d):
            cave[prev[0] + q * (t == 0), prev[1] + q * (t == 1)] = "#"

lowest = max([x[1] for x in cave])

start = (500, 0)
grains = 0

star1 = 0
star2 = 0

while True:
    si, sj = start
    while sj <= lowest:
        if (si, sj + 1) in cave:
            if (si - 1, sj + 1) not in cave:
                si, sj = si - 1, sj + 1  # move diag left
            elif (si + 1, sj + 1) not in cave:
                si, sj = si + 1, sj + 1  # move diag right
            else:
                break  # rest
        else:
            sj += + 1  # drop 1 down

    if not star1 and sj > lowest:
        star1 = grains

    cave[si, sj] = "O"
    grains += 1
    if (si, sj) == start:
        star2 = grains
        break

print(star1)
print(star2)
# print(utils.print_grid(cave))
utils.save_image(cave, "cave_d14.png", {"O": 128, "#": 255})
