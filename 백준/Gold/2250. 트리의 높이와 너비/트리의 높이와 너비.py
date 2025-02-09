# "임의의 노드의 왼쪽 부트리에 있는 노드들은 해당 노드보다 왼쪽의
# 열에 위치하고, 오른쪽 부트리에 있는 노드들은 해당 노드보다
# 오른쪽의 열에 위치한다."는 글자 그대로 중위 순회를 의미한다.
# 따라서 중위 순회를 통해 방문된 순서가 곧 열 좌표이다.
#
# 루트 노드는 부모 노드로서는 나타났으면서 자식 노드로서는 안
# 나타난 노드이다. 이를 알아내기 위해 그래프 순회를 할 필요는 없다.


from collections import defaultdict
import sys
input = sys.stdin.readline


def inorder(x, lv):
    if x == -1:
        return

    global turn

    inorder(nodes[x]['left'], lv+1)
    depth[lv] = [min(depth[lv][0], turn),
                 max(depth[lv][1], turn)]
    turn += 1
    inorder(nodes[x]['right'], lv+1)
    return


N = int(input())
nodes = {par: {'left': l, 'right': r} for par, l, r
         in (map(int, input().split()) for _ in range(N))}


# 루트 = 부모 노드 - 자식 노드 = summation 1..N - 자식 노드
root = (N * (N+1) // 2) - \
    sum(x for dic in nodes.values() for x in dic.values() if x != -1)
# depth[d] = [d 깊이의 노드 중 가장 왼쪽 좌표, d 깊이의 노드 중 가장 오른쪽 좌표]
depth = defaultdict(lambda: [float('inf'), -float('inf')])
# turn = 특정한 노드가 순회된 순서
turn = 1


inorder(x=root, lv=1)


ans = {'ind': float('inf'), 'width': -float('inf')}
for k, v in sorted(depth.items(), key=lambda x: x[0]):
    temp = v[1]-v[0]+1
    if temp > ans['width']:
        ans['ind'] = k
        ans['width'] = temp
print(ans['ind'], ans['width'])
