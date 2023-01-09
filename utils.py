import os.path
import inspect
from itertools import chain, combinations


# import stackprinter
# stackprinter.set_excepthook(style='lightbg')

### STRING ###
def replaceAll(string, repl_tuples):
    for t1, t2 in repl_tuples:
        string = string.replace(t1, t2)
    return string


nums = "0123456789"
hexanums = "0123456789abcdef"


def powerset(iterable):
    """
    https://stackoverflow.com/questions/1482308/how-to-get-all-subsets-of-a-set-powerset
    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    """
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

def manhattan(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])



def print_grid(grid, yes="#", no=" ", swap=True):
    xmin, xmax = min(x[0] for x in grid), max(x[0] for x in grid)
    ymin, ymax = min(x[1] for x in grid), max(x[1] for x in grid)

    if type(grid) == set:
        for i in range(ymin, ymax + 1):
            print("".join((no, yes)[(j, i) in grid] for j in range(xmin, xmax + 1)))
    if type(grid) == dict:
        if swap:
            for i in range(ymin, ymax + 1):
                print("".join(grid[j, i] if (j, i) in grid else no for j in range(xmin, xmax + 1)))
        else:
            for i in range(xmin, xmax + 1):
                print("".join(grid[i, j] if (i, j) in grid else no for j in range(ymin, ymax + 1)))


def save_image(grid, image: str, colors: dict):
    import numpy as np
    from PIL import Image

    xmin, xmax = min(x[0] for x in grid), max(x[0] for x in grid)
    ymin, ymax = min(x[1] for x in grid), max(x[1] for x in grid)

    arr = []
    for i in range(ymin, ymax + 1):
        for j in range(xmin, xmax + 1):
            if (j, i) in grid:
                arr.append(colors[grid[j, i]])
            else:
                arr.append(0)

    na = np.array(arr,  dtype=np.uint8)
    im = Image.fromarray(na.reshape(ymax-ymin+1, xmax-xmin+1))
    im.save(image)


### FILES ###
class Opener:
    @staticmethod
    def raw(location=None, s=1):
        if not location:
            location, name = os.path.split(inspect.stack()[s].filename)
            location = f"{location}/input/{os.path.splitext(name)[0]}.txt"
        with open(location, "rt") as f:
            return f.read()

    @staticmethod
    def lines(location=None, s=2):
        return Opener.raw(location, s=s).split("\n")[:-1]

    @staticmethod
    def numbers(location=None):
        return [int(x) for x in Opener.lines(location, s=3)]

    @staticmethod
    def grid(dtype=int, location=None):
        return [list(map(dtype, x)) for x in Opener.lines(location, s=3)]
