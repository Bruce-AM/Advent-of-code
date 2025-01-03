order:dict[set] = defaultdict(set)
with open(r"day5_order_dict.txt", "r") as file:
    for line in file:
        v, k = map(int, line.split('|'))
        order[k].add(v)

with open(r"day5_update_list.txt", "r") as file:
    updates = [list(map(int, line.split(','))) for line in file]

part1 = part2 = 0
for i, update in enumerate(updates):
    length = len(update)
    part = True
    for incorrect in range(length-1):
        for n in range(incorrect+1, length):
            if update[n] in order[update[incorrect]]:
                part = False
                updates[i][incorrect], updates[i][n] = updates[i][n], updates[i][incorrect]
    if part:
        part1 += update[length//2]
    else:
        part2 += update[length//2]

print(part1, part2)
