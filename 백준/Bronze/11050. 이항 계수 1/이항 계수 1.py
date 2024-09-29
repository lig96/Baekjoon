import sys
input = sys.stdin.readline


N, K = map(int, input().split())


numerator = 1
for i in range(K):
    numerator *= (N-i)
denominator = 1
for i in range(K):
    denominator *= (i+1)


print(numerator//denominator)
