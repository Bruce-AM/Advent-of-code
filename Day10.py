with open(r"day10_input.txt", "r") as file:
    grid = [[int(d) for l in line.split() for d in l] for line in file]

rows, cols = len(grid), len(grid[0])
trailheads = [(r,c) for r in range(rows) for c in range(cols) if grid[r][c] == 0]

def part1():
    total = 0
    for trail in trailheads:
        visited = {trail}
        queue = [trail]
        while queue:
            row, col = queue.pop()
            height = grid[row][col]+1
            for r, c in [(row, col-1), (row-1, col), (row, col+1), (row+1, col)]:
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
        queue = [trail]
        while queue:
            row, col = queue.pop()
            height = grid[row][col]+1
            for r, c in [(row, col-1), (row-1, col), (row, col+1), (row+1, col)]:
                if -1 < r < rows and -1 < c < cols:
                    if grid[r][c] == height:
                        if grid[r][c] != 9:
                            queue.append((r,c))
                        else:
                            total += 1
    print(total)

part1()
part2()
