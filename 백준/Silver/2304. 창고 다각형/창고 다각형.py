import sys
input = sys.stdin.readline


N = int(input())
pillars = [0 for _ in range(1001)]
for _ in range(N):
    L, H = map(int, input().split())
    pillars[L] = H


max_i = pillars.index(max(pillars))


for i in range(0, max_i):
    if pillars[i] > pillars[i+1]:
        pillars[i+1] = pillars[i]
for i in range(max_i, len(pillars)-1)[::-1]:
    if pillars[i] < pillars[i+1]:
        pillars[i] = pillars[i+1]


print(sum(pillars))
