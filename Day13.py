import re

with open(r"day13_input.txt", "r") as file:
    a = file.readlines()

claw_machines = []
cur_machine = []
for string in a:
    if string != '\n':
        cur_machine.append((tuple(map(int, re.findall(r'[-+]?\d+', string)))))
    else:
        claw_machines.append(cur_machine)
        cur_machine = []
claw_machines.append(cur_machine)

def part1(p2):
    tokens = 0
    for a, b, prize in claw_machines:
        b_times = (a[0] * (prize[1]+p2) - a[1] * (prize[0]+p2)) / (a[0] * b[1] - a[1] * b[0])
        a_times = ((prize[0]+p2) - (b[0] * b_times)) / a[0]
        if b_times == int(b_times) and a_times == int(a_times):         
            tokens +=  a_times * 3 + b_times
    print(int(tokens))

part1(0)
part1(10000000000000)
