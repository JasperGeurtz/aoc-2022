from functools import reduce

print((exec("")
          (fs := reduce(
           lambda c, i: (
               c[0] if i[0] == '$' else (
                       c[0] | dict(
                   [(c[1], c[0].get(c[1], []) +
                     ([(int(i[0]), i[1])] if i[0] != 'dir' else [(-1, c[1] + i[1] + '/')]))]
               )),
               c[1] if (i[0], i[1]) != ('$', 'cd') else (
                   '/'.join(c[1].split('/')[:-2]) + '/' if i[2] == '..' else c[1] + i[2] + '/')
           ),
           (s.split(' ') for s in open('input/d07s.txt').read()[:-1].split('\n')[1:]),
           ({}, '/'))[0]),
        (size := lambda d: sum(s if s >= 0 else size(n) for s, n in fs[d])),
       (min_size := 30_000_000 - (70_000_000 - size('/'))),
       sum(s for s in map(size, fs) if s <= 100_000),
       min(s for s in map(size, fs) if s >= min_size)
       )[3:])
