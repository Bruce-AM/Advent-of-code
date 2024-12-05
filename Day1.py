left_lst = list()
right_lst = list()
left_dct = defaultdict(int)
right_dct = defaultdict(int)

with open('leftrightlists.txt', 'r') as file:
    for line in file:
        l, r = map(int, line.split())
        left_lst.append(l)
        right_lst.append(r)
        left_dct[l] += 1
        right_dct[r] += 1

left_lst.sort()
right_lst.sort()
distance = sum(abs(l - r) for l, r in zip(left_lst, right_lst))
print(f'Distance: {distance}')

similarity_score = 0
for n, amount in left_dct.items():
    if n in right_dct:
        similarity_score += (n * right_dct[n]) * amount
print(f'Score: {similarity_score}')
