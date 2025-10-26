# 1. 그리디&구현
# 2. 그리디&분할정복


import sys
input = sys.stdin.readline


def sol(N, tabs, correct_tabs):
    def sign(x):
        if x > 0:
            return 1
        elif x == 0:
            return 0
        else:
            return -1

    ans = 0
    need = [correct_tabs[i] - tabs[i] for i in range(N)]

    for i in range(N):
        while need[i] != 0:
            ans += 1
            sign_ = sign(need[i])
            for j in range(i, N):  # i 포함
                if sign(need[j]) != sign_:
                    break
                need[j] += (-1 if sign_ == 1 else + 1)
    return ans


N = int(input())
tabs = list(map(int, input().split()))
correct_tabs = list(map(int, input().split()))


print(sol(N, tabs, correct_tabs))
