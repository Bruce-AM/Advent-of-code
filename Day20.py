with open(r"adventofcode/day20/day20_input.txt", "r") as file:
    grid = [[char for char in line] for line in file.read().split()]

cols, rows = len(grid[0]), len(grid)
start, end = [(r,c) for r in range(rows) for c in range(cols) if grid[r][c] in {"S","E"}]

def build_path():
    path = {end: (0, (None, None))}
    queue = [end]
    while queue:
        row, col = queue.pop()
        dirs = [(row, col-1), (row-1, col), (row, col+1), (row+1, col)]
        for next_r, next_c in dirs:
            if grid[next_r][next_c] == '.' and (next_r, next_c) not in path:
                path[(next_r, next_c)] = path[(row, col)][0]+1, (row, col)
                queue.append((next_r, next_c))
                break
    return path

def part1(path):
    length = len(path)-99
    next = start
    cheats = 0
    for _ in range(length):
        row, col = next
        dirs = [(row, col-2), (row-2, col), (row, col+2), (row+2, col)]
        for next_r, next_c in dirs:
            if -1 < next_r < rows and -1 < next_c < cols:
                if grid[next_r][next_c] == '.':
                    if path[(row, col)][0] - (path[(next_r, next_c)][0] + 2) > 99:
                        cheats += 1
        next = path[next][1]
    print(cheats)

def part2(path):
    length = len(path)-99
    next = start
    cheats = 0
    for _ in range(length): #for each pos on track
        row, col = next
        dirs = [((row-20)+r, (col-20)+c) for r in range(41) for c in range(41) if 1 < abs(r - 20) + abs(c - 20) <= 20]
        for next_r, next_c in dirs: #for each pos in rhomb
            if -1 < next_r < rows and -1 < next_c < cols: #if in bounds
                if grid[next_r][next_c] == '.': #if on track
                    if path[(row, col)][0] - (path[(next_r, next_c)][0] + abs(row-next_r) + abs(col-next_c)) > 99: #99
                        cheats += 1
        next = path[next][1]
    print(cheats)

path = build_path()
part1(path)
part2(path)
