import re
from collections import deque

with open("input8.txt") as f:
    instr = f.readline().strip()
    next(f)
    lines = f.readlines()


m = {}
pattern = r"([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)"

for line in lines:
    match = re.search(pattern, line)
    m[match.group(1)] = match.group(2), match.group(3)

d = deque(instr)


loc = None
i = 0

while True:
    for direction in d:
        if i == 0:
            loc = "AAA"

        if loc == "ZZZ":
            break

        lr = m[loc]

        print(i, loc, lr, direction)

        if direction == "L":
            loc = lr[0]
        elif direction == "R":
            loc = lr[1]
        else:
            raise ValueError

        i += 1
