
# 1 - 문자열의 뒤에 A를 추가한다.
# 2 - 문자열의 뒤에 B를 추가하고 문자열을 뒤집는다.


def dfs(S, T):
    global ans

    if len(S) > len(T):
        return
    elif len(S) == len(T):
        if S == T:
            ans = 1
        return

    if T[0] == 'A' and T[-1] == 'A':
        # 1
        dfs(S, T[0:-1])
    elif T[0] == 'A' and T[-1] == 'B':
        pass
    elif T[0] == 'B' and T[-1] == 'A':
        # 1
        dfs(S, T[0:-1])
        # 2
        dfs(S, T[1:][::-1])
    elif T[0] == 'B' and T[-1] == 'B':
        # 2
        dfs(S, T[1:][::-1])


S = input()
T = input()

ans = 0


dfs(S, T)


print(ans)
