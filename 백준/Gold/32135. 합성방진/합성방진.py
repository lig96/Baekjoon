# 특정 순열에서
# 좌우로 이웃한 두 수의 합이 합성수이고
# 맨 오른쪽 끝과 맨 왼쪽 끝 두 수의 합이 합성수라면,
# 그 순열을 회전시켜서 이루어진 n*n 2차원 배열에서
# 가로나 세로 방향으로 이웃한 두 수의 합이 합성수이다.
#
# 그런 순열을 찾는 방법은 브루트포스가 있다.
#
# 또한 수학적인 방법도 있다.
# 홀수+홀수 = 짝수, 짝수+짝수 = 짝수인데
# 2를 제외한 모든 짝수는 합성수이다.
# (홀수1...홀수2)(짝수3...짝수4)로 하면 괄호 내부는 조건을 충족하고
# 홀수2+짝수3, 짝수4+홀수1이 합성수라면 괄호 외곽도 조건을 충족한다.
# 그 합성수는 홀수일 것이고 (9, 15, 21, ...)이 후보이다.
# 그러한 경우가 가능한 가장 작은 n은 3+6=9, 4+5=9로 6이다.
#
# 6<=n이라면 존재하고 아니라면 존재하지 않는다.
# 문제 출제자는 가능한 쌍을 쉽게 찿을 수 있게끔
# n의 범위를 [8, 500]으로 했다고 한다.


from collections import deque
import sys
input = sys.stdin.readline
sys_print = sys.stdout.write


N = int(input())


permu = deque()
permu.append(3)
for i in range(1, N+1):
    if i % 2 == 1 and i != 3 and i != 5:
        permu.append(i)
permu.append(5)
permu.append(4)
for i in range(1, N+1):
    if i % 2 == 0 and i != 6 and i != 4:
        permu.append(i)
permu.append(6)
# 3(...)54(...)6


for _ in range(N):
    sys_print(' '.join(map(str, permu))+'\n')
    permu.rotate(1)
