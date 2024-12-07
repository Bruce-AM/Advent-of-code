#Bruce force change product range to 2, and remove else for || for part1
reports = []
with open('adventofcode/day2/day2_input.txt', 'r') as file:
    reports = [list(map(int, line.split())) for line in file]

total = 0
for desire, digits in numbers:
    variants = product(range(3), repeat = len(digits)-1)
    for var in variants:
        cur_sum = digits[0]
        for i, x in enumerate(digits[1:]):
            if (op := var[i]) == 0:
                cur_sum *= x
            elif op == 1:
                cur_sum += x
            else:
                cur_sum = int(str(cur_sum) + str(x))
        if cur_sum == desire:
            total += desire
            break
print(total)

""" #same but with lambda
ops = [
    lambda a, b: a * b,
    lambda a, b: a + b,
    lambda a, b: int(str(a) + str(b))
]
total = 0
for desire, digits in numbers:
    variants = product(range(3), repeat = len(digits)-1)
    for var in variants:
        cur_sum = digits[0]
        for i, x in enumerate(digits[1:]):
            cur_sum = ops[var[i]](cur_sum, x)
        if cur_sum == desire:
            total += desire
            break
return total"""