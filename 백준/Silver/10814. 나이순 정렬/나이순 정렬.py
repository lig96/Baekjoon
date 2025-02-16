import sys
input = sys.stdin.readline
sys_print = sys.stdout.write


N = int(input())
arr = [list(map(lambda x: int(x) if x.isdecimal() else x, input().rstrip().split()))
       for _ in range(N)]


arr.sort(key=lambda x: (x[0]))
# 안정 정렬


sys_print('\n'.join(map(lambda x: ' '.join(map(str, x)), arr)))
