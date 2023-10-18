####################
# https://leeingyun96.tistory.com/23

####################
# 1.

K = int(input())
if K == 0:
    print(0)
elif K % 2 == 0:
    print(-1)
else:
    print(K.bit_length())

####################
# 2.

K = abs(int(input()))
if K == 0:
    print(0)
elif K % 2 == 0:
    print(-1)
else:
    ans = 0
    while K > 0:
        K = K >> 1
        ans += 1
    print(ans)

####################
