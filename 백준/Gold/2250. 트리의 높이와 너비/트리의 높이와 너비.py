import sys
input = sys.stdin.readline


def rec(i):
    if width[i] is not None:
        return sum(width[i].values())
    temp = {}
    temp['self'] = 1
    temp['left'] = 0 if nodes[i]['left'] == -1 else rec(nodes[i]['left'])
    temp['right'] = 0 if nodes[i]['right'] == -1 else rec(nodes[i]['right'])
    width[i] = temp
    return sum(width[i].values())


def dfs(startx):
    stack = [(startx, 1)]
    while stack:
        now, lv = stack.pop()
        for lr_char in ['left', 'right']:
            child = nodes[now][lr_char]
            if child == -1:
                continue
            stack.append((child, lv+1))
            loc[child] = (loc[now] +
                          (-1 if lr_char == 'left' else 1) *
                          (sum(width[child].values()) - width[child][lr_char])
                          )
            depth[lv+1] = [min(depth[lv+1][0], loc[child]),
                           max(depth[lv+1][1], loc[child])]
    return


N = int(input())
nodes = dict()
for _ in range(N):
    parent, left, right = map(int, input().split())
    nodes[parent] = {'left': left, 'right': right}


# 루트 = summation 1..N - 자식 노드
root = (N * (N+1) // 2) - \
    sum(x for dic in nodes.values() for x in dic.values() if x != -1)


# width[i] = 노드 i를 루트로 하는 트리 전체의 너비
width = [None for _ in range(N+1)]
rec(root)  # width 배열 채우기
# depth[d] = [d 깊이의 노드 중 가장 왼쪽 좌표, d 깊이의 노드 중 가장 오른쪽 좌표]
depth = [[float('inf'), -float('inf')] for _ in range(N+1)]
depth[0] = None  # 없는 인덱스
depth[1] = [0, 0]  # 깊이 1은 [0, 0]으로 고정
# loc[i] = 노드 i의 위치
loc = [None for _ in range(N+1)]
loc[root] = 0  # 루트 노드는 0으로 고정
dfs(root)  # depth와 loc 배열 채우기


ans = {'ind': float('inf'), 'width': -float('inf')}
for i, v in enumerate(depth):
    if v == None:
        continue
    temp = v[1]-v[0]+1
    if temp > ans['width']:
        ans['ind'] = i
        ans['width'] = temp
print(ans['ind'], ans['width'])
