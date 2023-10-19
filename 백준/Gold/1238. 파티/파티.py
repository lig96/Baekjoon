# dist_arr을 고정좌표 출발 - i 도착의 거리가 아니라
# i 출발 - 고정좌표 도착의 거리 배열로 만드는 발상이 어렵다.
# 다익스트라 연산 2번만에 해결 가능.
# https://chb2005.tistory.com/128 의 그림 참고.


from heapq import heappush, heappop
import sys
input = sys.stdin.readline


def dijk(i, graph_i):
    dist_arr = [int(1e9) for _ in range(N+1)]
    dist_arr[i] = 0
    heap = []
    heappush(heap, (0, i))
    if graph_i == 'startX':
        graph = graph_startX_endi
    elif graph_i == 'starti':
        graph = graph_starti_endX

    while heap:
        now_dist, now = heappop(heap)
        if now_dist > dist_arr[now]:
            continue
        for end in graph[now]:
            end, end_dist = end
            temp = now_dist + end_dist
            if temp < dist_arr[end]:
                dist_arr[end] = temp
                heappush(heap, (dist_arr[end], end))
    return dist_arr


N, M, X = map(int, input().split())
graph_startX_endi = [[] for _ in range(N+1)]
graph_starti_endX = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, T = map(int, input().split())
    graph_startX_endi[start].append((end, T))
    graph_starti_endX[end].append((start, T))


arr_startX_endi = dijk(X, 'startX')
arr_starti_endX = dijk(X, 'starti')
# arr_starti_endX[3] 는 3에서 출발해서 X로 도착하는 거리.
# 일반적인 dist_arr와 반대.

ans_arr = [arr_starti_endX[i]+arr_startX_endi[i] for i in range(1, N+1)]
print(max(ans_arr))