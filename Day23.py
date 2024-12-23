from collections import defaultdict
import timeit

list_connections = defaultdict(list)
set_connections = defaultdict(set)
with open("day23_input.txt", "r") as file:
    for line in file.read().split():
        pc1, pc2 = tuple(line.split("-"))
        list_connections[pc1].append(pc2)
        list_connections[pc2].append(pc1)
        set_connections[pc1].add(pc2)
        set_connections[pc2].add(pc1)

def both():
    three_computers = set()
    longest = []
    for k, values in list_connections.items():
        for i in range(12):
            cur_lst = [k, values[i]]
            for j in range(i+1, 13):
                if values[j] in set_connections[values[i]]:
                    three_computers.add(tuple(sorted([k, values[i], values[j]])))
                for comp in cur_lst:
                    if values[j] not in set_connections[comp]:
                        break
                else:
                    cur_lst.append(values[j])
            if len(cur_lst) > len(longest):
                longest = cur_lst   
    total = 0
    for tup in three_computers:
        for char in tup:
            if char[0] == "t":
                total += 1
                break
    print(total)
    longest.sort()
    print(','.join(longest))
both()
