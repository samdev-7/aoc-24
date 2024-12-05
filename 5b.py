from functools import cmp_to_key

from multiprocessing import Pool


def correct_order(update, rules):
    for rule in rules:
        if (
            rule[0] in update
            and rule[1] in update
            and update.index(rule[0]) >= update.index(rule[1])
        ):
            return None
    print("correct", update)
    return update


def incorrect_order(update, rules):
    for rule in rules:
        if (
            rule[0] in update
            and rule[1] in update
            and update.index(rule[0]) >= update.index(rule[1])
        ):
            print("incorrect", update)
            return update
    return None


def make_correct(update, rules):
    print("fixing", update)
    u = update.copy()

    def comp(a, b):
        for rule in rules:
            if rule[0] == a and rule[1] == b:
                return -1
            elif rule[0] == b and rule[1] == a:
                return 1
        return 0

    while not correct_order(u, rules):
        u.sort(key=cmp_to_key(comp))
    return u


if __name__ == "__main__":
    inp = []

    with open("5in.txt", "r") as f:
        inp = [line.strip() for line in f.readlines()]

    rules, updates = inp[: inp.index("")], inp[inp.index("") + 1 :]
    rules = [[int(n) for n in rule.split("|")] for rule in rules]
    updates = [[int(n) for n in update.split(",")] for update in updates]

    correct = []
    incorrect = []

    pool = Pool(1)
    res1 = [pool.apply_async(incorrect_order, (update, rules)) for update in updates]

    incorrect = [p.get(timeout=10) for p in res1]

    incorrect = [update for update in incorrect if update is not None]

    res2 = [pool.apply_async(make_correct, (update, rules)) for update in incorrect]

    correct = [p.get() for p in res2]

    print(correct)

    res = 0
    for update in correct:
        res += update[len(update) // 2]
    print(res)
