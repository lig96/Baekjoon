from heapq import heappop, heappush, heapify
import sys
input = sys.stdin.readline

T = int(input())
for _1 in range(T):
    k = int(input())
    min_heap = []
    max_heap = []
    visited = [False for _ in range(k+1)]

    for id in range(k):
        char, n = input().split()
        n = int(n)
        if char == 'I':
            heappush(min_heap, (n, id))
            heappush(max_heap, (-n, id))
            visited[id] = True
        else:
            if n == -1:
                while min_heap and not visited[min_heap[0][1]]:
                    heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heappop(min_heap)
            elif n == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heappop(max_heap)
    else:
        while min_heap and not visited[min_heap[0][1]]:
            heappop(min_heap)
        while max_heap and not visited[max_heap[0][1]]:
            heappop(max_heap)

    if max_heap and min_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')
