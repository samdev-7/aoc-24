data = []

with open("4in.txt", "r") as f:
    data = [[c for c in line.strip()] for line in f.readlines()]

count = 0

pattern = [["M", ".", "S"], [".", "A", "."], ["M", ".", "S"]]
patterns = [pattern]
for i in range(3):
    patterns.append([list(x) for x in list(zip(*patterns[-1][::-1]))])

print(patterns)


def match(data, pattern):
    for i in range(len(pattern)):
        for j in range(len(pattern[i])):
            if pattern[i][j] != "." and pattern[i][j] != data[i][j]:
                return False
    return True


for pattern in patterns:
    for i in range(len(data) - 2):
        for j in range(len(data[i]) - 2):
            if match([data[i + k][j : j + 3] for k in range(3)], pattern):
                count += 1

print(count)
