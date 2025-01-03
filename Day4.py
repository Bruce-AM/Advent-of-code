from itertools import chain
import re

with open(r"day4_input.txt", "r") as file:
    matrix: list[list[str]] = [[char for char in line.strip()] for line in file]

row, col = len(matrix), len(matrix[0]) 
search = {"SM","MS"}
total = 0
#part2
for r in range(1, row-1):
    for c in range(1, col-1):
        if matrix[r][c] == 'A':
            if (matrix[r-1][c-1] + matrix[r+1][c+1] in search and 
                matrix[r-1][c+1] + matrix[r+1][c-1] in search):
                total += 1 
#part1
diagpos = [[] for _ in range((row+col-1))]
diagneg = [[] for _ in range((row+col-1))]
for r in range(row):
    for c in range(col):
        diagpos[r+c].append(matrix[r][c])
        diagneg[r+c].append(matrix[r][-c-1])
matrices = ' '.join(''.join(string) for string in chain(matrix, zip(*matrix), diagpos, diagneg))

print(len(re.findall(r"(?=(XMAS|SAMX))", matrices)), total)
