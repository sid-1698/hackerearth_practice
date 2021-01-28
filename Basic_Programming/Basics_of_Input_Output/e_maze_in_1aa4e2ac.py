# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/e-maze-in-1aa4e2ac/

s = input()
moves = {"L":[-1,0],
         "R":[1,0],
         "U":[0,1],
         "D":[0,-1]}
start = [0,0]
for move in s:
    start[0] += moves[move][0]
    start[1] += moves[move][1]
print(start[0], start[1])