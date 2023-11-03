import re


N = int(input())
p = re.compile(re.sub('\*', '[a-z]*', input()))
for _ in range(N):
    name = input()

    print('DA' if p.fullmatch(name) else 'NE')
