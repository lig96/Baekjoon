import sys
print = sys.stdout.write


def dfs(ans, start):
    if len(ans) == 6:
        print(' '.join(map(str, ans))+'\n')
        return

    for i in range(start, k):
        ans.append(numbers[i])
        dfs(ans, i+1)
        ans.pop()
    return


for line in sys.stdin.readlines():
    line = line.rstrip()
    if line == '0':
        break

    k, *numbers = map(int, line.split())

    dfs([], 0)
    print('\n')
