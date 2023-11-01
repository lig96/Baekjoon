import sys
input = sys.stdin.readline


def sol(string, type):
    if type == 2:
        return
    for i in range(0, ((len(string)+1)//2)):
        j = len(string)-i-1
        if string[i] != string[j]:
            sol(string[:i]+string[i+1:], type+1)
            sol(string[:j]+string[j+1:], type+1)
            ans.append(2)
            return
    else:
        ans.append(type)
        return


T = int(input())
for _ in range(T):
    string = input().rstrip()

    ans = []
    sol(string, 0)

    print(min(ans))
