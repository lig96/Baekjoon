# https://yabmoons.tistory.com/592


def make_P():
    # inclusive start, end
    # start=1, end=3이면
    # S[1], S[2], S[3]이 팰린드롬이냐 아니냐

    dp = [[False for end in range(N)] for start in range(N)]
    for i in range(N):
        dp[i][i] = True
    for width in range(1, 2):
        for i in range(0, N-width):
            dp[i][i+width] = (S[i] == S[i+width])
    for width in range(2, N):
        for i in range(0, N-width):
            dp[i][i+width] = (S[i] == S[i+width]) and (dp[i+1][i+width-1])
    return dp


def make_F():
    # dp[i] = S[0], ~~~, S[i]를 사용했을 때
    # 최소 팰린드롬 분할의 개수

    dp = [float('inf') for i in range(N)]
    dp[0] = 1
    for end in range(1, N):
        if P[0][end]:
            # start-1이 음수일 때 예외 처리
            dp[end] = 1
        else:
            for start in range(1, end):
                if P[start][end]:
                    dp[end] = min(dp[end], dp[start-1]+1)
            else:
                dp[end] = min(dp[end], dp[end-1]+1)
                # 팰린드롬이 없더라도 이전 값에 그대로 +1 가능
    return dp


S = input().rstrip()


N = len(S)
P = make_P()


F = make_F()


print(F[-1])
