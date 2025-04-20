from heapq import heappush, heappop
import sys
input = sys.stdin.readline
sys_print = sys.stdout.write


def sol(n, m, t, s, g, h, roads, candidates, gh_index):
    _, used_roads = dijk(n, m, t, s, g, h, roads, candidates)
    ans_arr = [i for i in candidates if gh_index in used_roads[i]]
    return ans_arr


def dijk(n, m, t, s, g, h, roads, candidates):
    dists = [float('inf') for _ in range(n)]
    used_roads = [set() for _ in range(n)]
    heap = []

    dists[s] = 0
    heappush(heap, (dists[s], s))

    while heap:
        cost, x = heappop(heap)
        if dists[x] < cost:
            continue
        for nxt, dist, ind in roads[x]:
            if dists[nxt] > cost+dist:
                dists[nxt] = cost+dist
                heappush(heap, (dists[nxt], nxt))
                # 기존보다 더 좋은 경로를 발견했으므로
                # used_roads[nxt]를 초기화하고
                # 지금 사용한 ind 도로의 시작점이 x이니 used_roads[x]를 더하고
                # 지금 사용한 ind 도로를 더한다.
                used_roads[nxt] = set()
                used_roads[nxt] = used_roads[nxt].union(used_roads[x])
                used_roads[nxt].add(ind)
            elif dists[nxt] == cost+dist:
                # 동거리일 때도 방문하여 가능한 경로가 여러 개일 때
                # 전부 탐색할 수 있도록 한다.
                # 기존과 동일하게 좋은 경로를 발견했으므로
                # used_roads[nxt]를 초기화하지 않고
                # 지금 사용한 ind 도로의 시작점이 x이니 used_roads[x]를 더하고
                # 지금 사용한 ind 도로를 더한다.
                used_roads[nxt] = used_roads[nxt].union(used_roads[x])
                used_roads[nxt].add(ind)
    return dists, used_roads


for _ in range(T := int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(lambda x: int(x)-1, input().split())  # 제로 인덱싱
    roads = [[] for _ in range(n)]  # 인접 리스트
    gh_index = None
    for i in range(m):
        a, b, d = map(int, input().split())
        a, b = a-1, b-1  # 제로 인덱싱
        if (a, b) == (g, h) or (b, a) == (g, h):
            gh_index = i
        roads[a].append((b, d, i))
        roads[b].append((a, d, i))
        # 양방향이기 때문에 roads[start] = list[(end, distance, road index)]

    candidates = [int(input())-1 for _ in range(t)]  # 제로 인덱싱

    ans = sol(n, m, t, s, g, h, roads, candidates, gh_index)

    sys_print(' '.join(map(lambda x: str(x+1), sorted(ans)))+'\n')  # 제로 인덱싱 해제
