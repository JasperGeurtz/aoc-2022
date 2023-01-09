import utils


m = utils.Opener.lines()

total = 0
total2 = 0
for line in m:
    a, b = line.split(",")
    a = list(map(int, a.split("-")))
    b = list(map(int, b.split("-")))
    print(a, b)
    if (a[0] >= b[0] and a[1] <= b[1]) or (b[0] >= a[0] and b[1] <= a[1]):
        total += 1

    if not(a[0] > b[1] or b[0] > a[1]):
        total2 += 1
print(total)
print(total2)

