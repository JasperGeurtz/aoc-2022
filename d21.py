import utils

m = utils.Opener.lines("input/d21.txt")
# m = utils.Opener.lines("input/d21_small.txt")


monkeys = {}
for line in m:
    x = line.split(" ")
    monkeys[x[0][:-1]] = int(x[1]) if len(x) == 2 else x[1:]


def yell(monkey):
    v = monkeys[monkey]
    if type(v) == int:
        return v
    return eval(f'{yell(v[0])} {v[1]} {yell(v[2])}')


print(int(yell("root")))

monkeys["root"][1] = "=="
queue = [("root", "")]
directions = ""
while queue:
    m, directions = queue.pop(0)
    if m == "humn":
        break
    x = monkeys[m]
    if type(x) == list:
        queue += [(x[0], directions + "L"), (x[2], directions + "R")]

level, target = "root", None
for c in directions:
    x = monkeys[level]
    op, level = (yell(x[2]), x[0]) if c == "L" else (yell(x[0]), x[2])

    if x[1] == "==":
        target = op
    elif x[1] == "/":
        if c == "L":  # L: TARGET = X / OP => X = TARGET * OP
            target = target * op
        else:  # R: TARGET = OP / X => X = OP / TARGET
            target = op / target
    elif x[1] == "+":
        target = target - op  # L: TARGET = X + OP, # R: TARGET = OP + X
    elif x[1] == "*":
        target = target / op  # L: TARGET = X * OP, R: TARGET = OP * X
    elif x[1] == "-":
        if c == "L":  # L: TARGET = X - OP => X = TARGET - OP
            target = target + op
        else:  # R: TARGET = OP - X => X = OP - TARGET
            target = op - target

print(int(target))
