import heapq

with open(r"day16_input.txt", "r") as file:
    grid:list[list[str]] = [[char for char in line.strip()] for line in file]

rows:int = len(grid)
cols:int = len(grid[0])
start:tuple[int] = rows-2, 1
end:tuple[int] = 1, cols-2

visited:dict[tuple, int] = {}
queue:list[tuple] = [(0, 2, start, [start])]
best_score:int = 100000
all_paths:set = set()
while queue:
    score, prev_dir, (row, col), path = heapq.heappop(queue)
    if (row,col) == end:
        best_score = score
        all_paths |= set(path)
    if (row, col, prev_dir) in visited and visited[(row, col, prev_dir)] < score:
        continue
    visited[(row, col, prev_dir)] = score
    dirs = [(row, col-1), (row-1, col), (row, col+1), (row+1, col)]
    for dir, (next_r, next_c) in enumerate(dirs):
        if grid[next_r][next_c] in [".", "E"]:                  
            s:int = score+1 if dir == prev_dir else score+1001
            if s <= best_score:
                heapq.heappush(queue, (s, dir, (next_r, next_c), path+[(next_r, next_c)]))
print(best_score, len(all_paths))
