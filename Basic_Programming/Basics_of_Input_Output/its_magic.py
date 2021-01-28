# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/its-magic/

n = int(input())
a = [int(item) for item in input().split()]
list_sum = sum(a)
num = list_sum%7
list_sum -= num
ans = max(a)
ans_ind = len(a) + 1
while(list_sum > 0):
    if num in a:
        if num < ans:
            ans = num
            ans_ind = a.index(ans)
        elif num == ans:
            if 
    
    