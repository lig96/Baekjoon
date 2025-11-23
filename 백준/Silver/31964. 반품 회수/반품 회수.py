import sys
input = sys.stdin.readline


N = int(input())
houses = list(map(int, input().split()))
times = list(map(int, input().split()))


houses.insert(0, 0)
times.insert(0, -float('inf'))
# 택배 회사로 돌아와야 하기 때문에
# 가상의 집을 만들어 준다.


tot_time = 0
now_pos = 0
tot_time += houses[-1]
now_pos = houses[-1]
# 아무 것도 회수하지 않고 맨 오른쪽 집으로 이동한다.
# 그 후 오른쪽에서 왼쪽으로 이동하며 회수를 진행한다.
for _ in range(len(houses)):
    tot_time += now_pos - houses[-1]
    now_pos = houses[-1]
    houses.pop()
    # 현재 위치에서 그 다음 집으로 이동한다.

    if times[-1] > tot_time:
        tot_time += (times[-1] - tot_time)
        # 가장 먼저 마주치는 집은 무조건 회수를 해야 하니
        # 기다렸다가 회수한다.
    times.pop()


print(tot_time)
