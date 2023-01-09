import utils

m = utils.Opener.raw()[:-1]

for i in range(0, len(m)-4):
    if len(set(m[i:i+4])) == 4:
        print(i+4)
        break

for i in range(0, len(m)-14):
    if len(set(m[i:i+14])) == 14:
        print(i+14)
        break

