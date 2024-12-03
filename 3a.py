import re

res = 0

with open("3in.txt", "r") as f:
    for line in f.readlines():
        match = re.findall("mul\(([0-9]+),([0-9]+)\)", line)
        for m in match:
            res += int(m[0]) * int(m[1])

print(res)
