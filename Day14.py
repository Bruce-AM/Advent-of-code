import re, timeit
from math import prod

with open(r"adventofcode/day14/day14_input.txt", "r") as file:
    f = ''.join(file.read().split('\n\n'))
robots = list(map(int, re.findall(r'[-+]?\d+', f)))
length = len(robots)

def both(runs):
    maxprod = 0, 0
    for run in range(1, runs):
        quadrants = [0,0,0,0]
        for i in range(0, length, 4):
            col, row, x, y = robots[i:i+4]
            new_col, new_row = (col + x*run) % 101, (row + y*run) % 103
            if new_col != 50 and new_row != 51:
                quadrants[(new_col // 51) * 2 + (new_row // 52)] += 1      
        prd = max(quadrants)
        if prd > maxprod[0]:
            maxprod = prd, run
    return maxprod, prod(quadrants)

print(both(101)[1])
print(both(101*103)[0][1])
