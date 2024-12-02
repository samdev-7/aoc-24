left = []
right = []

with open("1in.txt", "r") as f:
    for line in f.readlines():
        (l, r) = line.strip().split("   ")
        left.append(int(l))
        right.append(int(r))

score = 0

for l in left:
    score += l * right.count(l)

print(score)
