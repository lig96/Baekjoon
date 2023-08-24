def dfs(start, ans):
    if len(ans) == M:
        print(' '.join(map(str, ans))+'\n')
        return
    for i in range(0, N):
        if not arr[i] in ans:
            dfs(i+1, ans+[arr[i]])

import sys
print = sys.stdout.write
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

dfs(0, [])