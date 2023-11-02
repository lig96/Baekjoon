import sys
input = sys.stdin.readline


graph = dict()


N = int(input())
for _ in range(N):
    temp = input().split()
    K, infos = temp[0], temp[1:]

    now, now_d, now_dict = 'default', 0, graph
    for info in infos:
        if (now, now_d) in now_dict.keys():
            if (info, now_d+1) not in now_dict[(now, now_d)].keys():
                now_dict[(now, now_d)][(info, now_d+1)] = dict()
        else:
            now_dict[(now, now_d)] = dict()
            now_dict[(now, now_d)][(info, now_d+1)] = dict()
        now, now_d, now_dict = info, now_d+1, now_dict[(now, now_d)]


def rec(start, graph):
    if start not in graph.keys():
        return
    for now, now_d in sorted(graph[start].keys()):
        print('--'*(now_d-1), now, sep='')
        rec((now, now_d), graph[start])


rec(('default', 0), graph)
