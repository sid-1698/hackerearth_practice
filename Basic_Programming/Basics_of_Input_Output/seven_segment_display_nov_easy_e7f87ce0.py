# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/seven-segment-display-nov-easy-e7f87ce0/

t = int(input())
matchsticks_required = [6,2,5,5,4,5,6,3,7,6]
for _ in range(t):
    n = int(input())
    matchsticks_used = 0
    if n == 0:
        matchsticks_used = matchsticks_required[0]
    while(n>0):
        matchsticks_used += matchsticks_required[n%10]
        n = int(n/10) 
    print(matchsticks_used)