def topol():
    # dfs, indegree
    len_topol_arr = 0

    stack = []
    for i in range(1, n+1):
        if indegree[i] == 0:
            stack.append(i)
            len_topol_arr += 1

    while stack:
        now = stack.pop()
        for end in graph[now]:
            indegree[end] -= 1
            if indegree[end] == 0:
                stack.append(end)
                len_topol_arr += 1
    return len_topol_arr


T = int(input())
for _ in range(T):
    n = int(input())
    students = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    indegree = [0 for _ in range(n+1)]
    for i, v in enumerate(students, 1):
        graph[i].append(v)
        indegree[v] += 1

    print(topol())
    # 사이클을 이루지 않는다면, topol_arr 내에 들어감
