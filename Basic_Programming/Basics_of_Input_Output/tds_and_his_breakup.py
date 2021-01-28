# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/tds-and-his-breakup/

n = int(input())
threshold = int(input())
for _ in range(n):
    if int(input()) >= threshold:
        print("YES")
    else:
        print("NO")