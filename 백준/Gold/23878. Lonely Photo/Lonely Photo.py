from bisect import bisect_left
import sys
input = sys.stdin.readline


N = int(input())
cows = input().rstrip()  # str 타입


transform = {'G': 'H', 'H': 'G'}
dic = {'G': [], 'H': []}
for i, v in enumerate(cows):
    dic[v].append(i)
for key in dic.keys():
    dic[key].append(N)
    dic[key].append(N)


ans = 0
for left_i, left in enumerate(cows):
    # left가 1개인 경우
    first_next_i = dic[left][bisect_left(dic[left], left_i)+1]
    # left_i=3, first=9이라면
    # [3, 9)까지는 lonely photo 확정
    if (temp := first_next_i-(left_i+2)) >= 0:
        ans += temp

    # left가 2개 이상인 경우
    opp = transform[left]
    first_next_i = dic[opp][bisect_left(dic[opp], left_i)]
    second_next_i = dic[opp][bisect_left(dic[opp], left_i)+1]
    # left_i=3, first=7, second=9라면
    # 3,4,5,6,7,8
    # [3, 7], [3, 8] 이렇게 2개.
    if (temp := second_next_i-max(first_next_i, left_i+2)) >= 0:
        ans += temp


print(ans)