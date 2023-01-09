import utils

m = utils.Opener.lines("d25.txt")
# m = utils.Opener.lines("d25_small.txt")



def dec_to_snafu(line):
    q = 0
    for i, c in enumerate(reversed(line)):
        j = {"0": 0, "1": 1, "2": 2, "=": -2, "-": -1}
        q += j[c] * 5 ** i
    return q


def snafu_to_dec(number):
    q = ""
    while number > 0:
        r = number % 5
        number = number // 5
        q += {0: "0", 1: "1", 2: "2", 3: "=", 4: "-"}[r]
        if r > 2:
            number += 1
    return "".join(reversed(q))


total = 0

for line in m:
    total += dec_to_snafu(line)
print(total)

print(snafu_to_dec(total))

