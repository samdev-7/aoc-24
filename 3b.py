import re

res = 0
active = True

with open("3in.txt", "r") as f:
    for line in f.readlines():
        match = re.findall(
            "mul\(([0-9]{1,3}),([0-9]{1,3})\)|(don't\(\))|(do\(\))", line
        )
        for m in match:
            if len(m[2]) > 0:
                active = False
            elif len(m[3]) > 0:
                active = True
            elif active:
                res += int(m[0]) * int(m[1])

print(res)
