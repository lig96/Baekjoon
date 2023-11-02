# import sys
# if 'utf-8' != sys.stdin.encoding:
#     raise Exception
# 로컬 환경은 다를 수 있지만
# 백준 python3 환경은 utf-8
# 백준 pypy3 환경은 utf-8이 아닌 무언가

# print(sys.getdefaultencoding())
# print(sys.stdin.encoding)
# print(sys.stdout.encoding)
# 인코딩을 확인하는 방법은 위와 같고

# sys.stdin.reconfigure(encoding='utf-8')
# sys.stdout.reconfigure(encoding='utf-8')
# 인코딩을 변경하는 방법은 위와 같다.

# python, pypy 둘 다 전부 주석 처리 해도 답 처리 된다.
# 출제자가 의도한 풀이는 유니코드를 3자리씩 끊어서 비교하기인 듯하다.
# C와 달리 파이썬에서는 1글자로 처리되는 듯하다.

a, b = input(), input()


dp = [[0 for _ in range(len(b)+1)]
      for _ in range(len(a)+1)]


for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])


print(dp[-1][-1])
