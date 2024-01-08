# 태그: 게임 이론

# Case 1:
# dist <= m
# 자명하게 정답은 First 1

# Case 2:
# dist > m
# 첫 플레이어가 할 수 있는 경우의 수는
# 1. new_dist = dist+smth
# 2. new_dist = dist
# 3. new_dist = dist-smth, such that new_dist > m
# 4. new_dist = dist-smth, such that new_dist <= m
# 4번을 하면 게임을 지게 되니 선택하지 않는다.
# 1, 2, 3번 중 하나를 선택한다면
# 그 다음 번 순서에서 두 번째 플레이어가
# without loss of generality, Case 2를 맞이하게 된다.
# 이렇게 두 플레이어는 Case 2를 무한하게 반복하게 된다.


import sys
input = sys.stdin.readline
print = sys.stdout.write


n = int(input())
for _ in range(n):
    m, xs, ys, xf, yf = map(int, input().split())

    dist = abs(xs-xf) + abs(ys-yf)
    if dist <= m:
        print('First 1'+'\n')
    else:
        print('Infinity'+'\n')
