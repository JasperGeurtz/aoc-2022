from tqdm import tqdm

import utils

m = utils.Opener.numbers("input/d20.txt")
# m = utils.Opener.numbers("input/d20_small.txt")

numbers = [(e, i) for i, e in enumerate(m)]
size = len(numbers)

for i in range(size):
    nxt = [q for q, (e, j) in enumerate(numbers) if j == i][0]
    n, j = numbers.pop(nxt)
    offset = (nxt + n) % (size - 1)
    numbers = numbers[:offset] + [(n, j)] + numbers[offset:]


zero = [q for q, (e, j) in enumerate(numbers) if e == 0][0]
print(sum(numbers[(zero + i) % size][0] for i in [1000, 2000, 3000]))


numbers = [(811589153 * e, i) for i, e in enumerate(m)]

for _ in tqdm(range(10)):
    for i in range(size):
        nxt = [q for q, (e, j) in enumerate(numbers) if j == i][0]
        n, j = numbers.pop(nxt)
        offset = (nxt + n) % (size - 1)
        numbers = numbers[:offset] + [(n, j)] + numbers[offset:]

zero = [q for q, (e, j) in enumerate(numbers) if e == 0][0]

print(sum(numbers[(zero + i) % size][0] for i in [1000, 2000, 3000]))

