from collections import defaultdict
from itertools import pairwise
import timeit

maze = list[list[str]]
with open(r"day6_input.txt", "r") as file:
    maze = [[char for string in line.split() for char in string] for line in file]

rows = len(maze)
cols = len(maze[0])
guard_pos = ()
for r in range(rows):
    for c in range(cols):
        if maze[r][c] == '^':
            guard_pos = r, c
            break

dirs = [(-1,0), (0,1), (1,0), (0,-1)]
cur_dir = 0

def stuck_in_a_loop(stuck_pos, s_dir):
    
    obs = defaultdict(set)
    while 0 < stuck_pos[0] < rows-1 and 0 < stuck_pos[1] < cols-1:
        sr, sc = stuck_pos
        next_sr = sr + dirs[s_dir][0]
        next_sc = sc + dirs[s_dir][1]

        if maze[next_sr][next_sc] == '#':
            if obs.get(stuck_pos) != None and s_dir in obs[stuck_pos]:                     
                return True
            obs[stuck_pos].add(s_dir)
            s_dir = (s_dir + 1) % 4
        else:          
            stuck_pos = next_sr, next_sc

    return False

part1 = set()
part2 = 0

while 0 < guard_pos[0] < rows-1 and 0 < guard_pos[1] < cols-1:
    gr, gc = guard_pos
    next_r = gr + dirs[cur_dir][0]
    next_c = gc + dirs[cur_dir][1]
    if maze[next_r][next_c] == '#':
        cur_dir = (cur_dir + 1) % 4
    else:
        maze[next_r][next_c] = '#'
        if stuck_in_a_loop(guard_pos, cur_dir):
            part2 += 1
        maze[next_r][next_c] = '.'
        part1.add(guard_pos)
        guard_pos = next_r, next_c

return len(part1)+1, part2
