# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/two-strings-4/

t = int(input())
for _ in range(t):
    s1,s2=map(str, input().split())
    print(s1,s2)
    if sorted(s1) == sorted(s2):
        print("YES")
    else:
        print("NO")