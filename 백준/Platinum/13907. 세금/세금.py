'''
시간 확인용
https://www.acmicpc.net/source/88378309
'''

from heapq import heappush, heappop
import sys
input = sys.stdin.readline


def dijk(S):
    INF = float('inf')

    dist = [[INF for _ in range(N)] for _ in range(N+1)]
    heap = []

    dist[S][0] = 0
    heappush(heap, (0, 0, S))

    while heap:
        now_d, length, now = heappop(heap)
        if dist[now][length] < now_d:
            continue
        if (length+1) >= N:
            continue
        if any(v < now_d for v in dist[now][:length]):
            # v < now_d가 하나라도 있다면 해당 temp는 무의미하다.
            # 사용한 도로의 수도 많은데 비용도 많다는 뜻이기 때문이다.
            # 위치는 시간과 전혀 상관이 없었다.
            continue
        for child, cost in graph[now]:
            temp = now_d + cost
            temp_l = length+1
            if temp < dist[child][temp_l]:
                dist[child][temp_l] = temp
                heappush(heap, (temp, temp_l, child))

    return dist


N, M, K = map(int, input().split())
S, D = map(int, input().split())
# 원-인덱싱
graph = [[] for _ in range(N+1)]  # 원-인덱싱
for _ in range(M):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))
    # 양방향
taxes = [int(input()) for _ in range(K)]


# presum_taxes = [0]
# for v in taxes:
#     presum_taxes.append(presum_taxes[-1]+v)
# # 세금 인상은 누적으로 적용된다.


# dist_S_D: list[int] = dijk(S)[D]
# # dist_S_D[i] = v,
# # S에서 D까지 i개의 도로를 사용했을 때 최단 거리는 v이다.


# for tax in presum_taxes:
#     temp = (v+i*tax for i, v in enumerate(dist_S_D))
#     print(min(temp))

'''
시간 확인용
https://www.acmicpc.net/source/88378309
'''
distance = dijk(S)[D]


taxes = [0] + taxes
pay = 0
last_idx = N-1
for tax in taxes:
    pay += tax
    ans = float('inf')
    for idx in range(1, last_idx+1):
        cost = distance[idx] + idx*pay
        if ans > cost:
            ans = cost
            last_idx = idx
    print(ans)
