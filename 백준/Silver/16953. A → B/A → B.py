# greedy

A, B = map(int, input().split())


ans = 1
while B > A:
    if str(B)[-1] == str(1):
        B = (B-1)//10
    elif 0 == B % 2:
        B = B//2
    else:
        B = 'wrong'
        break
    ans += 1


if B == A:
    print(ans)
else:
    print(-1)
