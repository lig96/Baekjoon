# bfs로는 불가능. len(S)=1, len(T)=1000이라면 2^999를 탐색해야 함.
# 그리디로 접근해야 한다.
# 문자열 혹은 리스트를 뒤집는 것은 O(N)이라서 deque를 사용했는데
# O(1)의 상수가 커서인지 약간이나마 느리다.

from collections import deque
import sys
input = sys.stdin.readline


def sol():
    string = deque(T)
    is_reversed = False
    while len(string) != len(S):
        if not is_reversed:
            if string[-1] == 'A':
                string.pop()
            else:
                string.pop()
                is_reversed = not is_reversed
        else:
            if string[0] == 'A':
                string.popleft()
            else:
                string.popleft()
                is_reversed = not is_reversed
    else:
        if not is_reversed:
            if ''.join(string) == S:
                return 1
            else:
                return 0
        else:
            if ''.join(string)[::-1] == S:
                return 1
            else:
                return 0


S = input().rstrip()
T = input().rstrip()


ans = sol()


print(ans)
