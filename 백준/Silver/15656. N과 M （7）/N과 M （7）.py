import sys
input = sys.stdin.readline
print = sys.stdout.write


def dfs(ans):
    if len(ans) == M:
        print(' '.join(map(str, ans))+'\n')
        return

    for i in range(0, N):
        ans.append(numbers[i])
        dfs(ans)
        ans.pop()
    return


N, M = map(int, input().split())
numbers = list(map(int, input().split()))


numbers.sort()


dfs([])
