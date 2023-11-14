# l == r이면 안 된다는 규칙을 명시할 필요는 없다.
# l != r에서 l == r로 이동한다면 이미 비효율적이라 dp에서 걸러진다.
# 명시한다면 (l,r), (arr[d],r), (l,arr[d]) 모두 고려해야 한다. 


import sys
input = sys.stdin.readline


def f(x, y):
    # x는 움직이기 이전 위치, y는 움직인 이후 위치
    if x == y:
        return 1
    elif (x == 0) and (y != 0):
        return 2
    elif abs(x-y) == 2:
        return 4
    else:
        return 3


arr = list(map(int, input().split()))
arr.pop()
N = len(arr)


dp = [[[4*N for _ in range(N)] for _ in range(5)] for _ in range(5)]
# dp[left][right][depth] = depth번째 발판을 밟은 후 가장 낮은 힘


dp[arr[0]][0][0] = f(0, arr[0])
dp[0][arr[0]][0] = f(0, arr[0])
# d = 0 초기값
for d in range(1, len(arr)):
    for l in range(5):
        for r in range(5):
            if dp[arr[d]][r][d] > dp[l][r][d-1] + f(l, arr[d]):
                dp[arr[d]][r][d] = dp[l][r][d-1] + f(l, arr[d])
            # l, r 25가지 중 r을 고정하고 l->arr[d]로 움직임

            if dp[l][arr[d]][d] > dp[l][r][d-1] + f(r, arr[d]):
                dp[l][arr[d]][d] = dp[l][r][d-1] + f(r, arr[d])
            # l, r 25가지 중 l을 고정하고 r->arr[d]로 움직임
# detph = 1 ~ len(arr) 풀이


print(min([dp[l][r][-1] for l in range(5) for r in range(5)]))
