from collections import defaultdict

m = open('input/d07.txt').read()[:-1].split('\n')
fs = defaultdict(list)
current = '/'

for (x, y, *args) in (s.split(' ') for s in m[1:]):
    if x == "$":
        if y == "cd":
            if args[0] == "..":
                current = '/'.join(current.split('/')[:-2]) + '/'
            else:
                current += args[0] + '/'
    elif x == "dir":
        fs[current] += [(-1, current + y + '/')]
    else:
        fs[current] += [(int(x), y)]

size = lambda d: sum(s if s >= 0 else size(n) for s, n in fs[d])
min_solution = 30_000_000 - (70_000_000 - size('/'))

print("star1", sum(s for s in map(size, fs) if s <= 100_000))
print("star2", min(s for s in map(size, fs) if s >= min_solution))

