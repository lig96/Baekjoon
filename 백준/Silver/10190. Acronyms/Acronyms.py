import re


def sol(acronym, string):
    acronym = list(acronym)
    acronym = '\S*\s'.join(acronym)+'\S*$'
    ans = re.findall(acronym, string)
    return ans


n = int(input())
for _ in range(n):
    acronym, p = input().split()
    print(acronym)
    for _ in range(int(p)):
        string = input()
        if sol(acronym, string):
            print(string)
