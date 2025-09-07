# 강단조함수의 형태를 구현해야 한다.
# 이 조건에 맞지 않아
# 원소가 dist에 추가되지 않는다면 그만큼 그 원소의 child도
# 연산을 하지 않아 소요 시간이 줄어든다.
# 이때 이를 위해 다소 비효율적인 O(N)을 해도 된다.
# 8000ms 초과 -> 4000ms
#
# 정답을 출력할 때 마지막 인덱스를 조금씩 줄여나가는 것이 중요하다.
# 어떤 세금의 인덱스 k에 대하여 정답이 되는 인덱스가 i라면
# j > i에 대해서 이미 v_j+세금*j > v_i+세금*i인데
# 세금은 증가함수이니 앞으로도 해당 부등식은 성립하기 때문이다.
# 이를 통해 O(KN) 반복문의 시간 복잡도를 줄일 수 있다.
# 4000ms -> 200ms


from heapq import heappush, heappop
import sys
input = sys.stdin.readline


def dijk(S):
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
        for child, cost in graph[now]:
            temp = now_d + cost
            temp_l = length+1
            if temp < dist[child][temp_l]:
                if any(v <= temp for v in dist[child][:temp_l]):
                    # v <= temp가 하나라도 있다면 해당 temp는 무의미하다.
                    # 사용한 도로의 수도 많은데 비용도 많다는 뜻이기 때문이다.
                    # 이로써 강단조함수를 만들 수 있다.
                    # 이 조건문의 위치는 소요 시간과 전혀 상관이 없었다.
                    continue
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


INF = float('inf')
presum_taxes = [0]
for v in taxes:
    presum_taxes.append(presum_taxes[-1]+v)
# 세금 인상은 누적으로 적용된다.


dist_S_D: list[int] = dijk(S)[D]
# dist_S_D[i] = v,
# S에서 D까지 i개의 도로를 사용했을 때 최단 거리는 v이다.


last = len(dist_S_D)-1  # 마지막으로 가능한 인덱스
for tax in presum_taxes:
    ans = INF  # min의 항등원
    for i in range(last+1):  # 마지막으로 가능한 인덱스를 포함
        v = dist_S_D[i]
        temp = v+i*tax
        if temp < ans:
            ans = temp
            last = i  # 마지막으로 가능한 인덱스
    print(ans)
# # 하단과 기본적으로 동일하다.
# for tax in presum_taxes:
#     temp = (v+i*tax for i, v in enumerate(dist_S_D))
#     print(min(temp))
