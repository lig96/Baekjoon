# 방법 1.
# 구현, 브루트 포스, 그리디
# 1000 사이즈 배열의 pillars를 만들고
# 규칙에 따라 높이를 변형 후
# sum(pillars) 출력
# (실2)

# 방법 2.
# 스택
# #2493(골5)와 유사하게 monotone stack을 만들되
# 강단조증가&약단조감소,
# 약단조증가&강단조감소,
# 강단조증가&상수&강단조감소,
# 중 하나를 구현한 뒤 규칙에 따라 면적을 더해준다.
# (골4)


# 방법 1.
import sys
input = sys.stdin.readline


N = int(input())
pillars = [0 for _ in range(1001)]
for _ in range(N):
    L, H = map(int, input().split())
    pillars[L] = H


max_i = pillars.index(max(pillars))


for i in range(0, max_i):
    if pillars[i] > pillars[i+1]:
        pillars[i+1] = pillars[i]
for i in range(max_i, len(pillars)-1)[::-1]:
    if pillars[i] < pillars[i+1]:
        pillars[i] = pillars[i+1]


print(sum(pillars))


# 방법 2.
# import sys
# input = sys.stdin.readline


# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]


# arr.sort(key=lambda x: x[0])
# ascending = [(None, -float('inf'))]
# descending = [(None, float('inf'))]


# for L, H in arr:
#     if ascending[-1][1] < H:
#         ascending.append((L, H))
#     # 강한 단조 증가
#     # 중복된 max_H는 들어가지 않음

#     while descending[-1][1] < H:
#         descending.pop()
#     else:
#         descending.append((L, H))
#     # 약한 단조 감소
#     # 중복된 max_H가 여러 개 들어감


# ans = 0
# # 0번 인덱스에 INF가 있으니 range는 1부터
# for i in range(1, len(ascending)-1):
#     L1, H1 = ascending[i]
#     L2, H2 = ascending[i+1]
#     ans += (L2-L1)*H1
# if True:
#     ans += ascending[-1][1]  # max_H
#     # max_H의 왼쪽과 오른쪽의 면적을 더해줬기 때문에
#     # max_H 기둥 자체는 더해지지 않았음
# for i in range(1, len(descending)-1):
#     L1, H1 = descending[i]
#     L2, H2 = descending[i+1]
#     ans += (L2-L1)*H2


# print(ans)
