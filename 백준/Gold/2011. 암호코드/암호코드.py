import sys
sys.setrecursionlimit(5000+100)
input = sys.stdin.readline


def rec(txt):
    if txt in dp:
        return dp[txt]

    left_ret = (txt[0:1] in char and len(txt) >= 1) \
        * rec(txt[1:])
    right_ret = (txt[0:2] in char and len(txt) >= 2) \
        * rec(txt[2:])
    dp[txt] = (left_ret + right_ret) % MOD
    return dp[txt]


txt = input().rstrip()
MOD = 1_000_000


char = set(str(i) for i in range(1, 27))
dp = {}
dp[""] = 1


print(rec(txt))
