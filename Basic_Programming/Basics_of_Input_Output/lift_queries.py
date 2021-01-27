# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/lift-queries/

t = int(input())
a = 0
b = 7
for _ in range(t):
    n = int(input())
    if abs(n-a) < abs(n-b):
        a = n
        print("A")
    elif abs(n-a) == abs(n-b):
        if a < b:
            a = n
            print("A")
        else:
            b = n
            print("B")
    else:
        b = n
        print("B")