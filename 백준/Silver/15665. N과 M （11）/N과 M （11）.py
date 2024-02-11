import sys
input = sys.stdin.readline
print = sys.stdout.write


def dfs(sequence):
    if len(sequence) == M:
        print(' '.join(map(str, sequence))+'\n')
        return

    for i in range(0, N):
        sequence.append(numbers[i])
        dfs(sequence)
        sequence.pop()
    return


N, M = map(int, input().split())
numbers = map(int, input().split())


numbers = sorted(set(numbers))
N = len(numbers)


dfs([])
