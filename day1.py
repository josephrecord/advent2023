
import re

def line_amt(line: str) -> int:
    amt = ""
    decimals: list[str] = []
    for char in line:
        if char.isdecimal():
            decimals.append(char)
    return int(decimals[0] + decimals[-1])


def line_amt2(line: str) -> int:
    digits: dict[str: int] = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
        }
    
    found: dict[int, list[int]] = {}
    
    for nstr, nint in digits.items():
        matches = re.finditer(nstr, line)
        found[nint] = [x.start() for x in matches]
    
    print(found)

    first_idx = len(line) - 1
    last_idx = -1

    first_val = None
    last_val = None

    for nint, indices in found.items():
        if indices:
            print(indices)
            print(f"min: {min(indices)}")
            print(f"max: {max(indices)}")
            if min(indices) < first_idx:
                first_idx = min(indices)
                first_val = nint
            if max(indices) > last_idx:
                last_idx = max(indices)
                last_val = nint
    
    return (first_val, first_idx), (last_val, last_idx)








assert line_amt("1abc2") == 12
assert line_amt("pqr3stu8vwx") == 38
assert line_amt("a1b2c3d4e5f") == 15
assert line_amt("treb7uchet") == 77


with open("input1.txt") as f:
    lines = f.readlines()

total = 0
for line in lines:
    total += line_amt(line)

print(total)