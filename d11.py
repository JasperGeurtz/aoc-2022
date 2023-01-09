import dataclasses
from typing import List, Callable

import utils

m = utils.Opener.lines()


@dataclasses.dataclass
class Monkey:
    items: List[int]
    operation: Callable
    test: int
    target: List[int]
    inspections: int = 0


monkeys = []

for i in range(0, len(m), 7):
    monkeys.append(Monkey(
        items=list(map(int, m[i + 1].split(": ")[1].split(", "))),
        operation=eval("lambda old: " + m[i + 2].split("new = ")[1]),
        test=int(m[i + 3].split(": ")[1].split(" ")[-1]),
        target=[int(m[i + 5].split(" ")[-1]), int(m[i + 4].split(" ")[-1])]
    ))

for _ in range(20):
    for monkey in monkeys:
        for item in monkey.items:
            w = monkey.operation(item) // 3
            target = monkey.target[w % monkey.test == 0]
            monkeys[target].items.append(w)
            monkey.inspections += 1
        monkey.items = []

scores = sorted([monkey.inspections for monkey in monkeys])
print(scores[-1] * scores[-2])


mod = 1
for monkey in monkeys:
    mod *= monkey.test

for _ in range(10000):
    for monkey in monkeys:
        for item in monkey.items:
            w = monkey.operation(item) % mod
            target = monkey.target[w % monkey.test == 0]
            monkeys[target].items.append(w)
            monkey.inspections += 1
        monkey.items = []

scores = sorted([monkey.inspections for monkey in monkeys])
print(scores[-1] * scores[-2])
