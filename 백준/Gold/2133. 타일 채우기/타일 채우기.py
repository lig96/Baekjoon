# dp 문제를 풀 때는 배열 선언을 넉넉하게 해주자.
# 선언을 N+1까지만 했는데 대입을 dp[3]까지 하면
# IndexError가 난다.

# dp[N]은 N//2개의 인덱스에 접근해야 하는데
# 점화식을 dp[N] = dp[N-2]*4 - dp[N-4]로 축약하면
# 2개의 인덱스에만 접근해도 된다.


def sol(N):
    if dp[N] != 0:
        return dp[N]

    if N % 2 == 1:
        return 0
    else:
        ans = 0
        for i in range(2, N+1, 2):
            ans += sol(N-i) * (3 if i == 2 else 2)
        dp[N] = ans
        # dp[N] = (ans := sol(N-2)*4 - sol(N-4))
        return dp[N]


N = int(input())


dp = [0 for _ in range(N+1)]
dp[0] = 1  # '없다'라는 1가지 방법으로 생각하면 점화식이 깔끔해짐


print(sol(N))
