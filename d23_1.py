from collections import defaultdict

import utils

m = utils.Opener.raw("input/d23.txt")
# m = utils.Opener.raw("input/d23_small.txt")
# m = utils.Opener.raw("input/d23_very_small.txt"


def to_grid(string, x=0, y=0):
    grid = set()

    string = string.strip()
    for row, line in enumerate(string.split("\n")):
        for col, c in enumerate(line):
            if c == "#":
                grid.add((row+x, col+y))
    return grid

def check_north(row, col, state):
    for i in (-1, 0, 1):
        if (row - 1, col + i) in state:
            return None
    return row - 1, col


def check_south(row, col, state):
    for i in (-1, 0, 1):
        if (row + 1, col + i) in state:
            return None
    return row + 1, col


def check_west(row, col, state):
    for i in (-1, 0, 1):
        if (row + i, col - 1) in state:
            return None
    return row, col - 1


def check_east(row, col, state):
    for i in (-1, 0, 1):
        if (row + i, col + 1) in state:
            return None
    return row, col + 1

def all_empty(row, col, state):
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if (i, j) == (0, 0):
                continue
            if (row + i, col + j) in state:
                return False
    return True

def simulate(state, directions):
    new = defaultdict(list) # pos -> potential
    old = set()
    for elf in state:
        if all_empty(*elf, state):
            old.add(elf)
            continue
        for d in directions:
            target = d(*elf, state)
            if target:
                new[target].append(elf)
                break
        else:
            old.add(elf)

    for target, elves in new.items():
        if len(elves) > 1:
            print("MULTIPLE:", target, ":",elves)
            old.update(elves)
        else:
            old.add(target)
    return old

state = to_grid(m)
directions = [check_north, check_south, check_west, check_east]

print(len(state))
utils.print_grid(state, yes="#", no=".")

for i in range(10):
    print("episode:", i)
    state = simulate(state, directions)
    directions.append(directions.pop(0))
    print(state)
    utils.print_grid(state, yes="#", no=".")

row_min = min(r for r, c in state)
row_max = max(r for r, c in state)
col_min = min(c for r, c in state)
col_max = max(c for r, c in state)

# utils.print_grid(state, yes="#", no=".")
print(len(state))
print((row_max-row_min+1)*(col_max-col_min+1) - len(state))


