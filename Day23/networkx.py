import networkx as nx
from itertools import combinations

G = nx.Graph()
with open("adventofcode/day23/day23_input.txt", "r") as file:
    G.add_edges_from([tuple(line.split("-")) for line in file.read().split()])

cliques = sorted(nx.find_cliques(G), key = len)
print(sorted(cliques[-1])) #part2

triplets = {tuple(sorted(comb)) for lst in cliques if len(lst) > 2 for comb in combinations(lst, 3)}
print(sum(1 for tup in triplets if any(char[0] == "t" for char in tup))) #part1
