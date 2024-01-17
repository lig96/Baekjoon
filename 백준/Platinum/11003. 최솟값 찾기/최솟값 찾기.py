# 방법 1.
# heap
# (중요한 건 아니지만
# 힙의 길이는 L이면 충분하지만
# 큰 값이 힙 속에 남아있어서 L 초과일 수도 있음)
# 푸쉬-nlogn, 팝-nlogn, 출력-n
# O(nlogn)

# 방법 2.
# deque
# 강단조증가가 되도록 deque를 구성하면
# qu[0]은 언제나 최솟값임
# 슬라이딩윈도우 속에서
# 오른쪽이 오래 살아남으니 오른쪽이 작다면
# 왼쪽의 작은 것을 남길 필요가 없음
# (중요한 건 아니지만 길이는 L 이하
# 무조건 조건에 따라 걸러내긴 해야 함)
# 어팬드-n, 팝-n, 출력-n
# O(n)


from collections import deque
from heapq import heappush, heappop
import sys
input = sys.stdin.readline
print = sys.stdout.write


def sol_deque(A_arr, N, L):
    ans = []

    qu = deque()
    for i, A in enumerate(A_arr):
        # 강단조증가
        while qu and qu[-1][0] >= A:
            qu.pop()
        else:
            qu.append((A, i))

        # 조건 확인
        # 이게 매번 되기 때문에 while 안 해도 됨
        # append도 무조건 되니 qu도 안 해도 됨
        if not (i-L+1 <= qu[0][1]):
            qu.popleft()

        ans.append(qu[0][0])
    return ans


def sol_heap(A_arr, N, L):
    ans = []

    heap = []
    for i, A in enumerate(A_arr):
        heappush(heap, (A, i))
        while True:
            temp_A, temp_i = heappop(heap)
            if i-L+1 <= temp_i:
                ans.append(temp_A)
                heappush(heap, (temp_A, temp_i))
                break
    return ans


N, L = map(int, input().split())
A_arr = list(map(int, input().split()))


ans = sol_deque(A_arr, N, L)


print(' '.join(map(str, ans)))
