with open(r"day15_input.txt", "r") as file:
    grid_str, moves_str = file.read().split("\n\n")
#list(list(str))
grid = [[char for char in line.strip()] for line in grid_str.split('\n')]
#find robot position
rows, cols = len(grid), len(grid[0])
robot_pos = 0,0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '@':
            grid[r][c] = '.'
            robot_pos = r, c
            break
#rewrite char moves to indexes of dirs list
move_dirs = []
for m in moves_str:
    if m == '<':
        move_dirs.append(0)
    elif m == '^':
        move_dirs.append(1)
    elif m == '>':
        move_dirs.append(2)
    elif m == 'v':
        move_dirs.append(3)

dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]#left up right down
def part1(robot_pos):
    for m in move_dirs:
        dy, dx = dirs[m]
        next_y, next_x = robot_pos[0] + dy, robot_pos[1] + dx
        if grid[next_y][next_x] == '.':
            robot_pos = next_y, next_x
        elif grid[next_y][next_x] == 'O':    
            bnp = next_y + dy, next_x + dx
            boxes_new_pos = [bnp]
            while grid[bnp[0]][bnp[1]] == 'O':
                bnp = bnp[0] + dy, bnp[1] + dx
                boxes_new_pos.append(bnp)
            if grid[bnp[0]][bnp[1]] == '.':
                for y, x in boxes_new_pos:
                    grid[y][x] = 'O'
                grid[next_y][next_x] = '.'
                robot_pos = next_y, next_x
    print(sum(100 * r + c for r in range(rows) for c in range(cols) if grid[r][c] == 'O'))


def part2(robot_pos):
    robot_pos = robot_pos[0], robot_pos[1]*2
    for r in range(rows): #rebuild grid
        for c in range(cols-1, -1, -1):
            if grid[r][c] == "#":
                grid[r].insert(c,"#")
            elif grid[r][c] == "O":
                grid[r][c] = "]"
                grid[r].insert(c,"[")
            elif grid[r][c] == ".":
                grid[r].insert(c,".")
            elif grid[r][c] == "@":             
                grid[r][c] = "."
                grid[r].insert(c,".")
    row, col = len(grid), len(grid[0])

    for m in move_dirs:
        dy, dx = dirs[m] # current dirrection
        next_y, next_x = robot_pos[0] + dy, robot_pos[1] + dx
        if grid[next_y][next_x] == '.':
            robot_pos = next_y, next_x
        elif grid[next_y][next_x] in ("[","]"):
            if m in (0,2): #left right
                bnp = next_y + dy, next_x + dx
                boxes_new_pos = [bnp]
                while grid[bnp[0]][bnp[1]] in ("[","]"):
                    bnp = bnp[0] + dy, bnp[1] + dx
                    boxes_new_pos.append(bnp)
                if grid[bnp[0]][bnp[1]] == '.':
                    for i, (y, x) in enumerate(boxes_new_pos):
                        if i%2:
                            grid[y][x] = "]" if m else "["      
                        else:
                            grid[y][x] = "[" if m else "]"
                    grid[next_y][next_x] = '.'
                    robot_pos = next_y, next_x
            else: #up down
                bnp = next_y, next_x
                boxes_new_pos = [bnp] #visited for bfs, list intended
                bracket = 1 if grid[bnp[0]][bnp[1]] == "[" else -1
                boxes_new_pos.append((bnp[0],bnp[1] + bracket))
                queue = boxes_new_pos.copy() #queue for bfs
                while queue: #bfs to find #
                    next_b_p = queue.pop(0)
                    bnp = next_b_p[0] + dy, next_b_p[1] + dx
                    if bnp not in boxes_new_pos:
                        if grid[bnp[0]][bnp[1]] in ("[","]"):
                            bracket = 1 if grid[bnp[0]][bnp[1]] == "[" else -1
                            queue.append(bnp)
                            queue.append((bnp[0],bnp[1] + bracket))
                            boxes_new_pos.append(bnp)
                            boxes_new_pos.append((bnp[0],bnp[1] + bracket))
                        elif grid[bnp[0]][bnp[1]] == "#":
                            break
                else: #if we didn't find # (no break)
                    cur_dir = 1 if m == 3 else -1
                    for y, x in reversed(boxes_new_pos):
                        grid[y + cur_dir][x] = grid[y][x]
                        grid[y][x] = '.'
                    robot_pos = next_y, next_x
    print(sum(100 * r + c for r in range(row) for c in range(col) if grid[r][c] == '['))

def main():
    part1(robot_pos)
    part2(robot_pos)
main()
