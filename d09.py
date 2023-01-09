import utils

m = utils.Opener.lines()

d = {"R": (1, 0), "L":(-1,0), "D":(0, -1), "U": (0,1)}
visited = set()

Hx, Hy = (0, 0)
Tx, Ty = (0, 0)
for line in m:
    c, v = line.split(" ")
    v = int(v)
    dx, dy = d[c]
    # print(c, v)
    for _ in range(v):
        Hx, Hy = Hx+dx, Hy+dy
        qx, qy = abs(Hx - Tx), abs(Hy - Ty)
        if qx <= 1 and qy <= 1:
            pass
        elif qx > 1:
            Tx += 1 if Hx > Tx else -1
            if qy == 1:
                Ty += 1 if Hy > Ty else -1
        elif qy > 1:
            Ty += 1 if Hy > Ty else -1
            if qx == 1:
                Tx += 1 if Hx > Tx else -1
        visited.add((Tx, Ty))
        # print()

        # print((Hx, Hy), (Tx, Ty), (qx, qy))


print(len(visited))

visited = set()
snake = [(0, 0)] * 10
for line in m:
    c, v = line.split(" ")
    v = int(v)
    dx, dy = d[c]
    for _ in range(v):
        snake[0] = snake[0][0]+dx, snake[0][1]+dy
        for i in range(1, len(snake)):
            Hx, Hy = snake[i-1]
            Tx, Ty = snake[i]
            qx, qy = abs(Hx - Tx), abs(Hy - Ty)
            if qx <= 1 and qy <= 1:
                pass
            elif qx > 1:
                Tx += 1 if Hx > Tx else -1
                if qy >= 1:
                    Ty += 1 if Hy > Ty else -1
            elif qy > 1:
                Ty += 1 if Hy > Ty else -1
                if qx >= 1:
                    Tx += 1 if Hx > Tx else -1
            snake[i] = (Tx, Ty)
            if i == 9:
                visited.add((Tx, Ty))

utils.print_grid(visited)

print(len(visited))
