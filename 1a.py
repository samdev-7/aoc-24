left = []
right = []

with open("1in.txt", "r") as f:
    for line in f.readlines():
        (l, r) = line.strip().split("   ")
        left.append(int(l))
        right.append(int(r))

left.sort()
right.sort()

dist = 0

for i in range(len(left)):
    dist += abs(left[i] - right[i])

print(dist)
