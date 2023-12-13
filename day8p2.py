import re
import sys
from collections import deque


Char = str


with open("input8.txt") as f:
    instr = f.readline().strip()
    next(f)
    lines = f.readlines()


m = {}
pattern = r"([0-9A-Z]{3}) = \(([0-9A-Z]{3}), ([0-9A-Z]{3})\)"

for line in lines:
    match = re.search(pattern, line)
    m[match.group(1)] = match.group(2), match.group(3)


d = deque(instr)


def startpoints(m: dict[str, tuple[str, str]]):
    s = []
    for k in m:
        if k.endswith("A"):
            s.append(k)
    return s


def step(m: dict, loc: str, dir: Char):
    if dir == "L":
        return m[loc][0]
    elif dir == "R":
        return m[loc][1]
    else:
        raise ValueError


def step_all(locs, mapping, dir):
    a = []
    for loc in locs:
        new = step(mapping, loc, dir)
        a.append(new)
    return a


sd = d

i = 0


start = "11A"


def cycle(deq, mapping, start):
    i = 0
    steps = []

    while True:
        for dir in deq:
            if i == 0:
                loc = start
                steps.append(loc)

            next_loc = step(mapping, loc, dir)

            # print(f"{i} Location: {loc}, Next: {next_loc}")

            if next_loc in steps:
                return steps
            else:
                loc = next_loc
                steps.append(loc)
                i += 1


def cycle_all(deq, mapping, starts):
    i = 0

    while True:
        for dir in deq:
            if i == 0:
                locs = starts

            new_locs = step_all(locs, mapping, dir)

            print(f"{i} Location: {locs}, Next: {new_locs}")

            if all(x.endswith('Z') for x in new_locs):
                print(i+ 1)
                sys.exit()

            locs = new_locs

            i += 1


# q = []

# for s in startpoints(m):
#     nd = sd
#     points = cycle(nd, m, s)
#     q.append(points)


# for points in q:
#     has_z = [x for x in points if x.endswith("Z")]
#     print(points)
#     print(len(points))
#     print(len(has_z))
