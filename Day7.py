#Bruce force change product range to 2, and remove else for || for part1
numbers = []
with open(r"adventofcode/day7/day7_input.txt","r") as file:
    for line in file:
        total, nums = line.split(':')
        numbers.append([int(total), list(map(int, nums.split()))])

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
