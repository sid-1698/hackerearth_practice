# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/bricks-game-5140869d/

n = int(input())
m = 1
while(True):
    bricks = (3*m*(m+1))/2
    if bricks >= n:
        break
    m+=1

if n > (3*m*m - m)/2:
    print("Motu")
else:
    print("Patlu")