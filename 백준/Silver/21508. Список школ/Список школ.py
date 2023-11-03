from collections import defaultdict


dic = defaultdict(lambda: 0)


n = int(input())
for _ in range(n):
    school = input()
    num = ''
    for char in school:
        if char.isdecimal():
            num = num + char
    dic[num] += 1

ans = [k for k, v in dic.items() if v <= 5]
print(len(ans), *ans, sep='\n')
