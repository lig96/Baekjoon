# 냅색 문제와 비슷하지만 중복을 허락하기 때문에
# 3중 반복문(사용할 동전, 가치의 합, 사용할 동전의 배수)을
# 돌려야 한다는 차이점이 있다.
# 빡센 시간 제한에 걸리지 않기 위해 2중 반복문으로
# 점화식을 바꿔야 하는데 이게 어렵다.
# 메모리 제한도 빡세기 때문에(파이썬 기준 상관 없는 듯)
# dp 역시 바꿔야 하는데 이게 합쳐지면
# 점화식을 알아내는 게 더 어려워진다.


import sys
input = sys.stdin.readline


n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]


dp = [0 for _ in range(k+1)]
dp[0] = 1


for coin in coins:
    for tot in range(coin, k+1):
        dp[tot] = dp[tot-coin] + dp[tot]
        # 1차원 배열 1개에서 냅색을 풀 때는
        # 과거 용도로 쓰는 값을 변경하지 않기 위해
        # 거꾸로 순회해야 하지만
        # 일부러 정방향으로 순회하며
        # 과거의 여러 배수들을 현재의 값 1개로 변경 후
        # 1개만 인덱싱을 통해 접근한다.


sys.stdout.write(str(dp[-1]))
