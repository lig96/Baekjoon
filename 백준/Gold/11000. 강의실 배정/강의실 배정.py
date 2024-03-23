from heapq import heappush, heappop
import sys
input = sys.stdin.readline


N = int(input())
lectures = [tuple(map(int, input().split())) for _ in range(N)]


lectures.sort(key=lambda x: x[0])  # x[1]은 상관없음
times = []  # 현재 교실에서 진행중인 수업의 끝나는 시간들
heappush(times, -1)  # 교실 1개는 무조건 있음


for s, e in lectures:
    if times[0] <= s:
        # 가장 빨리 끝나는 교실의 수업 시간 <= s 라면
        # 그 교실의 끝나는 시간을 e로 변경(=increase_key)
        heappop(times)
        heappush(times, e)
    else:
        # 가장 빨리 끝나는 교실도 못 쓴다면
        # 새로운 교실을 추가
        heappush(times, e)


print(len(times))
