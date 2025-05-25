# 1. LCS.
# dp[n][m] = max(dp[n-1][m-1][0:i]+[A_arr[n]]
# for i in range(len(dp[n-1][m-1])+1))
# 이 한 줄만 바꿔주면 된다.
# LCS와 달리 끝에 하나 붙이는 게 최적이 아닐 수도 있기 때문에
# 마지막 len-i개를 버리고 붙이는 것을 고려해야 한다.
#
# 2. 그리디
# 한 CS가 A의 가장 큰 원소를 첫 원소로 갖는다면,
# 그 CS는 A의 다른 원소를 첫 원소로 갖는 모든 CS보다 크다.
# A의 i번째로 큰 원소가 B에 속한지를 확인하여 CS의 j번째 원소를 찾은 뒤
# i를 늘려가며 j번째 원소를 찾으면 된다.
# 이 과정에서 A와 B의 가용 범위는 줄어든다.


import sys
input = sys.stdin.readline
sys_print = sys.stdout.write


def sol_LCS(N, A_arr, M, B_arr) -> list[int]:
    def outcome(arr: list[int], x: int) -> list[int]:
        # arr = [a, b], x = x라면
        # [a, b, x], [a, x], [x]가 가능하고
        # 이 중에서 최댓값을 리턴한다.
        #
        # max(arr[:i]+[x] for i in range(len(arr)+1))도
        # 가능하지만 다소 비효율적이다. O(L)인 것은 동일하다.
        #
        # arr는 약단조감소이고 최대값을 찾는 것이니
        # max(모든 경우의 수)를 하지 않고
        # v와의 비교를 통해 x가 들어갈 위치를 찾을 수 있다. 이분탐색으로도 가능하다.
        temp = []
        for v in arr:
            if v < x:
                break
            else:
                temp.append(v)
        return temp+[x]
    A_arr, B_arr = [None]+A_arr, [None]+B_arr
    # dp와 arr를 순회하는 과정에서 인덱싱 여유를 만듦
    dp = [[None for _ in range(M+1)] for _ in range(N+1)]
    # dp[n][m] = A_arr[:n+1]과 B_arr[:m+1]을 썼을 때 최대 공통 부분 수열

    for n in range(N+1):
        for m in range(M+1):
            if n == 0 or m == 0:
                dp[n][m] = []
            else:
                if A_arr[n] == B_arr[m]:
                    dp[n][m] = outcome(dp[n-1][m-1], A_arr[n])
                    # dp[n][m] = max(dp[n-1][m-1][0:i]+[A_arr[n]]
                    #                for i in range(len(dp[n-1][m-1])+1))
                else:
                    dp[n][m] = max(dp[n-1][m],
                                   dp[n][m-1])
    return max(map(max, dp))


def sol_greedy(N, A_arr, M, B_arr) -> list[int]:
    A_start, B_start = 0, 0
    ans = []
    while A_start < N and B_start < M:
        sorted_A = sorted(A_arr[A_start:], reverse=True)  # 내림차순
        for v in sorted_A:
            if v in B_arr[B_start:]:
                B_i = B_arr[B_start:].index(v) + B_start
                # 일치하는 첫 원소의 원래 배열에서의 위치
                B_start = B_i+1
                ans.append(v)
                break
        A_start += A_arr[A_start:].index(v)+1
    return ans


N = int(input())
A_arr = list(map(int, input().split()))
M = int(input())
B_arr = list(map(int, input().split()))


# ans = sol_LCS(N, A_arr, M, B_arr)
ans = sol_greedy(N, A_arr, M, B_arr)


print(len(ans))
if len(ans) != 0:
    print(*ans)
