import timeit

with open("adventofcode/day19/day19_input.txt","r") as file:
    tow, pat = file.read().split("\n\n")
towels = tow.strip().split(", ")
patterns = pat.split("\n")

def part1():
    def dfs(p):
        if not p:
            return True
        for pref in towels:
            if p.startswith(pref):
                if dfs(p[len(pref):]):
                    return True
        return False
    return sum(1 for pattern in patterns if dfs(pattern))

def part2():
    def different_ways(p):
        cache = {}
        def dfs(p):
            if p in cache:
                return cache[p]
            if not p:
                return 1
            total = 0
            for pref in towels:
                if p.startswith(pref):
                    total += dfs(p[len(pref):])
            cache[p] = total            
            return total
        return dfs(p)
    return sum(different_ways(pattern) for pattern in patterns)
  
print(part1())
print(part2())
