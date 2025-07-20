import sys
input = sys.stdin.readline


def sys_print(*x, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, x))+end)
    return None


def sol_dfs(n, m, graph):
    def _dfs(n, m, graph, visited, v, parent):
        ret = 1
        visited[v] = True
        for child in graph[v]:
            if not visited[child]:
                ret &= _dfs(n, m, graph, visited, child, v)
            else:
                if parent != child:
                    ret = 0
        return ret
    ret = 0
    visited = [False for _ in range(n+1)]
    for v in range(1, n+1):
        if not visited[v]:
            temp = _dfs(n, m, graph, visited, v, None)
            ret += temp
    return ret


def sol_unionfind(n, m, graph, edges):
    def _union(a, b):
        a, b = _find(a), _find(b)
        if a == b:
            # 이미 a와 b로 연결이 되있는데
            # 다시 연결을 시키려고 한다면
            parent[a] = 0
            return
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
        return

    def _find(x):
        if parent[x] != x:
            parent[x] = _find(parent[x])
        return parent[x]

    parent = [i for i in range(n+1)]
    # 원인덱싱
    # find(x)==0이라면 해당 정점이 속한 연결 요소가 사이클이 있다는 뜻
    for a, b in edges:
        _union(a, b)
    ret = len(set(_find(i) for i in range(n+1))) - 1
    # find(i)==0이라면 사이클이 있다는 뜻이니 하나를 빼줘야 함
    return ret


case_ind = 0
while True:
    case_ind += 1
    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        break
    graph = [[] for _ in range(n+1)]  # 원인덱싱
    edges = []
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        edges.append((a, b))

    ans = sol_dfs(n, m, graph)
    # ans = sol_unionfind(n, m, graph, edges)
    if ans == 0:
        sys_print(f"Case {case_ind}: No trees.")
    elif ans == 1:
        sys_print(f"Case {case_ind}: There is one tree.")
    else:
        sys_print(f"Case {case_ind}: A forest of {ans} trees.")
