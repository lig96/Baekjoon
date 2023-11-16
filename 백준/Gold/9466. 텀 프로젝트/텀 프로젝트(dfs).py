import sys
sys.setrecursionlimit(int(1e5)+10)


def dfs(start):
    global len_cycle, cycle

    visited[start] = True
    cycle.append(start)

    end = graph[start][0]  # 인접리스트 요소가 1개뿐
    if not visited[end]:
        dfs(end)
    else:
        try:
            middle_index = cycle.index(end)
            len_cycle += len(cycle) - middle_index
            # len(cycle) 길이만큼의 직선이 있고
            # 꼬리와 머리가 맞닿는 부분이 middle_index
        except ValueError:
            # cycle 내에 end가 없으면
            pass


T = int(input())
for _ in range(T):
    n = int(input())
    students = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    indegree = [0 for _ in range(n+1)]
    for i, v in enumerate(students, 1):
        graph[i].append(v)
        indegree[v] += 1
    visited = [False for _ in range(n+1)]

    len_cycle = 0
    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(n - len_cycle)
