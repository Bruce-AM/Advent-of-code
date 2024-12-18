import timeit
from collections import deque 

grid = [["." for c in range(71)]for r in range(71)]

with open(r"adventofcode/day18/day18_input.txt", "r") as file:
    safe = [list(map(int, line.strip().split(','))) for line in file]

safe_part1 = safe[:1024]
safe_part2 = safe[1024:]
for r,c in safe_part1:
    grid[c][r] = "#"

def part1() -> int: #deque
    visited: set[tuple] = set()
    queue: deque[list[tuple[int,tuple[int,int]]]] = deque([(0,(0,0))])
    while queue:
        cur_dis, (row, col) = queue.popleft()
        dirs = [(row, col-1), (row-1, col), (row, col+1), (row+1, col)]
        for r, c in dirs:
            if -1 < r < 71 and -1 < c < 71:
                if grid[r][c] == "." and (r, c) not in visited:
                    if (r, c) == (70,70):
                        return cur_dis+1
                    visited.add((r,c))
                    queue.append((cur_dis+1,(r, c)))
    return False
print(part1())

left: int= 0
right: int= len(safe_part2)-1
mid: int= (left + right) // 2
for i in range(mid):
    grid[safe_part2[i][1]][safe_part2[i][0]] = "#"
while left < right:   
    if bfs():
        left = mid+1
        mid = (left + right) // 2
        for i in range(left-1, mid):
            grid[safe_part2[i][1]][safe_part2[i][0]] = "#"
    else:
        right = mid
        mid = (left + right) // 2
        for i in range(mid, right+1):
            grid[safe_part2[i][1]][safe_part2[i][0]] = "."
print(safe_part2[mid-1])
