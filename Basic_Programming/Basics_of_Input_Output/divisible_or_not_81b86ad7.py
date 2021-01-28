# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/divisible-or-not-81b86ad7/

n = input()
last_digit = int(input().split()[-1])
if last_digit%10 == 0:
    print("Yes")
else:
    print("No")
