import time

import utils

m = utils.Opener.lines("input/d15.txt")

def func():
    r_min = 0
    r_max =  4_000_000  # 20

    slices = [list() for _ in range(r_max+1)]
    for line in m:
        si, sj, bi, bj = line.split("=")[1:]
        si, sj, bi, bj = map(int, (si.split(",")[0], sj.split(":")[0], bi.split(",")[0], bj))

        md = utils.manhattan((si, sj), (bi, bj))

        for i in range(max(r_min, si - md), min(si + md + 1, r_max + 1)):
            t = md - abs(i - si)
            slices[i].append((max(sj - t, r_min), min(sj + t + 1, r_max+1)))

    for i in range(len(slices)):
        slices[i].sort()
        merged_list = [(slices[i][0])]

        for start, end in slices[i][1:]:
            last_start, last_end = merged_list[-1]
            if start <= last_end:
                merged_list[-1] = (last_start, max(end, last_end))
            else:
                merged_list.append((start, end))

        if len(merged_list) > 1:
            return 4_000_000 * i + merged_list[0][1]


start = time.time()
res = func()
end = time.time()
print(f"{res} in {end - start:.2f}s")