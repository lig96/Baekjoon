# 방법 1: 조합론
# 종류가 동일하면서 연속된 소의 개수의 배열을 만든다.
# GGGGGHGGH -> 0, 5, 1, 2, 1, 0
# solve(left, mid, right)로 조합론으로 구한다.
# if mid==1: left+mid+right 연속으로
# else: left+mid의왼쪽, mid의오른쪽+right
# mid를 1개만 쓰는 경우의 수만 고려한다.
# mid(a,b,c 중 b)를 2개 이상 쓰는 경우의 수는 mid가 한 칸 넘어가서
# b,c,d가 됐을 때 left로서 구해진다.
#
# 방법 2: 이분탐색
# i를 0부터 N까지 순회를 돌며 v=cows[i]가 시작인 수열의 개수를 구한다.
# wlog v=='G'라 하자. v를 1번만 쓰는 정답은 i~다음번'G'의등장인덱스이다.
# v를 2번 이상 쓰는 정답은 다음번'H'의등장인덱스~다다음번'H'의등장인덱스이다.


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
    # [7, 9)까지는 lonely photo 확정
    if (temp := second_next_i-max(first_next_i, left_i+2)) >= 0:
        ans += temp


print(ans)
