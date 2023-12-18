# 전깃줄을 가장 덜 줄인다는 것은
# 전깃줄을 가장 많이 살린다는 것과 동일하다.
# 전깃줄을 왼쪽 전봇대를 기준으로 정렬할 경우
# 오른쪽 전봇대의 도착 위치만 신경쓰면 된다.
# 오른쪽 전봇대의 도착 위치가 증가하도록(=꼬이지 않도록)
# 선택한 요소들의 최장 길이= LIS이다.


def make_dp():
    dp = [1 for _ in range(N)]
    # dp[i] = i번째 요소를 사용했을 때 lis의 길이

    for now in range(1, N):
        for prev in range(0, now):
            if arr[prev] < arr[now]:
                dp[now] = max(dp[now], dp[prev]+1)

    return dp


N = int(input())
arr = sorted([list(map(int, input().split())) for _ in range(N)])
arr = [x[1] for x in arr]


dp = make_dp()


print(N-max(dp))
