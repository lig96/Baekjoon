# 그리디 알고리즘처럼
# 처음 num[i] < num[i+1]이 되는 num[i]를 없애는 게 언제나 최적이다.
# 이는 결과적으로 약단조감소 배열을 만든다는 뜻이 된다.


import sys
input = sys.stdin.readline
sys_print = sys.stdout.write


N, K = map(int, input().split())
num: str = input().rstrip()


num: list[int] = list(map(int, num))
remained_K = K
stack = list()
stack.append(float('inf'))


for v in num:
    while stack[-1] < v and remained_K:
        stack.pop()
        remained_K -= 1
    else:
        stack.append(v)
else:
    while remained_K:
        stack.pop()
        remained_K -= 1
    stack.pop(0)  # 인덱스 0에 위치한 기본 값을 제거한다.


sys_print(''.join(map(str, stack)))
