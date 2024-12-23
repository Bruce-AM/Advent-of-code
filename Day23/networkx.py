import networkx as nx

G = nx.Graph()
with open("adventofcode/day23/day23_input.txt", "r") as file:
    G.add_edges_from([tuple(line.split("-")) for line in file.read().split()])

cliques = sorted(nx.find_cliques(G), key = len)
print(sorted(cliques[-1])) #part2
