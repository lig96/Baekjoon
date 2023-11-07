import sys
print = sys.stdout.write


def dfs(n, string):
    if n == N+1:
        if eval(string.replace(' ', '')) == 0:
            print(string+'\n')
            return
        else:
            return

    if string == '':
        dfs(n+1, str(n))
    else:
        for oper in [' ', '+',  '-']:
            # # ASCII 순서에 따라
            # print(oper, ord(oper))
            # 32, 43, 45
            dfs(n+1, string+oper+str(n))


T = int(input())
for _ in range(T):
    N = int(input())
    dfs(1, '')
    print('\n')
