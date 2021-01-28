# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/arithmetic-progression-1-81131fa7/
t = int(input())
for _ in range(t):
    a,b,c = map(int, input().split())
    ans = abs((b-a)-(c-b))
    ans = (ans+1)//2
    print(ans)