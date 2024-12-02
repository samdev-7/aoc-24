safe = 0


def line_safe(nline):
    inc = True
    for i in range(len(nline) - 1):
        if nline[i] > nline[i + 1]:
            inc = False
            break
    for i in range(len(nline) - 1):
        if not nline[i + 1] - nline[i] in ([1, 2, 3] if inc else [-1, -2, -3]):
            return False
    return True


with open("2in.txt", "r") as f:
    for line in f.readlines():
        if line_safe([int(x) for x in line.strip().split(" ")]):
            safe += 1
        else:
            for i in range(len(line.strip().split(" "))):
                nline = [int(x) for x in line.strip().split(" ")]
                nline.pop(i)
                if line_safe(nline):
                    safe += 1
                    break


print(safe)
