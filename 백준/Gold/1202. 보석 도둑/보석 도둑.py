from heapq import heappush, heappop
from collections import deque
import sys
input = sys.stdin.readline


N, K = map(int, input().split())
gems = [tuple(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]


gems = deque(sorted(gems))
# w 오름차순 1순위, v 정렬은 중요하지 않음
bags.sort()
# 크기 오름차순
max_heap = []
# bag = x일 때, x 이하의 크기를 지닌 가방이
# 가질 수 있는 value들.
# 계속해서 누적됨.


ans = 0
for bag in bags:
    # 작은 가방이
    while gems and gems[0][0] <= bag:
        # 보석의 무게보다 크다면
        w, v = gems.popleft()
        heappush(max_heap, -v)
        # max_heap에 v를 넣는다.
    if max_heap:
        ans += -heappop(max_heap)
        # 그 후 가장 큰 v를 ans에 더한다.
# 시간복잡도 O(N+KlogK)
# 누적이라서 O(N*K)가 아님
# 최대값도 새로 뽑는 게 아니라 누적해서 할 수 있도록 heap


print(ans)
