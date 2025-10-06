# 풀이 1: dp
# dp[i][n] = i를 오른쪽 끝으로 사용하는 합이 n인
# 윈도우의 개수.
# 메모리 초과와 시간 초과 때문에 2차원 list 대신 1차원 deque로 선언하면 된다.
#
# 풀이 2: 누적합
# "sum(arr[l:r]) % M == 0"
# = "(psum[r] - psum[l]) % M == 0"
# = "psum[r] % M == psum[l] % M"
# psum을 순회하며 이미 있는 cnt만큼 ans에 더해준다.


import sys
input = sys.stdin.readline


N, M = map(int, input().split())
arr = list(map(int, input().split()))


psum = [0]
for v in arr:
    psum.append((psum[-1]+v) % M)
# psum[i] = sum(arr[0:i])
# psum[0] = sum(공집합) = 0
# sum(arr[l..r]) = psum[r+1] - psum[l]


ans = 0
cnt = [0 for _ in range(M)]
for v in psum:  # psum[0]을 포함해야 한다.
    ans += cnt[v]
    cnt[v] += 1
# for문이 끝난 뒤 길이 M짜리 cnt 배열을 돌며
# ans += vC2를 해도 된다.
# 1+2+3.... = (n+1) * n / 2 = nC2이기 때문이다.


sys.stdout.write(str(ans))
