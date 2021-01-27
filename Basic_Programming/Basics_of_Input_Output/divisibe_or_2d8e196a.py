# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/divisibe-or-2d8e196a/

n = int(input())
a = input().split()
num = ""
for i in range(n):
    if i < (n/2):
        num += a[i][0]
    else:
        num += a[i][-1]
if int(num) % 11 == 0:
    print("OUI")
else:
    print("NON")

