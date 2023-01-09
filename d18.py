import utils

m = utils.Opener.lines()

cubes = {tuple(map(int, line.split(","))) for line in m}


def neighbours(cube):
    return {(cube[0] + dx, cube[1] + dy, cube[2] + dz)
            for dx, dy, dz in (
                (1, 0, 0), (-1, 0, 0),
                (0, 1, 0), (0, -1, 0),
                (0, 0, 1), (0, 0, -1)
            )}


sides = {c: 6 for c in cubes}
for c in cubes:
    sides[c] -= sum(1 for n in neighbours(c) if n in cubes)
print(sum(sides.values()))

min_x = min(c[0] for c in cubes) - 1
max_x = max(c[0] for c in cubes) + 1
min_y = min(c[1] for c in cubes) - 1
max_y = max(c[1] for c in cubes) + 1
min_z = min(c[2] for c in cubes) - 1
max_z = max(c[2] for c in cubes) + 1

q = [(min_x, min_y, min_z)]
visited = {(min_x, min_y, min_z)} #exterior

while q:
    c = q.pop(0)
    for n in neighbours(c):
        if min_x <= n[0] <= max_x and min_y <= n[1] <= max_y and min_z <= n[2] <= max_z:
            if n not in cubes and n not in visited:
                q.append(n)
                visited.add(n)

for x in range(min_x, max_x):
    for y in range(min_y, max_y):
        for z in range(min_z, max_z):
            c = (x, y, z)
            if c not in visited and c not in cubes:
                for n in neighbours(c):
                    if n in cubes:
                        sides[n] -= 1

print(sum(sides.values()))
