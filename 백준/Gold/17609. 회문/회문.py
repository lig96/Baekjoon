import sys
input = sys.stdin.readline


def sol(s, type):
    if type == 2:
        return
    for i in range(0, ((len(s)+1)//2)):
        j = len(s)-i-1
        if s[i] != s[j]:
            # s = 1s[:i]+2s[i]+3s[i+1:j]+4s[j]+5s[j+1:]
            # 1, 5는 이미 회문인 게 확인이 되었으니 불필요.
            # 2, 4는 서로 다름. 3은 모름.
            # sol(start_i, end_i)처럼 투포인터로 풀이 가능.
            sol(s[i:j], type+1)  # 23
            sol(s[i+1:j+1], type+1)  # 34
            ans.append(2)
            return
    else:
        ans.append(type)
        return


T = int(input())
for _ in range(T):
    s = input().rstrip()

    ans = []
    sol(s, 0)

    print(min(ans))
    # print(ans)
