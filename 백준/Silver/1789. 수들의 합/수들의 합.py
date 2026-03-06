import sys
input = sys.stdin.readline


S = int(input())


tot = 0
for N in range(1, 93_000):
    tot += N
    if tot > S:
        break
N -= 1


print(N)
