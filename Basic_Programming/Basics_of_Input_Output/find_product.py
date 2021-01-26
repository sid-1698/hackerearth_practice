# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/find-product/description/

input()
a = map(int, input().split())
prod = 1
for item in a:
    prod *= item
    prod = prod%(1000000007)
print(prod)