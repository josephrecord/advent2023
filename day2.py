import re

from collections import defaultdict

max_red = 12
max_green = 13
max_blue = 14

colors = ["red", "green", "blue"]
 

def n_color(color: str, s: str) -> int:
    if color not in colors:
        raise ValueError
    if m := re.search(rf"(\d+) {color}", s):
        return int(m.group(1))
    return 0


def valid_game(line) -> bool:
    for set in line.split(":")[-1].split(";"):
        red = n_color("red", set)
        green = n_color("green", set)
        blue = n_color("blue", set)
        if red > max_red or green > max_green or blue > max_blue:
            return False
    return True


def pow(line) -> int:
    c = defaultdict(list)
    for set in line.split(":")[-1].split(";"):
        for color in colors:
            c[color].append(n_color(color, set))
    return max(c["red"]) * max(c["green"]) * max(c["blue"])


with open("input2.txt") as f:
    lines = f.readlines()

ans1 = 0
ans2 = 0

for line in lines:
    ans2 += pow(line)

for i, line in enumerate(lines, start=1):
    if valid_game(line):
        ans1 += i


print(ans1)
print(ans2)
