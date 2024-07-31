import sys
input = sys.stdin.readline


def sol(N, K):
    cnt = 0
    nums = [True for _ in range(0, N+1)]
    for i in range(2, N+1):
        if nums[i]:
            for nxt in range(i, N+1, i):
                if nums[nxt]:
                    nums[nxt] = False
                    cnt += 1
                    if cnt == K:
                        ret = nxt
    return ret


N, K = map(int, input().split())


ans = sol(N, K)


print(ans)
