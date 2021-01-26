# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/vc-pairs/

t = int(input())
vowels = ['a','e','i','o','u']
for _ in range(t):
    n = int(input())
    s = input()
    cnt = 0 
    for i,item in enumerate(s[:-1]):
        if((item not in vowels) & (s[i+1] in vowels)):
            cnt += 1
    print(cnt)