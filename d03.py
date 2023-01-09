import utils


m = utils.Opener.lines()

stars = {'1': 0, '2': 0}
d = {chr(i+ord('a')): i+1 for i in range(0, 26)} |\
    {chr(i+ord('A')): i+27 for i in range(0, 26)}

for line in m:
    half = len(line)//2
    unique = set(line[:half]) & set(line[half:])
    stars['1'] += d[unique.pop()]

for i in range(0, len(m), 3):
    unique = set(m[i]) & set(m[i+1]) & set(m[i+2])
    stars['2'] += d[unique.pop()]

print(stars)


print(sum(map(
    lambda c: ord(c) + (-ord('a') + 1, -ord('A') + 27)[c.isupper()],
    ((set(a) & set(b) & set(c)).pop()
        for a, b, c in zip(*[iter(open("input/d03.txt").read().split('\n'))]*3)
    )
)))

