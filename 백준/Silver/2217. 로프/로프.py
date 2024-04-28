import sys
input = sys.stdin.readline


N = int(input())
ropes = [int(input()) for _ in range(N)]


ropes.sort(reverse=True)
# 내림차순 정렬


ans = -float('inf')
for i, v in enumerate(ropes):
    # 0번째 로프부터 i번째 로프까지 사용했을 때
    # 가장 약한 로프의 허용 중량은 v이고
    # 걸리는 하중은 w/(i+1)이다.
    # v >= w/(i+1)
    # v*(i+1) >= w
    temp = v*(i+1)
    ans = max(ans, temp)


print(ans)
