# 666의 왼쪽에 숫자를 붙여 1_666, 2_666, ~~~, N_666처럼
# 숫자를 만들면 N*1000 + 666에서
# 최소한 N개의 종말의 수를 만들 수 있다.
# 반복문의 최댓값은 10_000_666으로 O(1e7)

# naive 문자열 검색 알고리즘의 시간 복잡도는
# O((text - pattern + 1) * pattern)으로 약 O(text*pattern)
# pattern이 3자리고 text가 8자리이니 O(24)

# 합치면 naive이더라도 2.4e8
# 이 과정에서 더 많은 종말의 수가 나올 것이고(666_N 등)
# 파이썬의 기본 구현은 O(text) 정도로 상당히 빠르니
# 브루트포스로도 가능하다.


N = int(input())


pattern = '666'
cnt = 0
ans = None


for num in range(666, (N*1000 + 666) + 1):
    if pattern in str(num):
        cnt += 1
        if cnt == N:
            ans = num
            break


print(ans)
