safe = 0

with open("2in.txt", "r") as f:
    for line in f.readlines():
        cur_safe = True
        inc = True
        nline = [int(x) for x in line.strip().split(" ")]
        for i in range(len(nline) - 1):
            if nline[i] > nline[i + 1]:
                inc = False
                break
        for i in range(len(nline) - 1):
            if not nline[i + 1] - nline[i] in ([1, 2, 3] if inc else [-1, -2, -3]):
                cur_safe = False
                break
        if cur_safe:
            safe += 1

print(safe)
