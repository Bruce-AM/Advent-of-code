import timeit

#day24_input
with open("adventofcode/day24/day24_input.txt","r") as file:
    i, g = file.read().split("\n\n")
inputs = [line.split(": ") for line in i.split("\n")]
gates = [line.split(" ") for line in g.split("\n")]

wires = {k: v == "1" for k, v in inputs}
op = {"AND":0,"OR":1,"XOR":2}
ops = [
    lambda a, b: wires[a] & wires[b],
    lambda a, b: wires[a] | wires[b],
    lambda a, b: wires[a] ^ wires[b]
]

def part1():
    while gates:
        length = len(gates)-1
        for i, gate in enumerate(reversed(gates)):
            a, o, b, _, res = gate
            if a in wires and b in wires:
                wires[res] = ops[op[o]](a, b)
                gates.pop(length - i)
    num = []
    for k, v in wires.items():
        if k[0] == "z" and k[1] in ("0123456789"):
            num.append((k, v))
    num.sort(key = lambda a: int(a[0][1:]))
    print(int(''.join("1" if x else "0" for _, x in reversed(num)), 2))

def main():
    part1()
  
main()
