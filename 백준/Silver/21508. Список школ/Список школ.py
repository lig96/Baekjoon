import re
from collections import defaultdict


def make_num_by_regex():
    num = re.search('[\d]+', school).group()
    return num


def make_num_by_loop():
    num = ''
    for char in school:
        if char.isdecimal():
            num += char
    return num


dic = defaultdict(lambda: 0)


n = int(input())
for _ in range(n):
    school = input()
    # num = make_num_by_regex()
    num = make_num_by_loop()
    dic[num] += 1

ans = [k for k, v in dic.items() if v <= 5]
print(len(ans), *ans, sep='\n')
