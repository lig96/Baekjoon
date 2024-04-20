# Python 3와 동일한 코드 

# 선수 i가 선수 j를 이긴다.
# = 힘i + 링i*힘j > 힘j + 링j*힘i
# = 힘i(1-링j) > 힘j(1-링i)
# = (1-링j)/힘j > (1-링i)/힘i
# = xj > xi, 단 xi=(1-링i)/힘i
#
# 이제부터 '선수들의 힘은 수직선 상에 위치한 정수이다'로
# 문제를 변환할 수 있고
# 힘의 크기대로 정렬을 하면
# '선수들의 줄에서 자기보다 앞에 있는데 자기가 이긴 선수의 수'가 0이 되어
# 수여하는 금화의 수를 최소화할 수 있다.
# 왜냐하면 이 정렬에서는 자기보다 앞에 있다면 언제나 자기가 지기 때문이다.
#
# 한편 힘의 크기의 순위는 승수에 대해 강단조증가하기 때문에
# 자기보다 승수가 높은 선수에 대해 자기가 이기는 경우는 없다.
# 따라서 승수에 대해 정렬을 해도 된다.(ㄱ)
#
# 별 다른 증명 없이 (ㄱ)의 성질만을 이용하여
# 단순히 nC2 브루트포스로 구한 승수를 기준으로 정렬하는 풀이가
# 인터넷에는 많지만 이러한 풀이로는 정답임을 증명하지 못한다.


import sys
input = sys.stdin.readline
print = sys.stdout.write


N = int(input())
players = [(i+1,)+tuple(map(int, input().split())) for i in range(N)]


players.sort(key=lambda x: (1-x[2])/x[1])


print('\n'.join(map(lambda x: str(x[0]), players)))
