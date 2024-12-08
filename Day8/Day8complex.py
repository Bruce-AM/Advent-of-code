from collections import defaultdict
from itertools import combinations

with open(r"adventofcode/day8/day8_input.txt","r") as file:
    ascii_map = [[c for char in line.split() for c in char] for line in file]

rows = len(ascii_map)
cols = len(ascii_map[0])
frequencies = defaultdict(list)
[frequencies[ascii_map[r][c]].append(complex(r, c)) for r in range(rows) for c in range(cols)]   
frequencies.pop('.')

def part1_complex():
    antidot = set()
    for freq in frequencies.values():
        for a, b in combinations(freq, 2):
            d = b-a
            if (-1 < (a-d).real < rows) and (-1 < (a-d).imag < cols):
                antidot.add(a-d)
            if (-1 < (b+d).real < rows) and (-1 < (b+d).imag < cols):
                antidot.add(b+d)
    print(len(antidot))

def part2_complex():
    antidot = set()
    for freq in frequencies.values():
        for a, b in combinations(freq, 2):            
            antidot.add(a)
            antidot.add(b)
            d = b-a
            ad, bd = a-d, b+d
            while (-1 < ad.real < rows) and (-1 < ad.imag < cols): #y/row.real x/col.imag
                antidot.add(ad)
                ad -= d
            while (-1 < bd.real < rows) and (-1 < bd.imag < cols):
                antidot.add(bd)
                bd += d
    print(len(antidot))
  
part1_complex()
part2_complex()
