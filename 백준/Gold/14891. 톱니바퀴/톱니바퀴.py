# 한쪽 방향의 톱니바퀴가 회전 가능한지 여부는
# 지금처럼 반복문으로도 구현할 수 있고
# 재귀문으로도 구현할 수 있다.


from collections import deque
import sys
input = sys.stdin.readline


def find_right(wheel_ind):
    return wheels[wheel_ind][2]


def find_left(wheel_ind):
    return wheels[wheel_ind][-2]


wheels = [deque(map(int, input().rstrip())) for _ in range(4)]
K = int(input())
rotations = [list(map(int, input().split())) for _ in range(K)]


for ind, direction in rotations:
    ind -= 1  # 제로 인덱스

    can_rotate = [0 for _ in range(4)]
    can_rotate[ind] = direction

    for i in range(ind+1, 4):
        # 오른쪽 톱니바퀴가 회전 가능한지
        if find_right(i-1) != find_left(i):
            can_rotate[i] = -1 * can_rotate[i-1]
        else:
            break
    for i in range(0, ind)[::-1]:
        # 왼쪽 톱니바퀴가 회전 가능한지
        # range를 거꾸로 순회해야 함
        if find_right(i) != find_left(i+1):
            can_rotate[i] = -1 * can_rotate[i+1]
        else:
            break

    for i, v in enumerate(can_rotate):
        wheels[i].rotate(v)


ans = 0
for i in range(4):
    ans += wheels[i][0] * 2**i
print(ans)
