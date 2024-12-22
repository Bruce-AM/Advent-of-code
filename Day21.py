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

def sequence(code):
    shortest = 0
    r1 = numpad["A"]
    for num in code:
        sequence_of_buttons = str()
        y = r1[0] - numpad[num][0]
        x = r1[1] - numpad[num][1]
        if r1[1] == 0 and numpad[num][0] == 3: #x first so we dont hit (3,0)
            sequence_of_buttons += ("<" * x if x > 0 else ">" * -x) + ("^" * y if y > 0 else "v" * -y) + "A"               
        elif r1[0] == 3 and numpad[num][1] == 0: #y first so we dont hit (3,0)
            sequence_of_buttons += ("^" * y if y > 0 else "v" * -y) + ("<" * x if x > 0 else ">" * -x) + "A"       
        else:
            if numpad[num][0] > r1[0] and numpad[num][1] > r1[1]:
                sequence_of_buttons += ("^" * y if y > 0 else "v" * -y) + ("<" * x if x > 0 else ">" * -x) + "A"
            elif numpad[num][0] < r1[0] and numpad[num][1] > r1[1]:
                sequence_of_buttons += ("^" * y if y > 0 else "v" * -y) + ("<" * x if x > 0 else ">" * -x) + "A"
            elif numpad[num][0] < r1[0] and numpad[num][1] < r1[1]:
                sequence_of_buttons += ("<" * x if x > 0 else ">" * -x) + ("^" * y if y > 0 else "v" * -y) + "A"
            else:
                sequence_of_buttons += ("<" * x if x > 0 else ">" * -x) + ("^" * y if y > 0 else "v" * -y) + "A"
        r1 = numpad[num]

        def dirrectional_keypads(sequence_of_buttons):
            cur_sequence = str()
            hand_pos = dirpad["A"]
            for char in sequence_of_buttons:
                y = hand_pos[0] - dirpad[char][0]
                x = hand_pos[1] - dirpad[char][1]
                if hand_pos[1] == 0 and dirpad[char][0] == 0: #we dont hit (0,0)
                    cur_sequence += ("<" * x if x > 0 else ">" * -x) + ("^" * y if y > 0 else "v" * -y) + "A"
                elif hand_pos[0] == 0 and dirpad[char][1] == 0:
                    cur_sequence += ("^" * y if y > 0 else "v" * -y) + ("<" * x if x > 0 else ">" * -x) + "A"
                else:
                    if dirpad[char][0] > hand_pos[0] and dirpad[char][1] > hand_pos[1]:
                        cur_sequence += ("^" * y if y > 0 else "v" * -y) + ("<" * x if x > 0 else ">" * -x) + "A"
                    elif dirpad[char][0] < hand_pos[0] and dirpad[char][1] > hand_pos[1]:
                        cur_sequence += ("^" * y if y > 0 else "v" * -y) + ("<" * x if x > 0 else ">" * -x) + "A"
                    elif dirpad[char][0] < hand_pos[0] and dirpad[char][1] < hand_pos[1]:
                        cur_sequence += ("<" * x if x > 0 else ">" * -x) + ("^" * y if y > 0 else "v" * -y) + "A"
                    else:
                        cur_sequence += ("<" * x if x > 0 else ">" * -x) + ("^" * y if y > 0 else "v" * -y) + "A"
                hand_pos = dirpad[char]
            return cur_sequence

        for amount_of_keypads in range(2): #amount of dirrections keypads after numeric
            sequence_of_buttons = dirrectional_keypads(sequence_of_buttons)
        shortest += len(sequence_of_buttons)
    return shortest

total = 0
for i, code in enumerate(codes):
    a = sequence(code)
    total += a * numcode[i]
print(total)

#part 2 recursion not working 
def part2_v1():
    def sequence(code):
        shortest = 0
        r1 = numpad["A"]
        for num in code:
            y = r1[0] - numpad[num][0]
            x = r1[1] - numpad[num][1]
            if r1[1] == 0 and numpad[num][0] == 3: #y first so we dont hit (3,0)
                sequence_of_buttons = ("<" * x if x > 0 else ">" * -x) + ("^" * y if y > 0 else "v" * -y) + "A"               
            elif r1[0] == 3 and numpad[num][1] == 0: #x first so we dont hit (3,0)
                sequence_of_buttons = ("^" * y if y > 0 else "v" * -y) + ("<" * x if x > 0 else ">" * -x) + "A"       
            else:
                if numpad[num][0] > r1[0] and numpad[num][1] > r1[1]:
                    sequence_of_buttons = ("^" * y if y > 0 else "v" * -y) + ("<" * x if x > 0 else ">" * -x) + "A"
                elif numpad[num][0] < r1[0] and numpad[num][1] > r1[1]:
                    sequence_of_buttons = ("^" * y if y > 0 else "v" * -y) + ("<" * x if x > 0 else ">" * -x) + "A"
                elif numpad[num][0] < r1[0] and numpad[num][1] < r1[1]:
                    sequence_of_buttons = ("<" * x if x > 0 else ">" * -x) + ("^" * y if y > 0 else "v" * -y) + "A"
                else:
                    sequence_of_buttons = ("<" * x if x > 0 else ">" * -x) + ("^" * y if y > 0 else "v" * -y) + "A"
            r1 = numpad[num]

            @lru_cache(None)
            def dirrectional_keypads(sequence_of_buttons, hand_pos, depth):
                if depth == 24: #depth of recursion without numpad
                    print(sequence_of_buttons) #at second num shows wrong moves
                    return len(sequence_of_buttons)
                last_len = 0
                for char in sequence_of_buttons:
                    y = hand_pos[0] - dirpad[char][0]
                    x = hand_pos[1] - dirpad[char][1]
                    if hand_pos[1] == 0 and dirpad[char][0] == 0: #we dont hit (0,0)
                        cur_sequence = ("<" * x if x > 0 else ">" * -x) + ("^" * y if y > 0 else "v" * -y) + "A"
                    elif hand_pos[0] == 0 and dirpad[char][1] == 0:
                        cur_sequence = ("^" * y if y > 0 else "v" * -y) + ("<" * x if x > 0 else ">" * -x) + "A"
                    else:
                        if dirpad[char][0] > hand_pos[0] and dirpad[char][1] > hand_pos[1]:
                            cur_sequence = ("^" * y if y > 0 else "v" * -y) + ("<" * x if x > 0 else ">" * -x) + "A"
                        elif dirpad[char][0] < hand_pos[0] and dirpad[char][1] > hand_pos[1]:
                            cur_sequence = ("^" * y if y > 0 else "v" * -y) + ("<" * x if x > 0 else ">" * -x) + "A"
                        elif dirpad[char][0] < hand_pos[0] and dirpad[char][1] < hand_pos[1]:
                            cur_sequence = ("<" * x if x > 0 else ">" * -x) + ("^" * y if y > 0 else "v" * -y) + "A"
                        else:
                            cur_sequence = ("<" * x if x > 0 else ">" * -x) + ("^" * y if y > 0 else "v" * -y) + "A"               
                    last_len += dirrectional_keypads(cur_sequence, hand_pos, depth + 1)
                    hand_pos = dirpad[char]
                    
                return last_len

            shortest += dirrectional_keypads(sequence_of_buttons, dirpad["A"], 0)

        print(shortest)
        return shortest

total = 0
for i, code in enumerate(codes[:1]): # only first number for test
    a = sequence(code)
    total += a * numcode[i]
print(total)







