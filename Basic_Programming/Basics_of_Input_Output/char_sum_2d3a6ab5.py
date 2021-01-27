# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/char-sum-2d3a6ab5/

s = input()
weight = 0
for item in s:
    weight += (ord(item)-ord('a')+1)
print(weight)