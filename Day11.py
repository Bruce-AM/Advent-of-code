import timeit
from collections import defaultdict 
import math

def part():
    with open(r"day11_input.txt", "r") as file:
        stones = file.readline().split()
    
    numbers = defaultdict(int)
    for num in stones:
        numbers[num] += 1
    
    for _ in range(75):
        new_numbers = defaultdict(int)
        for num, amount in numbers.items():
            if len(num) % 2:
                n = int(num)
                if n:
                    new_numbers[str(n*2024)] += amount
                else:
                    new_numbers['1'] += amount
            else:
                half = len(num)//2
                new_numbers[num[:half]] += amount
                new_numbers[str(int(num[half:]))] += amount
        numbers = new_numbers
    print(sum(numbers.values()))

#or
def part_v2():
    with open(r"day11_input.txt", "r") as file:
        stones = map(int, file.readline().split())
    
    numbers = defaultdict(int)
    for num in stones:
        numbers[num] += 1

    for _ in range(75):
        new_numbers = defaultdict(int)
        for num, amount in numbers.items():
            if num:
                length = math.floor(math.log10(num))+1
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

part_v2()
