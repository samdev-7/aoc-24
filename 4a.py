from re import S


data = []

with open("4in.txt", "r") as f:
    data = [[c for c in line.strip()] for line in f.readlines()]

count = 0

# horizontal
for line in data:
    for i in range(len(line) - 3):
        if line[i : i + 4] == ["X", "M", "A", "S"] or line[i : i + 4] == [
            "S",
            "A",
            "M",
            "X",
        ]:
            print("hori", line)
            count += 1

rot_data = list(zip(*data))

print(rot_data)
# vertical
for line in rot_data:
    for i in range(len(line) - 3):
        if line[i : i + 4] == ("X", "M", "A", "S") or line[i : i + 4] == (
            "S",
            "A",
            "M",
            "X",
        ):
            print("vert", line)
            count += 1

# diagonal br
for i in range(len(data) - 3):
    for j in range(len(data[i]) - 3):
        if [data[i][j], data[i + 1][j + 1], data[i + 2][j + 2], data[i + 3][j + 3]] == [
            "X",
            "M",
            "A",
            "S",
        ] or [
            data[i][j],
            data[i + 1][j + 1],
            data[i + 2][j + 2],
            data[i + 3][j + 3],
        ] == [
            "S",
            "A",
            "M",
            "X",
        ]:
            print("diag br", i, j)
            count += 1

# diagonal bl
for i in range(len(data) - 3):
    for j in range(3, len(data[i])):
        if [data[i][j], data[i + 1][j - 1], data[i + 2][j - 2], data[i + 3][j - 3]] == [
            "X",
            "M",
            "A",
            "S",
        ] or [
            data[i][j],
            data[i + 1][j - 1],
            data[i + 2][j - 2],
            data[i + 3][j - 3],
        ] == [
            "S",
            "A",
            "M",
            "X",
        ]:
            print("diag bl", i, j)
            count += 1

print(count)
