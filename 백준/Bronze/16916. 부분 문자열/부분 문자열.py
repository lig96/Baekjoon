# 최대 길이가 100만(1e6)이기 때문에
# KMP를 활용하여 O(N+M)로 푸는 플레티넘 문제였으나
# 파이썬 기본 in이 O(NM)에서 O(N+M)으로 바뀌면서
# 브론즈로 내려옴


import sys
input = sys.stdin.readline


S = input().rstrip()
P = input().rstrip()


print(1 if P in S else 0)
