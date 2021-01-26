# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/mojtaba-prepares-contest-29b2a044/description/

t = int(input())
print(t)
for _ in range(t):
    g,p = map(int, input().split())
    n = int(input())
    solved_f = 0
    solved_s = 0
    for _ in range(n):
        f,s = map(int, input().split())
        if f==1:
            solved_f+=1
        if s==1:
            solved_s+=1
    
    print(min(g*solved_f + p*solved_s, g*solved_s + p*solved_f))