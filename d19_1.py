import time
from functools import cache

import utils

m = utils.Opener.lines("input/d19.txt")
# m = utils.Opener.lines("input/d19_small.txt")

blueprints = []

lookup = ["ore", "clay", "obsidian", "geode"]

for line in m:
    blueprint = []
    for i, info in enumerate(line.split(": ")[1].split(".")[:-1]):
        # rt = info.strip().split(" ")[1]
        res = {lookup.index(x.split(" ")[1]): int(x.split(" ")[0]) for x in info.split("costs ")[1].split(" and ")}
        blueprint.append([res.get(i, 0 ) for i in range(4)])
    blueprints.append(blueprint)


# print("\n".join(map(str, blueprints)))

tot = 0
tt = time.time()

for i, blueprint in enumerate(blueprints):
    max_ore = max(k[0] for k in blueprint)
    max_clay = max(k[1] for k in blueprint)
    max_obsidian = max(k[2] for k in blueprint)
    maxes = [max_ore, max_clay, max_obsidian]
    # exit()

    @cache
    def collect(timeleft, f_0, f_1, f_2, f_3, r_0, r_1, r_2, r_3):
        if timeleft == 0:
            return r_3  # geode

        max_geode = collect(timeleft - 1, f_0, f_1, f_2, f_3, r_0+f_0, r_1+f_1, r_2+f_2, r_3+f_3)

        # (1) buying doesn't matter if timeleft = 1
        if timeleft > 1:

            # (2) always buy geode factory if possible
            c_0, c_1, c_2, c_3 = blueprint[3]
            if r_0 >= c_0 and r_1 >= c_1 and r_2 >= c_2 and r_3 >= c_3:
                d_0 = r_0 - c_0
                d_1 = r_1 - c_1
                d_2 = r_2 - c_2
                d_3 = r_3 - c_3
                max_geode = max(max_geode, collect(
                    timeleft - 1, f_0, f_1, f_2,  f_3 + 1, d_0 + f_0, d_1 + f_1, d_2 + f_2, d_3 + f_3
                ))
            else:
                for fact_type, costs in enumerate(blueprint[:3]):
                    # (3) only need a max(ore_requirements) of ore to produce a bot per turn
                    if (f_0, f_1, f_2)[fact_type] >= maxes[fact_type]:
                        continue
                    c_0, c_1, c_2, c_3 = costs
                    if r_0 >= c_0 and r_1 >= c_1 and r_2 >= c_2 and r_3 >= c_3:
                        d_0 = r_0 - c_0
                        d_1 = r_1 - c_1
                        d_2 = r_2 - c_2
                        d_3 = r_3 - c_3

                        max_geode = max(max_geode, collect(
                            timeleft - 1,
                            f_0 + int(fact_type == 0),
                            f_1 + int(fact_type == 1),
                            f_2 + int(fact_type == 2),
                            f_3,
                            d_0 + f_0,
                            d_1 + f_1,
                            d_2 + f_2,
                            d_3 + f_3
                        ))

        return max_geode

    t = time.time()
    print(i, blueprint)
    collect.cache_clear()
    result = collect(24, 1, 0, 0, 0, 0, 0, 0, 0)
    print(f"{i=}: {result=}")
    print(collect.cache_info())
    print(time.time() - t, "s")

    tot += (i + 1) * result
    # break

print("FINISHED: ", tot)
print("total time: ", time.time()-tt)
