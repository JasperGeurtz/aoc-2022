import time
from functools import cache

import utils

m = utils.Opener.lines("input/d16.txt")
# m = utils.Opener.lines("input/d16_small.txt")

cave = {}

for line in m:
    a, c = line.split("to valve")
    a, b = a.split(" has flow rate=")
    valve = a.split(" ")[1]
    flow = int(b.split(";")[0])
    target = "".join(c.split(" ")[1:]).split(",")
    print(valve, flow, target)
    cave[valve] = (flow, target)


@cache
def resolve(position, timeleft, opened):
    if timeleft == 1:
        return 0

    best = float('-inf')
    if position not in opened and cave[position][0] > 0:
        best = max(best, cave[position][0] + resolve(position, timeleft - 1, opened + position))

    for t in cave[position][1]:
        best = max(best, resolve(t, timeleft - 1, opened))

    return best + (sum(cave[opened[i:i + 2]][0] for i in range(0, len(opened), 2)) if opened else 0)

t = time.time()
print(resolve("AA", 30, ""))
print(f"time: {time.time()-t}")
print(resolve.cache_info())
