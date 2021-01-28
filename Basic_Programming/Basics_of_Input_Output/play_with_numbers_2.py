# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/play-with-numbers-2/

n,q = map(int, input().split())
arr = input().split()
a = [0]
for item in arr:
    a.append(int(item)+a[-1])
for _ in range(q):
    l,r = map(int, input().split())
    print((a[r]-a[l-1])//(r-l+1))