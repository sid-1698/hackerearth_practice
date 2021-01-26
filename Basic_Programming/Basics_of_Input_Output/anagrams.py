# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/anagrams-651/description/

t = int(input())
for _ in range(t):
    a = input()
    b = input()

    count_a = [0]*26
    count_b = [0]*26
    for item in a:
        count_a[ord(item)-ord('a')] += 1
    for item in b:
        count_b[ord(item)-ord('a')] += 1
    deletions = 0
    for i in range(26):
        deletions += abs(count_a[i] - count_b[i])
    print(deletions)