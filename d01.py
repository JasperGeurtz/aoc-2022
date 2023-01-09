import utils

m = utils.Opener.raw()[:-1]

stars = {'1': 0, '2': {}}
for elf in m.split("\n\n"):
    calories = sum(map(int, elf.split('\n')))
    stars['1'] = max(stars['1'], calories)
    stars['2'][calories] = 1
    if len(stars['2']) > 3:
        stars['2'].pop(min(stars['2']))

stars['2'] = sum(stars['2'].keys())

print(stars)  # {'1': 71124, '2': 204639}
