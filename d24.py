from queue import PriorityQueue

import utils

m = utils.Opener.lines("input/d24.txt")
# m = utils.Opener.lines("input/d24_small.txt")


rows = len(m)
cols = len(m[0])
grid = {}

start = None
end = None
for i, line in enumerate(m):
    for j, c in enumerate(line):
        if i == 0 and c == ".":
            start = (i, j)
        if i == rows - 1 and c == ".":
            end = (i, j)
        if c not in "#.":
            grid[i, j] = c

print(rows, cols)
print(start, end)
print("#########################")


def simulate(state):
    new_state = {}
    dirs = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
    for (bi, bj), chars in state.items():
        for c in chars:
            qi, qj = bi + dirs[c][0], bj + dirs[c][1]
            if (qi, qj) == start or (qi, qj) == end:
                raise Exception("NOT POSSIBLE")
            if qi == 0:
                qi = rows - 2
            if qi == rows - 1:
                qi = 1
            if qj == 0:
                qj = cols - 2
            if qj == cols - 1:
                qj = 1
            if (qi, qj) not in new_state:
                new_state[qi, qj] = c
            else:
                new_state[qi, qj] += c
    return new_state



def dijkstra(start, end, state):
    state_lookup = {
        0: state
    }
    queue = PriorityQueue()
    queue.put((0, start))
    visited = {(0, *start)}
    while not queue.empty():
        d, (i, j) = queue.get()

        for x, y in ((i, j), (i-1, j), (i+1, j), (i, j-1), (i, j+1)):
            if (x, y) == end:
                return d+1, state_lookup[d+1]

            if (x, y) == start or (1 <= x < rows - 1 and 1 <= y < cols - 1):
                if d+1 not in state_lookup:
                    state_lookup[d+1] = simulate(state_lookup[d])
                if (d+1, x, y) not in visited and (x, y) not in state_lookup[d+1]:
                    queue.put((d+1, (x, y)))
                    visited.add((d+1, x, y))


a, state = dijkstra(start, end, grid)
print("star1", a)

b, state = dijkstra(end, start, state)
c, _ = dijkstra(start, end, state)
print("star2", a+b+c)
