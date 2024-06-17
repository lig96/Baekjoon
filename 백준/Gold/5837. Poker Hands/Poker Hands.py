# 풀이: https://readble-ko.tistory.com/154


import sys
input = sys.stdin.readline


N = int(input())
a_i = [int(input()) for _ in range(N)]


# d = a_i
# d = [0] + d + [0]
a_i.append(0)  # 맨 왼쪽 0 대신 -1 인덱싱으로 오른쪽 0으로 갈음함
dd = [a_i[i] - a_i[i-1] for i in range(N+1)]
ans = sum(map(abs, dd))//2


print(ans)
