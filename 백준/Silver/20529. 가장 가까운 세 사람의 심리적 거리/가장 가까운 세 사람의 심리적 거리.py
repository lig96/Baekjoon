from itertools import combinations
from collections import Counter
import sys
input = sys.stdin.readline


def calc(a, b, c):
    ans = 0
    for i in range(4):
        if a[i] != b[i]:
            ans += 1
        if c[i] != b[i]:
            ans += 1
        if a[i] != c[i]:
            ans += 1
    return ans


T = int(input())
for _ in range(T):
    N = int(input())
    arr = input().split()
    answers = []

    total = Counter()
    total.update(arr)
    if max(total.values()) >= 3:
        print(0)
        continue
    total = list(total.elements())

    # for a in range(0, len(total)):
    #     for b in range(a+1, len(total)):
    #         for c in range(b+1, len(total)):
    #             ans = calc(total[a], total[b], total[c])
    #             answers.append(ans)
    # print(min(answers))

    for combs in combinations(total, 3):
        ans = calc(*combs)
        answers.append(ans)
    print(min(answers))
