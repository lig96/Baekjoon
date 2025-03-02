# "09"와 "9"를 구별하기 위해 그리고 지문에 나온대로 정직하게 str을 쓰자.
# int를 쓰면 어떤 면에서는 조금 더 깔끔하지만 오류가 난다.
#
# string 슬라이싱은 절대로 IndexError가 안 나지만
# 오히려 이 점 때문에 "1"과 "1"+IndexError를 구별하지 못한다.
# 정확히 2 글자가 필요하다면 지금처럼 if문을 쓰거나
# 인덱싱과 try문을 쓰자.


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
