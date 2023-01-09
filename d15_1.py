import utils

m = utils.Opener.lines("input/d15.txt")


grid = {}
ty = 2000000
used = set()

for line in m:
    si, sj, bi, bj = line.split("=")[1:]
    si, sj, bi, bj = map(int, (si.split(",")[0], sj.split(":")[0], bi.split(",")[0], bj))
    grid[si, sj] = "S"
    grid[bi, bj] = "B"

for line in m:
    si, sj, bi, bj = line.split("=")[1:]
    si, sj, bi, bj = map(int, (si.split(",")[0], sj.split(":")[0], bi.split(",")[0], bj))
    d = utils.manhattan((si, sj), (bi, bj))

    down = sj - ty
    print(down)
    over = d - abs(down)
    for y in range(si+-over, si+over+1):
        if (y, ty) not in grid:
            used.add(y)

print(len(used))
