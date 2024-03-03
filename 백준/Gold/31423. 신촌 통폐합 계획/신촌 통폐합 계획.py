import sys
input = sys.stdin.readline
print = sys.stdout.write


N = int(input())
schools = [''] + [input().strip() for _ in range(N)]


nxt = [None for _ in range(N+1)]
tail = [i for i in range(N+1)]
for _ in range(N-1):
    i, j = map(int, input().split())

    nxt[tail[i]] = j
    tail[i] = tail[j]


for _ in range(N):
    print(schools[i])  # 맨 마지막의 i
    i = nxt[i]
