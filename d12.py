from queue import PriorityQueue
import utils

m = utils.Opener.grid(dtype=str)
w, h = len(m), len(m[0])
print(len(m), len(m[0]))


def valid(x, y, i, j):
    if m[i][j] == "S" or m[x][y] == "S":
        return True
    if m[x][y] == "E":
        return m[i][j] in "yz"
    # c - b == 1, c - a == 2
    return ord(m[x][y]) - ord(m[i][j]) <= 1

def dijkstra(S):
    queue = PriorityQueue()
    queue.put((0, S))
    visited = {S}
    while not queue.empty():
        l, (i, j) = queue.get()

        if m[i][j] == "E":
            return l
        for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
            if x < 0 or y < 0 or x >= w or y >= h:
                continue
            if (x, y) in visited:
                continue
            if valid(x, y, i, j):
                queue.put((l+1, (x, y)))
                visited.add((x, y))
    return float('inf')


for i in range(w):
    for j in range(h):
        if m[i][j] == "S":
            dmin = dijkstra((i, j))
            break
print(dmin)

for i in range(w):
    for j in range(h):
        if m[i][j] == "a":
            d = dijkstra((i, j))
            dmin = min(dmin, d)
print(dmin)
