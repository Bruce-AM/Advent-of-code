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
                if values[j] in set_connections[values[i]]: #part1
                    three_computers.add(tuple(sorted([k, values[i], values[j]])))
                if all(values[j] in set_connections[comp] for comp in cur_lst):
                    cur_lst.append(values[j])
            if len(cur_lst) > len(longest): #part2
                longest = cur_lst   
    print(sum(1 for tup in three_computers if any(char[0] == "t" for char in tup)))
    print(','.join(sorted(longest)))
both()
