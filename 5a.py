inp = []

with open("5in.txt", "r") as f:
    inp = [line.strip() for line in f.readlines()]

rules, updates = inp[: inp.index("")], inp[inp.index("") + 1 :]
rules = [[int(n) for n in rule.split("|")] for rule in rules]
updates = [[int(n) for n in update.split(",")] for update in updates]

print(rules, updates)

correct = []

for update in updates:
    cor = True
    for rule in rules:
        if (
            rule[0] in update
            and rule[1] in update
            and update.index(rule[0]) >= update.index(rule[1])
        ):
            cor = False
            break
    if cor:
        print(update)
        correct.append(update)

res = 0
for update in correct:
    res += update[len(update) // 2]
print(res)
