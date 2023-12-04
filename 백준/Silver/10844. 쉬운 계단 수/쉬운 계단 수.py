N = int(input())


dp_old = [1 for _ in range(10)]
dp_new = [1 for _ in range(10)]


# N == 1이라면
# 반복문에 안 들어가고 dp도 바뀌지 않음
for i in range(N-1):
    for j in range(10):
        if j == 0:
            dp_new[j] = dp_old[j+1]
        elif j == 9:
            dp_new[j] = dp_old[j-1]
        else:
            dp_new[j] = dp_old[j-1]+dp_old[j+1]
    dp_old = dp_new[::]
    # dp_new의 모든 원소는 전부 새로 대입되기 때문에
    # 새로 선언할 필요 없음
    # 깊은 복사는 해줘야 함.


print(sum(dp_new[1:]) % 1_000_000_000)
