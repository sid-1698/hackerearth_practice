# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/count-divisors/

# https://www.geeksforgeeks.org/count-divisors-n-on13/ O(n^1/3)

#Naive Method
l,r,k = map(int, input().split())
cnt = 0
for i in range(l,r+1):
    if i%k == 0:
        cnt+=1
print(cnt)
