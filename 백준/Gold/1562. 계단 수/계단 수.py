N = int(input())
MOD = 1_000_000_000


dp_old = [[0 for _ in range(1 << 10)] for _ in range(10)]
dp_new = [[0 for _ in range(1 << 10)] for _ in range(10)]
# dp[맨왼쪽숫자][비트마스크로 표현된 0~9 포함 여부]
for i in range(10):
    dp_old[i][1 << i] += 1
# N == 1일 때 초기값


# N == 1이라면 반복문 들어가지 않고 바로 출력
# 새로운 숫자 j를 맨 왼쪽에 붙임
for i in range(N-1):
    for j in range(10):
        if j == 0:
            for bitmask in range(1 << 10):
                dp_new[0][bitmask | 1 << 0] += dp_old[1][bitmask] % MOD
        elif j == 9:
            for bitmask in range(1 << 10):
                dp_new[9][bitmask | 1 << 9] += dp_old[8][bitmask] % MOD
        else:
            for bitmask in range(1 << 10):
                dp_new[j][bitmask | 1 << j] += dp_old[j-1][bitmask] % MOD
                dp_new[j][bitmask | 1 << j] += dp_old[j+1][bitmask] % MOD
    dp_old = dp_new
    dp_new = [[0 for _ in range(1 << 10)] for _ in range(10)]


print(sum(dp_old[i][(1 << 10)-1] for i in range(1, 10)) % MOD)
# (1 << 10)-1
# int('0b1_111_111_111', 2)
