import heapq

with open(r"day16_input.txt", "r") as file:
    grid:list[list[str]] = [[char for char in line.strip()] for line in file]

rows:int = len(grid)
cols:int = len(grid[0])
start:tuple[int] = rows-2, 1
end:tuple[int] = 1, cols-2

def part1() -> int:
    visited:set[tuple] = {}
    queue:list[tuple] = list()
    heapq.heappush(queue, (0, 2, start))
    while queue:
        score, prev_dir, (row, col) = heapq.heappop(queue)
        if (row,col) == end:
            return score
        if (row, col, prev_dir) in visited and visited[(row, col, prev_dir)] <= score:
            continue
        visited[(row, col, prev_dir)] = score
        dirs = [(row, col-1), (row-1, col), (row, col+1), (row+1, col)]
        for dir, (next_r, next_c) in enumerate(dirs):
            if grid[next_r][next_c] in [".", "E"]:                  
                s:int = score+1 if dir == prev_dir else score+1001
                heapq.heappush(queue, (s, dir, (next_r, next_c)))

def main() -> print:
    print(part1())

main()
