# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/palindrome-check-2/description/

s = input()
for i in range(int(len(s)/2)):
    if s[i] != s[len(s)-i-1]:
        break
if i != int(len(s)/2)-1:
    print("NO")
else:
    print("YES")    