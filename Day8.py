from collections import defaultdict
from itertools import combinations

with open(r"ay8_input.txt","r") as file:
    ascii_map = [[c for char in line.split() for c in char] for line in file]

rows = len(ascii_map)
cols = len(ascii_map[0])
frequencies = defaultdict(list)
for r in range(rows):
    for c in range(cols):
        frequencies[ascii_map[r][c]].append((r, c))
frequencies.pop('.')

def unique_locations_part1():
    antidot = set()
    for freq in frequencies.values():
        for comb in combinations(freq, 2):
            a, b = comb
            y, x = b[0]-a[0], b[1]-a[1]    #distance
            a_y, a_x = a[0] - y, a[1] - x  #freq a-distance
            b_y, b_x = b[0] + y, b[1] + x  #freq b+distance
            if (-1 < a_y < rows) and (-1 < a_x < cols):
                antidot.add((a_y, a_x))
            if (-1 < b_y < rows) and (-1 < b_x < cols):
                antidot.add((b_y, b_x))
    print(len(antidot))

def unique_locations_part2():
    antidot = set()
    for freq in frequencies.values():
        for comb in combinations(freq, 2):
            a, b = comb
            antidot.add(a)
            antidot.add(b)
            y, x = b[0]-a[0], b[1]-a[1]    #distance        
            a_y, a_x = a[0] - y, a[1] - x  #freq a - distance
            b_y, b_x = b[0] + y, b[1] + x  #freq b + distance
            while (-1 < a_y < rows) and (-1 < a_x < cols):
                antidot.add((a_y, a_x))
                a_y, a_x = a_y - y, a_x - x
            while (-1 < b_y < rows) and (-1 < b_x < cols):
                antidot.add((b_y, b_x))
                b_y, b_x = b_y + y, b_x + x
    print(len(antidot))

unique_locations_part1()
unique_locations_part2()
