input = ''.join(file) #read.file()

#part1
return sum(int(x)*int(y) for x, y in (re.findall(r"mul\((\d+),(\d+)\)", input)))

part2
muls = re.findall(r"mul\((\d+),(\d+)\)|(don't\(\)|do\(\))", input)
do = True
total = 0
for x, y, b in muls:
    if do and x:
        total += int(x) * int(y)
    else:
        do = b == "do()"            
return total
