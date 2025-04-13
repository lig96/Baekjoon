import sys
input = sys.stdin.readline
sys_print = sys.stdout.write


N = int(input())
arr = []
for _ in range(N):
    a, b, c, d = input().split()
    b, c, d = list(map(int, [b, c, d]))
    arr.append((a, b, c, d))


arr.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))


sys_print('\n'.join(x[0] for x in arr))
