from collections import defaultdict 
import timeit

def both():
    with open(r"day11_input.txt", "r") as file:
        stones = map(int, file.readline().split())
    
    numbers = defaultdict(int)
    [numbers[num] += 1 for num in stones]

    for _ in range(75): # print(sum(numbers.values())) if _ == 25
        new_numbers = defaultdict(int)
        for num, amount in numbers.items():
            if num:
                length = len(str(num)) #math.floor(math.log10(num))+1
                if length % 2:
                    new_numbers[num * 2024] += amount
                else:
                    half = 10**(length // 2)
                    new_numbers[num // half] += amount
                    new_numbers[num % half] += amount          
            else:
                new_numbers[1] += amount
        numbers = new_numbers
    print(sum(numbers.values()))

both()
