##  https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/split-house-547be0e9/description/

n = int(input())
grid = input()
if "HH" in grid:
    print("NO")
else:
    print("YES")
    print(grid.replace(".","B"))
