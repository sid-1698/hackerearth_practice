# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/a-movement-1/

n = int(input())
steps = 0
possible = [5,4,3,2,1]
for step in possible:
    while n>=step:
        steps+=1
        n=n-step
print(steps)