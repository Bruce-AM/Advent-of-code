import re

with open(r"day13_input.txt", "r") as file:
    a = ''.join(file.read().split('\n\n'))
claw_machines = list(map(int, re.findall(r'\d+', a)))
length = len(claw_machines)

def part1(p2):
    tokens = 0
    for i in range(0, length, 6):
        ax,ay, bx,by, prizex,prizey = claw_machines[i:i+6]
        b_times = (ax * (prizey+p2) - ay * (prizex+p2)) / (ax * by - ay * bx)
        a_times = ((prizex+p2) - (bx * b_times)) / ax
        if b_times == int(b_times) and a_times == int(a_times):         
            tokens +=  a_times * 3 + b_times
    print(int(tokens))

part1(0)
part1(10000000000000)
