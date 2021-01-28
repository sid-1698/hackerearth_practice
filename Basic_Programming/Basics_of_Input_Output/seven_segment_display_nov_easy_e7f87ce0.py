# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/seven-segment-display-nov-easy-e7f87ce0/

t = int(input())
matchsticks_required = [6,2,5,5,4,5,6,3,7,6]
for _ in range(t):
    n = input()
    matchsticks_used = 0
    for digit in n:
        matchsticks_used += matchsticks_required[int(digit)]
    if matchsticks_used%2 == 0:
        max_num = "1"*int(matchsticks_used/2)
    else:
        max_num = "1"*int((matchsticks_used-3)/2)
        max_num = "7"+max_num
    print(max_num)