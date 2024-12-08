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
            [part2_antidot.add(n) for n in (a, b)]
            d = b-a
            for pos, dis in ((a-d,-d), (b+d,d)):
                if (-1 < pos.real < rows) and (-1 < pos.imag < cols):
                    part1_antidot.add(pos)
                    while (-1 < pos.real < rows) and (-1 < pos.imag < cols):
                        part2_antidot.add(pos)
                        pos += dis
    print(len(part1_antidot), len(part2_antidot.union(part1_antidot)))
  
both_parts()
