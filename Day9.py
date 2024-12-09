def part1():
    with open(r"adventofcode/day9/day9_input.txt","r") as file:
        turn = True
        id_number = 0
        disk_map = list()
        amount = 0
        for c in file.read():
            a = int(c)
            if turn:
                [disk_map.append(id_number) for _ in range(a)] 
                id_number += 1
                amount += a
            else:
                [disk_map.append('.') for _ in range(a)]
            turn = not turn

    right = len(disk_map)-1
    total = 0
    for i in range(amount):
        if disk_map[i] == '.':
            while disk_map[right] == '.':
                right -= 1
            total += disk_map[right] * i
            right -= 1
        else:
            total += disk_map[i] * i
    print(total)

def part2():
    with open(r"adventofcode/day9/day9_input.txt","r") as file:
        turn = True
        id_number = 0
        disk_map = list()
        for c in file.read():
            if turn:
                disk_map.append((id_number, int(c)))
                id_number += 1
            else:
                disk_map.append(('.', int(c)))
            turn = not turn

    filesystem = list()
    length = len(disk_map)-1
    for i, (id, amount) in enumerate(disk_map):
        if id == '.' and amount != 0:
            for j in range(length, i, -2):
                n, a = disk_map[j] #id, amount
                if n != '.' and a <= amount:
                    [filesystem.append(n) for _ in range(a)]
                    amount -= a
                    disk_map[j] = ('.', a)
                    if amount == 0:
                        break
            if amount:
                [filesystem.append('.')for _ in range(amount)]
        else:
            [filesystem.append(id) for _ in range(amount)]
    print(sum(i * c for i, c in enumerate(filesystem) if c != '.'))

part1()
part2()
