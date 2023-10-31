import re


n = int(input())
for _ in range(n):
    strings = input()

    ans = re.findall('([pP]).*?([lL]).*?([uU])', strings)

    print(len(ans))
