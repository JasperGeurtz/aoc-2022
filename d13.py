from functools import cmp_to_key

import utils

m = utils.Opener.lines()


def comp(a, b):
    res = 0
    if type(a) == list and type(b) == int:
        res = comp(a, [b])
    if type(a) == int and type(b) == list:
        res = comp([a], b)
    if type(a) == int and type(b) == int:
        res = a - b
    if type(a) == list and type(b) == list:
        for i in range(len(a)):
            if i >= len(b):
                res = 1
            else:
                res = comp(a[i], b[i])
            if res != 0:
                break
        if res == 0 and len(b) > len(a):
            res = -1
    return res


lines = []
star1 = 0
for i in range(0, len(m), 3):
    lines += [eval(m[i]), eval(m[i+1])]
    c = comp(lines[-2], lines[-1])
    if c < 0:
        star1 += (i // 3) + 1

print(star1)

lines = sorted(lines + [[[2]], [[6]]], key=cmp_to_key(lambda x, y: comp(x, y)))
print((lines.index([[2]])+1)*(lines.index([[6]])+1))
