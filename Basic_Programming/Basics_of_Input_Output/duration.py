# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/duration/

n = int(input())
for _ in range(n):
    sh, sm, eh, em = map(int, input().split())
    duration_m = 60-sm+em
    duration_h = (eh-sh)-1 + int(duration_m/60)
    duration_m = duration_m%60
    print("{} {}".format(duration_h, duration_m))