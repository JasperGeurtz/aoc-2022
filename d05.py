from collections import defaultdict

import utils


m = utils.Opener.lines()

stacks1 = defaultdict(list)
stacks2 = defaultdict(list)

for line in m:
    if line.strip().startswith("["):
        for i in range(0, len(line), 4):
            if line[i+1] != ' ':
                stacks1[(i//4)+1].append(line[i+1])
                stacks2[(i//4)+1].append(line[i+1])

    if line.startswith("move"):
        amount, t = line.split(' from ')
        amount = int(amount.split(' ')[1])
        source, target = map(int, t.split(' to '))

        stacks1[target] = list(reversed(stacks1[source][0:amount])) + stacks1[target]
        stacks2[target] = list(stacks2[source][0:amount]) + stacks2[target]

        stacks1[source] = stacks1[source][amount:]
        stacks2[source] = stacks2[source][amount:]

print(''.join(stacks1[k][0] for k in sorted(stacks1.keys())))
print(''.join(stacks2[k][0] for k in sorted(stacks1.keys())))

# SVFDLGLWV
# DCVTCVPCL
