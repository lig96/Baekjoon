# https://velog.io/@nmrhtn7898/ps-0-1-BFS(2021년)
# 0-1 BFS에서는 가중치가 낮은 간선을 먼저 넣어야 한다.
# https://www.acmicpc.net/board/view/38887#comment-69010(2019년)
# 다익스트라 / 0-1 BFS, 0을 먼저 넣기 / 별도의 처리
# 3가지 풀이(+재귀)를 제시하지만 이 문제는 단순히 그것만으로는 풀리지 않는다.
# 4-3-6(1)이냐 4-5-6(2)이냐에서 0의 순서는 상관이 없기 때문이다.
# https://www.acmicpc.net/board/view/121219#comment-188376
# 해당 링크도 동일한 문제를 겪고 있다.
# 2021년 자바 풀이도 순서를 바꾸면 4 6이 오답 2를 출력한다.
# https://www.acmicpc.net/board/view/120041#comment-186955(2023년)
# 2023년 6월에야 데이터가 추가되었고
# 해당 시점 이전에 작성된 풀이는 오류가 섞여있는 것에 주의해야 한다.
# 결론적으로 (조금 줄이고 크게 키우기), (조금 키우고 조금 키우기)가
# 동일한 결과, 다른 과정을 낼 수 있다는 점을 파악하고
# 전자가 과정이 빠를 수 있기 때문에 우선시 되어야 한다는 점을 파악하는 것이야말로 중요했다.

from collections import deque


N, K = map(int, input().split())


MAX_K = min(2*K+1, 100_000+1) if N < K else (print(N-K), exit())
visited = [-1 for _ in range(MAX_K)]
visited[N] = 0
qu = deque([(N, 0)])

while qu:
    loc, time = qu.popleft()

    for newloc, newtime in zip((loc*2, loc-1, loc+1), (time, time+1, time+1)):
        if (0 <= newloc < len(visited)) and (visited[newloc] == -1):
            visited[newloc] = newtime
            if newloc == loc*2:
                qu.appendleft((newloc, newtime))
            else:
                qu.append((newloc, newtime))

    if visited[K] != -1:
        break


print(visited[K])
