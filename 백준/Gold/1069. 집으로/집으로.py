import sys
input = sys.stdin.readline


X, Y, D, T = map(int, input().split())


DIST = (X**2+Y**2)**(1/2)
cnt_l = int(DIST/D)  # 모자르거나 딱 맞게 점프
cnt_h = cnt_l+1  # 지나치게 점프


ans = []
# cnt_l만큼 직선으로 점프 + 나머지만큼 직선으로 걷기
ans.append(
    T*(cnt_l) + 1*(DIST-(D*cnt_l))
)
# cnt_h만큼 직선으로 점프 + 나머지만큼 직선으로 걷기
ans.append(
    T*(cnt_h) + 1*abs(DIST-(D*(cnt_h)))
)
# cnt_l-1만큼 직선으로 점프 + 2번을 V모양으로 점프 + 0걷기
ans.append(
    T*(max(cnt_l-1, 0)+2) + 1*(0)
)  # cnt_l+1과는 다름. DIST>=<D 조건 분기를 해야 같음.
# 0점프 + 나머지만큼 직선으로 걷기
ans.append(
    T*(0) + 1*(DIST)
)


print(min(ans))
