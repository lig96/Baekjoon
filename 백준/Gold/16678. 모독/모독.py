import sys
input = sys.stdin.readline


N = int(input())
arr = [int(input()) for _ in range(N)]


ans, defile = 0, 1
for v in sorted(arr):
    if (v-defile) > 0:
        ans += (v-defile)
        defile += 1
    elif (v-defile) == 0:
        defile += 1
    elif (v-defile) < 0:
        pass
    else:
        raise Exception


print(ans)
