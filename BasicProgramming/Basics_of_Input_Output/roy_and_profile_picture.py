# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/roy-and-profile-picture/description/

l = float(input())
n = int(input())
for _ in range(n):
    w,h = map(float, input().split())
    if ((w<l) | (h<l)):
        print("UPLOAD ANOTHER")
    elif(w == h):
        print("ACCEPTED")
    else:
        print("CROP IT")