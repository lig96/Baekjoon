# 페이지 교체 알고리즘 중 OPT 알고리즘을 구현하면 됨
# O(NKK)


import sys
input = sys.stdin.readline


N, K = map(int, input().split())
names = list(map(int, input().split()))  # 길이 K


multitap = set()  # 길이 N
cnt = 0
for i in range(K):  # O(K)
    name = names[i]
    if name in multitap:
        # 이미 멀티탭에 꽂혀있어서 다른 것을 뽑을 필요가 없음
        pass
    else:
        if len(multitap) == N:
            # 멀티탭이 꽉 차서 다른 것을 뽑아야 함
            latest_usage, latest_name = -float('inf'), None
            for member in multitap:  # O(N)
                temp_usage = (names[i+1:].index(member) if (member in names[i+1:])
                              else float('inf'))  # O(K)
                # temp_usage = 미래 중에서 member가 쓰이는 첫 번째 인덱스
                if latest_usage < temp_usage:
                    latest_usage, latest_name = temp_usage, member

            multitap.remove(latest_name)
            cnt += 1
            # 뽑은 것을 언젠가는 다시 꽂아야 할 때가 오는데
            # 그 시간을 최대한 뒤로 늦추는 알고리즘
            multitap.add(name)
        else:
            # 멀티탭이 비어있어서 현재 name을 꽂을 수 있음
            # 이 경우 무조건 꽂는 게 유리
            multitap.add(name)


print(cnt)
