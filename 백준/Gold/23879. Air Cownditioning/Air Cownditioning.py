# 풀이: https://readble-ko.tistory.com/154


import sys
input = sys.stdin.readline


N = int(input())
p = list(map(int, input().split()))  # prefer
t = list(map(int, input().split()))  # time_now


d = [0] + [p[i] - t[i] for i in range(N)] + [0]
dd = [d[i+1] - d[i] for i in range(N+1)]
ans = sum(map(abs, dd)) // 2


print(ans)
