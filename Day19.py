with open("adventofcode/day19/day19_input.txt","r") as file:
    tow, pat = file.read().split("\n\n")
towels, patterns = tow.strip().split(", "), pat.split("\n")

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
print(sum(1 for pattern in patterns if different_ways(pattern)))
print(sum(different_ways(pattern) for pattern in patterns))
