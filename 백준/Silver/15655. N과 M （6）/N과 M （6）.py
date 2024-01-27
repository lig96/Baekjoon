import sys
input = sys.stdin.readline
print = sys.stdout.write


def dfs(ans, start):
    if len(ans) == M:
        print(' '.join(map(str, ans))+'\n')
        return

    for i in range(start, N):
        ans.append(numbers[i])
        dfs(ans, i+1)
        ans.pop()
    return


N, M = map(int, input().split())
numbers = list(map(int, input().split()))


numbers.sort()


dfs([], 0)
