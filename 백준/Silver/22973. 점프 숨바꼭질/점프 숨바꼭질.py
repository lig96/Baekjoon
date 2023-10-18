
K = abs(int(input()))

if K == 0:
    print(0)
    exit()
elif K % 2 == 0:
    print(-1)
    exit()


ans = 0
while K > 0:
    if (K & 1):
        K = K >> 1
        ans += 1
        # print(K)
    else:
        ans += 1
        K = K >> 1
        # print(K)
print(ans)