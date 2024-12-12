from collections import defaultdict, deque

with open(r"day12_input.txt", "r") as file:
    grid = [[char for line in lines for char in line.split()] for lines in file]

rows, cols = len(grid), len(grid[0])
regions = defaultdict(set)
for r in range(rows):
    for c in range(cols):
        regions[grid[r][c]].add((r,c))

def both():
    garden = defaultdict(set)
    total_sides = 0
    for key in regions: # for A, B, C, D, E
        garden[key] = []
        dct_index = 0
        while regions[key]: # if set is not empty
            garden[key].append({})
            visited = {regions[key].pop()}
            queue = deque(visited)
            sides = 4
            while queue:        
                row, col = queue.popleft()
                garden[key][dct_index][(row, col)] = [0,0,0,0]
                dirs = [(row, col-1), (row-1, col), (row, col+1), (row+1, col)]
                for i, (r, c) in enumerate(dirs):
                    if -1 < r < rows and -1 < c < cols:
                        if grid[r][c] == key:
                            if (r, c) in visited:
                                sides -= 1
                            else:
                                queue.append((r, c))
                                regions[key].remove((r, c))
                                visited.add((r, c))
                                sides += 3
                        else:
                            garden[key][dct_index][(row, col)][i] = 1
                    else:
                        garden[key][dct_index][(row, col)][i] = 1
            total_sides += sides*len(visited)
            dct_index += 1
    print(total_sides) #part1

    def region_size(dct):
        min_x, min_y, max_x, max_y = 1000,1000,0,0
        for y, x in dct:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
        return min_x, min_y, max_x+1, max_y+1

    total_sides = 0 #garden[A]:[{(pos):[left,top,right,bottom], (pos1):[left,top,right,bottom]}, {dict}, {dict}]}
    for key, key_region in garden.items(): # A, list of dicts(regions)
        for reg in key_region: #for each dict(reg)
            start_x, start_y, end_x, end_y = region_size(reg) #find rectangle size
            tops, bots = 0, 0
            lefts, rights = 0, 0
            for r in range(start_y, end_y): #traverse region and find all horizontal sides
                saw_top_side, saw_bot_side = False, False #memo gaps           
                for c in range(start_x, end_x): 
                    if (r, c) in reg:
                        if reg[(r, c)][1] == 1:                         
                            if not saw_top_side: #top horizontal
                                tops += 1
                            saw_top_side = True
                        else:
                            saw_top_side = False
                        if reg[(r, c)][3] == 1:          
                            if not saw_bot_side: #bot horizontal
                                bots += 1
                            saw_bot_side = True
                        else:
                            saw_bot_side = False
                    else:
                        saw_top_side, saw_bot_side = False, False
            for c in range(start_x, end_x): #traverse region and find all vertical sides
                saw_left_side, saw_right_side = False, False #memo gaps          
                for r in range(start_y, end_y): 
                    if (r, c) in reg:
                        if reg[(r, c)][0] == 1:        
                            if not saw_left_side: #left vertical
                                lefts += 1
                            saw_left_side = True
                        else:
                            saw_left_side = False
                        if reg[(r, c)][2] == 1:                           
                            if not saw_right_side: #right vertical
                                rights += 1
                            saw_right_side = True
                        else:
                            saw_right_side = False
                    else:
                        saw_left_side, saw_right_side = False, False
            total_sides += (tops+bots+lefts+rights) * len(reg)
    print(total_sides)
both()
