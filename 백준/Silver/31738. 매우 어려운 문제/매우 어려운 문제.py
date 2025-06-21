N, M = map(int, input().split())


if N >= M:
    # 무조건 나눠떨어진다.
    ans = 0
else:
    ans = 1  # 곱셈의 항등원
    for i in range(1, N+1):
        ans = (ans*i) % M
        # i%M=i이기 때문에 i%m 대신 i만 써줘도 된다.
        if ans == 0:
            break


print(ans)
