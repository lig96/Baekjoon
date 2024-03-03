# 풀이 1
# 동순위 처리 방식이 약간 특이한 dfs
# 깊이 우선이되, 자식 노드가 왼쪽부터 pop되게끔
# 뒤집어서 append 해줘야 한다.
# 재귀 방식으로 dfs를 구현하면
# 메모리 초과 혹은 시간 초과가 나는 듯하다.

# 풀이 2
# 연결 리스트


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
    print(schools[i])  # 초기값은 맨 마지막의 i
    i = nxt[i]
