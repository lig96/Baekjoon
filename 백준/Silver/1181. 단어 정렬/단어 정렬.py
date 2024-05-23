import sys
input = sys.stdin.readline
print = sys.stdout.write


N = int(input())
words = [input().rstrip() for _ in range(N)]


words = sorted(set(words), key=lambda x: (len(x), x))


print('\n'.join(words))
