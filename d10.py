import utils


m = utils.Opener.lines()


X = [1]
for (cmd, *args) in (s.split(" ") for s in m):
    if cmd == "addx":
        X += [X[-1], X[-1] + int(args[0])]
    elif cmd == "noop":
        X += [X[-1]]
    else:
        raise Exception(f"unknown: {cmd, args}")


star1 = sum(i * X[i-1] for i in range(20, 221, 40))
print(star1)

for i in range(len(X)):
    if i % 40 == 0:
        print()
    pos = X[i]
    if (i % 40) in (pos-1, pos, pos+1):
        print("#", end="")
    else:
        print(" ", end="")
