from itertools import islice


def batched(iterable, n):
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError("n must be at least one")
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch


def line_lookup(n, line) -> tuple[int, bool]:
    if line[1] <= n < (line[1] + line[2]):
        return n - (line[1] - line[0]), True
    return n, False


assert line_lookup(79, [52, 50, 48]) == (81, True)


def lookup(n, lines):
    for line in lines:
        n, found = line_lookup(n, line)
        if found is True:
            return n
    return n


assert lookup(79, [[50, 98, 2], [52, 50, 48]]) == 81


with open("input5.txt") as f:
    seeds = [int(x) for x in f.readline().split(":")[-1].split()]
    next(f)
    lines = f.readlines()


def maps_from_input(lines):
    maps: list[list[int]] = []

    for line in lines:
        if "map" in line:
            # new mapping
            m = []
        elif line == "\n":
            maps.append(m)
        else:
            m.append([int(x) for x in line.split()])

    maps.append(m)

    return maps


maps = maps_from_input(lines)
smallest = False

batches = batched(seeds, n=2)

b = []

for start, length in sorted(batches):
    stop = start + length
    if b and b[-1][1] >= start - 1:
        b[-1][1] = max(b[-1][1], stop)
    else:
        b.append((start, stop))


rngs = [range(start, stop) for start, stop in b]


for r in rngs:
    for seed in r:
        print(f"Seed: {seed}")
        for i, m in enumerate(maps):
            if i == 0:
                search = seed
            search = lookup(search, m)
        loc = search
        if smallest is False:
            smallest = loc
        else:
            if loc < smallest:
                smallest = loc

print(smallest)
