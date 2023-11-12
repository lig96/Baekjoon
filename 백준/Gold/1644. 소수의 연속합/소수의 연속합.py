def make_prime():
    # sparse
    prime = [True for _ in range(0, N+1)]
    prime[0] = prime[1] = False
    for i in range(0, N+1):
        if prime[i]:
            # 에라토네스의 체에서 지워지지 않았다면
            # prime[i] = True, dense_arr.append(i)
            j = 2
            while i*j <= N:
                prime[i*j] = False
                j += 1
    # dense
    prime = [i for i, v in enumerate(prime) if v]
    return prime


N = int(input())
if N < 2:
    # prime[0]이 없을 정도로 N이 작다면
    print(0)
    exit()

prime = make_prime()
cnt = 0
left, right = 0, 0  # inclusive, inclusive
my_sum = prime[0]


while True:  # prime 리스트에서 IndexError가 날 때 탈출
    if my_sum > N:
        my_sum -= prime[left]
        left += 1
    elif my_sum == N:
        cnt += 1
        right += 1
        if right == len(prime):
            break
        my_sum += prime[right]
    elif my_sum < N:
        right += 1
        if right == len(prime):
            break
        my_sum += prime[right]
print(cnt)
