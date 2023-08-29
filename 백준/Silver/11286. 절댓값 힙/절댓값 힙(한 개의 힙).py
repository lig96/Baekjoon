from heapq import heappush, heappop
import sys
input = sys.stdin.readline
print = sys.stdout.write


heap = []


N = int(input())
for _ in range(N):
    x = int(input())
    if x != 0:
        heappush(heap, (abs(x), x))
    else:
        if heap:
            a, b = heappop(heap)
            print(str(b)+'\n')
        else:
            print(str(0)+'\n')


# https://github.com/python/cpython/blob/3.11/Lib/heapq.py
# def heappush(heap, item):
#     """Push item onto heap, maintaining the heap invariant."""
#     heap.append(item)
#     _siftdown(heap, 0, len(heap)-1)
# def _siftdown(heap, startpos, pos):
#     newitem = heap[pos]
#     # Follow the path to the root, moving parents down until finding a place
#     # newitem fits.
#     while pos > startpos:
#         parentpos = (pos - 1) >> 1
#         parent = heap[parentpos]
#         if newitem < parent:
#             heap[pos] = parent
#             pos = parentpos
#             continue
#         break
#     heap[pos] = newitem

# 파이썬 heapq는 위와 같은 소스코드로 구성되어있다.
# heappush를 실행할 경우 내부에서 _siftdown 함수가 호출된다.
# 이때 heap 정렬을 시행하기 위해 "newitem < parent" 조건문을 거친다.
# 즉, heap 속의 아이템을 튜플로 줄 경우 "newitem튜플 < parent튜플"을 거친다.


# https://docs.python.org/3/reference/expressions.html#value-comparisons
# Sequences (instances of tuple, list, or range) can be compared (중략)
# Lexicographical comparison between built-in collections works as follows: (후략)

# 대소 비교는 Lexicographical, 즉 사전순으로 이루어진다.
# 튜플의 첫 번째 요소를 key로 정렬 후, 두 번째 요소를 key로 정렬 후, ~~~
# 하는 방식으로 이루어진다.


# 이번 문제의 경우 절댓값이 작은 것이 1순위, 값이 작은 것이 2순위였기 때문에
# heap을 2개로 나누지 않더라도 구현할 수 있다.
# 튜플의 첫 번째 요소만이 key로 사용된다고 적은 블로그가 많아서 헷갈림을 해소하는 데에 어려움을 겪었다.
