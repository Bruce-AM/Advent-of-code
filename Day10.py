from collections import deque

with open(r"day10_input.txt", "r") as file:
    grid = [[d for d in map(int, line.split())] for line in file]

rows, cols = len(grid), len(grid[0])
trailheads = [(r,c) for r in range(rows) for c in range(cols) if grid[r][c] == 0]

def part1():
    total = 0
    for trail in trailheads:
        visited = {trail}
        queue = deque(trail)
        while queue:
            row, col = queue.popleft()
            height = grid[row][col]+1
            dirs = [(row, col-1), (row-1, col), (row, col+1), (row+1, col)]
            for r, c in dirs:
                if -1 < r < rows and -1 < c < cols:
                    if grid[r][c] == height and (r,c) not in visited:
                        if grid[r][c] != 9:
                            queue.append((r,c))
                        else:
                            total += 1
                        visited.add((r,c))
    print(total)

def part2():
    total = 0
    for trail in trailheads:
        queue = deque(trail)
        while queue:
            row, col = queue.popleft()
            height = grid[row][col]+1
            dirs = [(row, col-1), (row-1, col), (row, col+1), (row+1, col)]
            for r, c in dirs:
                if -1 < r < rows and -1 < c < cols:
                    if grid[r][c] == height:
                        if grid[r][c] != 9:
                            queue.append((r,c))
                        else:
                            total += 1
    print(total)

part1()
part2()
