from collections import defaultdict
from itertools import combinations
import timeit # 0.00095s
with open(r"adventofcode/day8/day8_input.txt","r") as file:
    ascii_map = [[c for char in line.split() for c in char] for line in file]

rows = len(ascii_map)
cols = len(ascii_map[0])
frequencies = defaultdict(list)
[frequencies[ascii_map[r][c]].append(complex(r, c)) for r in range(rows) for c in range(cols)]   
frequencies.pop('.')

def both_parts():
    part1_antidot = set()
    part2_antidot = set()
    for freq in frequencies.values():
        for a, b in combinations(freq, 2):            
            part2_antidot.add(a)
            part2_antidot.add(b)
            d = b-a
            ad, bd = a-d, b+d
            if (-1 < ad.real < rows) and (-1 < ad.imag < cols):
                part1_antidot.add(ad)
                while (-1 < ad.real < rows) and (-1 < ad.imag < cols): #y.row.real x.col.imag
                    part2_antidot.add(ad)
                    ad -= d
            if (-1 < bd.real < rows) and (-1 < bd.imag < cols):
                part1_antidot.add(bd)
                while (-1 < bd.real < rows) and (-1 < bd.imag < cols):
                    part2_antidot.add(bd)
                    bd += d
    print(len(part1_antidot), len(part2_antidot.union(part1_antidot)))
  
both_parts()
