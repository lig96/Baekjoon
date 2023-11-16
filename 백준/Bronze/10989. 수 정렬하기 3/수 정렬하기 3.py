import sys
input = sys.stdin.readline
print = sys.stdout.write

# 계수정렬
N = int(input())
count_arr = [0 for _ in range(10_000+1)]
for _ in range(N):
    num = int(input())
    count_arr[num] += 1
# sum_arr = []
# temp = 0
# for i in count_arr:
#     temp += i
#     sum_arr.append(temp)


for i in range(0, 10_000+1):
    # 정방향으로 가면 불안정 정렬
    # 거꾸로 하면 안정 정렬
    while count_arr[i] != 0:
        print(str(i)+'\n')
        count_arr[i] -= 1
        # sum_arr[i] -= 1
