import datetime
import time
from functools import cache

import utils

m = utils.Opener.lines("input/d16.txt")
# m = utils.Opener.lines("input/d16_small.txt")

cave = {}
zeroes = []

for line in m:
    a, c = line.split("to valve")
    a, b = a.split(" has flow rate=")
    valve = a.split(" ")[1]
    flow = int(b.split(";")[0])
    target = "".join(c.split(" ")[1:]).split(",")
    if flow == 0 and valve != "AA":
        zeroes.append([valve, [[t, 1] for t in target]])
    else:
        cave[valve] = [flow, [[t, 1] for t in target]]

done = set()

while zeroes:
    v, targets = zeroes.pop(0)
    done.add(v)
    for c in cave:
        res = cave[c][1]
        tem = None
        for i in range(len(res)):
            if res[i][0] == v:
                tem = res.pop(i)
                break
        if tem:
            cave[c][1] = res + [(t, x+tem[1]) for t, x in targets if t not in done and t!=c]

    for z in zeroes:
        res = z[1]
        tem = None
        for i in range(len(res)):
            if res[i][0] == v:
                tem = res.pop(i)
                break
        if tem:
            z[1] = res + [(t, x + tem[1]) for t, x in targets if t not in done]

for c in list(cave.keys()):
    paths = {}
    for x, n in cave[c][1]:
        if x not in paths:
            paths[x] = n
        else:
            paths[x] = min(paths[x], n)
    cave[c][1] = paths

lookup = {k: i for i, k in enumerate(cave)} # use set of ints (map AA->1 etc.)
cave = {lookup[k]: [v[0], {lookup[q]:d for q, d in v[1].items()}] for k, v in cave.items()}

@cache
def resolve(position, timeleft, person, opened):
    if timeleft == 1 and person == 1:
        return 0

    new_person = timeleft == 1 and person == 0

    if new_person:
        return resolve(lookup["AA"], 26, 1, opened)

    best = float("-inf")

    if cave[position][0] > 0 and position not in opened:
        best = max(best, (timeleft - 1) * cave[position][0] +
                   resolve(position, timeleft - 1, person,
                           tuple(sorted(opened + (position,)))))

    for c, t in cave[position][1].items():
        if timeleft - t >= 1:
            best = max(best, resolve(c, timeleft - t, person, opened))

    return best

t = time.time()
print(resolve(lookup["AA"], 26, 0, ()))
print(f"time: {time.time()-t}")
print(resolve.cache_info())
