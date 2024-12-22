import timeit
from functools import lru_cache

with open(r"adventofcode/day21/day21_input.txt", "r") as file:
    codes = [line for line in file.read().split()]

numpad = {"7":(0,0),"8":(0,1),"9":(0,2),
          "4":(1,0),"5":(1,1),"6":(1,2),
          "1":(2,0),"2":(2,1),"3":(2,2),
                    "0":(3,1),"A":(3,2)}

dirpad = {          "^":(0,1),"A":(0,2),
          "<":(1,0),"v":(1,1),">":(1,2)}
numcode = list(map(lambda c: int(c.strip("A")), codes))
def part2_v1(max_depth):
    def sequence(code):
        shortest = 0
        r1 = numpad["A"]
        for num in code:
            y, x = r1[0] - numpad[num][0], r1[1] - numpad[num][1]
            vertical = ("^" * y if y > 0 else "v" * -y)
            horizontal = ("<" * x if x > 0 else ">" * -x)
            if r1[1] == 0 and numpad[num][0] == 3:
                sequence_of_buttons = horizontal + vertical + "A"  
            elif r1[0] == 3 and numpad[num][1] == 0: 
                sequence_of_buttons = vertical + horizontal + "A"
            else:
                if numpad[num][0] > r1[0] and numpad[num][1] > r1[1]:
                    sequence_of_buttons = vertical + horizontal + "A"
                elif numpad[num][0] < r1[0] and numpad[num][1] > r1[1]:
                    sequence_of_buttons = vertical + horizontal + "A"
                elif numpad[num][0] < r1[0] and numpad[num][1] < r1[1]:
                    sequence_of_buttons = horizontal + vertical + "A"
                else:
                    sequence_of_buttons = horizontal + vertical + "A"
            r1 = numpad[num]

            @lru_cache(None)
            def dirrectional_keypads(sequence_of_buttons, hand_pos, depth):
                if depth == max_depth:
                    return len(sequence_of_buttons)
                last_len = 0
                hand_pos = dirpad["A"]
                for char in sequence_of_buttons:
                    y, x = hand_pos[0] - dirpad[char][0], hand_pos[1] - dirpad[char][1]
                    vertical = ("^" * y if y > 0 else "v" * -y)
                    horizontal = ("<" * x if x > 0 else ">" * -x)
                    if hand_pos[1] == 0 and dirpad[char][0] == 0: #we dont hit (0,0)
                        cur_sequence = horizontal + vertical + "A"
                    elif hand_pos[0] == 0 and dirpad[char][1] == 0:
                        cur_sequence = vertical + horizontal + "A"
                    else:
                        if dirpad[char][0] > hand_pos[0] and dirpad[char][1] > hand_pos[1]:
                            cur_sequence = vertical + horizontal + "A"
                        elif dirpad[char][0] < hand_pos[0] and dirpad[char][1] > hand_pos[1]:
                            cur_sequence = vertical + horizontal + "A"
                        elif dirpad[char][0] < hand_pos[0] and dirpad[char][1] < hand_pos[1]:
                            cur_sequence = horizontal + vertical + "A"
                        else:
                            cur_sequence = horizontal + vertical + "A"               
                    last_len += dirrectional_keypads(cur_sequence, hand_pos, depth + 1)
                    hand_pos = dirpad[char]
                return last_len

            shortest += dirrectional_keypads(sequence_of_buttons, dirpad["A"], 0)
        return shortest

    print(sum(sequence(code) * numcode[i] for i, code in enumerate(codes)))

def main():
    part2_v1(2)
    part2_v1(25)
main()
