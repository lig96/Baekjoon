import sys
input = sys.stdin.readline


N = int(input())
temp = list(map(int, input().split()))
a, b, c = temp[:]
d, e, f = temp[:]
for _ in range(1, N):
    x, y, z = list(map(int, input().split()))
    a, b, c = x+max(a, b), y+max(a, b, c), z+max(b, c)
    d, e, f = x+min(d, e), y+min(d, e, f), z+min(e, f)


print(max(a, b, c), min(d, e, f))