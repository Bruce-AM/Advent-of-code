from collections import defaultdict
import timeit

list_connections = defaultdict(list)
set_connections = defaultdict(set)
with open("day23_input.txt", "r") as file:
    for line in file.read().split():
        pc1, pc2 = tuple(line.split("-"))
        list_connections[pc1].append(pc2) # 'jr': ['ev', 'qr', 'ox', 'ha', 'cf', 'bp', 'nm', 'dh', 'ly', 'rw', 'db', 'yk', 'eo']
        list_connections[pc2].append(pc1) # pc: [what connections it has]
        set_connections[pc1].add(pc2)
        set_connections[pc2].add(pc1)

three_computers = set()
longest = []
for k, values in list_connections.items(): # k - 'jr', values - list
    for i in range(12): #len(values)-1
        cur_set = {k, values[i]} # set('jr', and first value in the list 'ev')
        for j in range(i+1, 13): # starting from next after 'ev' which is 'qr'
            if values[j] in set_connections[values[i]]: #part1 #if next item 'qr' in in list 'ev':[]
                three_computers.add(tuple(sorted([k, values[i], values[j]])))
            if cur_set.issubset(set_connections[values[j]]): # if set('jr', 'ev') all items are in set of 'qr'
                cur_set.add(values[j]) # we add 'qr' to the set('jr', 'ev', 'qr')
        if len(cur_set) > len(longest): #part2 #just remember longest set
            longest = cur_set
print(sum(1 for tup in three_computers if any(char[0] == "t" for char in tup)))
print(','.join(sorted(longest)))
