from collections import deque
import sys
input = sys.stdin.readline


N, Q, k = map(int, input().split())
operations = [list(map(int, input().split())) for _ in range(Q)]


left = deque()
right = deque()
mid = deque()
# mid scheduler는 실제로 정렬되진 않았지만 정렬되었다 가정하고 추가하다가
# 맨 마지막에 정렬해준다.
is_forward_direction = True
# True: 자료 구조의 오른쪽이 맨 앞,
# False: 자료 구조의 왼쪽이 맨 앞
sort_direction = True


for operation in operations:
    match operation:
        case [0, p]:
            if is_forward_direction:
                right.append(p)
            else:
                left.appendleft(p)
        case [1]:
            mid += left + right
            left.clear()
            right.clear()
            sort_direction = is_forward_direction
        case [2]:
            is_forward_direction = not is_forward_direction
else:
    mid = deque(sorted(mid, reverse=sort_direction))
    ans = left+mid+right
    # left.clear()
    # mid.clear()
    # right.clear()


if is_forward_direction:
    print(ans[-k])
else:
    print(ans[k-1])
# 1<=k<='0번 명령의 등장 횟수'