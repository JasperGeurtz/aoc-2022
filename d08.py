from math import ceil

import utils

m = utils.Opener.grid()

assert len(m) == len(m[0])
n = len(m)

mh = {}

visible = set()

def look(f):
    for c in range(n):
        q = -1
        for i in range(n):
            x, y = f(i, c)
            t = m [x][y]
            if q < t:
                visible.add((x, y))
                q = t

#top
look(lambda i, c: (i, c))
look(lambda i, c: (n-1-i, c))

look(lambda i, c: (c, i))
look(lambda i, c: (c, n-1-i))

print(len(visible))

best = 0

def score(x, y):
    v = m[x][y]
    print("#", x, y, v)
    a = 0
    for i in range(x+1, n):
        if m[i][y] < v:
            a += 1
        else:
            a += 1
            break
    b = 0
    for i in range(y+1, n):
        if m[x][i] < v:
            b += 1
        else:
            b+= 1
            break
    c = 0
    for i in range(x-1, -1, -1):
        if m[i][y] < v:
            c += 1
        else:
            c+=1
            break
    d = 0
    for i in range(y-1, -1, -1):
        if m[x][i] < v:
            d += 1
        else:
            d += 1
            break
    print(a, b, c, d)
    return a*b*c*d

best = -1
bb = 0
for t in visible:
    x, y = t[0], t[1]
    s = score(x, y)
    if s > best:
        bb = x,y
    best = max(s, best)

print("best: ", (bb, best))
score(*bb)
#
# print(best)
#
# print(score(3,2))
# print(score(0,0))

