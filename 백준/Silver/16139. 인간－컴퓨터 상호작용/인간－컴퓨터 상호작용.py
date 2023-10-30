import sys
input = sys.stdin.readline
print = sys.stdout.write


def sol(ai, start, end):
    ai = ord(ai)-97
    a = dp[end][ai]
    if start > 0:
        b = dp[start-1][ai]
    else:
        b = 0
    return a-b


S = input().rstrip()
dp = [[] for _ in range(len(S))]
# dp[end][char] = 0 이상 end 이하의 누적합
temp = [0 for _ in range(26)]
for i, v in enumerate(S):
    v = ord(v)-97  # a-z, 0-25
    temp[v] += 1
    dp[i] = temp[:]

q = int(input())
for _ in range(q):
    ai, start, end = input().split()
    start, end = int(start), int(end)

    ans = sol(ai, start, end)

    print(str(ans)+'\n')
