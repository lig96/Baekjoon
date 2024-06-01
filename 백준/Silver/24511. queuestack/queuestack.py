from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))


queue_union = deque()
for i in range(N):
    if A[i] == 0:
        queue_union.appendleft(B[i])


ans = []
for i in range(M):
    queue_union.append(C[i])
    temp = queue_union.popleft()
    ans.append(temp)


print(' '.join(map(str, ans)))
