with open("adventofcode/day25/day25_input.txt", "r") as file:
    lockskeys = [[line for line in lk.split("\n")] for lk in file.read().split("\n\n") ]

def createlocksandkeys():
    locks = set()
    keys = set()
    for lk in lockskeys:      
        cur_pattern = tuple(col.count("#") for col in zip(*lk))
        if lk[0][0] == "#":
            locks.add(cur_pattern)
        else:
            keys.add(cur_pattern)
    return locks, keys

def part1(locks, keys):
    fit = 0
    for lock in locks:
        for key in keys:
            for col_l, col_k in zip(lock, key):
                if col_l+col_k > 7:
                    break
            else:
                fit += 1
    print(fit)

def main():
    locks, keys = createlocksandkeys()
    part1(locks, keys)
main()
