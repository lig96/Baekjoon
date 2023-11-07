# 1013


def dfs(n, string):
    if n == N+1:
        string2 = ''.join([x for x in string if x != ' '])
        if eval(string2) == 0:
            print(string)
            return
        else:
            return

    if string == '':
        dfs(n+1, str(n))
    else:
        for oper in [' ', '+',  '-']:
            dfs(n+1, string+oper+str(n))


T = int(input())
for _ in range(T):
    N = int(input())
    dfs(1, '')
    print()
