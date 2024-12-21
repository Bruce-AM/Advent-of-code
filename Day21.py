import timeit

with open(r"adventofcode/day21/day21_input.txt", "r") as file:
    codes = [line for line in file.read().split()]

numpad = {"7":(0,0),"8":(0,1),"9":(0,2),
          "4":(1,0),"5":(1,1),"6":(1,2),
          "1":(2,0),"2":(2,1),"3":(2,2),
                    "0":(3,1),"A":(3,2)}

dirpad = {          "^":(0,1),"A":(0,2),
          "<":(1,0),"v":(1,1),">":(1,2)}
numcode = list(map(lambda c: int(c.strip("A")), codes))
