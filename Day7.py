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
