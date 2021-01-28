# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/doctors-secret/

length, pages = map(int, input().split())
if ((length<= 23)&(500<=pages<=1000)):
    print("Take Medicine")
else:
    print("Don't take Medicine")