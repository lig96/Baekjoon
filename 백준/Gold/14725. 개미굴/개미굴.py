import sys
input = sys.stdin.readline


graph = dict()


N = int(input())
for _ in range(N):
    temp = input().split()
    K, infos = temp[0], temp[1:]

    now, now_depth = 'default', 0
    now_dict = graph
    for info in infos:
        if (now, now_depth) in now_dict.keys():
            if (info, now_depth+1) not in now_dict[(now, now_depth)].keys():
                now_dict[(now, now_depth)][(info, now_depth+1)] = dict()
        else:
            now_dict[(now, now_depth)] = dict()
            now_dict[(now, now_depth)][(info, now_depth+1)] = dict()
        now_dict = now_dict[(now, now_depth)]
        now, now_depth = info, now_depth+1


def rec(start, graph):
    if start not in graph.keys():
        return
    for key in sorted(graph[start].keys()):
        print('--'*(key[1]-1), key[0], sep='')
        temp = (key[0], key[1])
        rec(temp, graph[start])


rec(('default', 0), graph)
