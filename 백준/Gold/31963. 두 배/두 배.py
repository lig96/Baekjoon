import sys
input = sys.stdin.readline


def sol(N, arr):
    d = [0 for _ in range(N)]
    # d[i] = n, such that arr[i]*2^n-1<arr[i-1]<=arr[i]*2^n
    # d[i]가 양수라면 arr[i]가 작은 경우
    # d[i]가 0이라면 arr[i]가 적당히 큰 경우
    # d[i]가 음수라면 arr[i]가 매우 큰 경우
    for i in range(1, N):
        if arr[i-1] > arr[i]:
            for n in range(1, 21):
                if arr[i-1] <= arr[i] << n:
                    break
            d[i] = n
        else:  # arr[i-1] <= arr[i]:
            for n in range(-1, -21, -1):
                if not (arr[i-1] <= arr[i] >> -n):
                    break
            d[i] = n+1

    ret = 0
    for i in range(1, N):
        ret += max(d[i], 0)  # 양수라면 곱한 셈 치고 더한다.
        if i == N-1:
            pass
        else:
            d[i+1] += max(d[i], 0)
            # 양수라면 곱한 셈이니,그 다음 수의 필요한 d를 높인다.
    return ret


N = int(input())
arr = list(map(int, input().split()))


ans = sol(N, arr)


print(ans)
