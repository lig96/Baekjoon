
def is_promising(r, c):
    for prev_r, prev_c in enumerate(rows[:r]):
        # 자신보다 과거의 queen들을 순회

        # if prev_r == r:
        #     # 동일 row
        #     # 자명하게 해당 안 됨
        #     return False
        # if prev_c == c:
        #     # 동일 col
        #     # cols 리스트를 통해 이미 검증됨
        #     # 700ms -> 640ms
        #     return False
        if abs(r-prev_r) == abs(c-prev_c):
            # 동일 대각선
            return False
    return True


def dfs(r):
    global cnt

    if r == N:
        # 01234567 퀸을 놓고 8에 진입했다면
        # 이미 8개 다 완료한 상태.
        cnt += 1
        return
    for c in range(N):
        if not cols[c] and is_promising(r, c):
            rows[r] = c
            cols[c] = True
            dfs(r+1)
            # rows[r] = -1
            cols[c] = False


N = int(input())


rows = [-1 for _ in range(N)]
# rows[2]=3 이라면 row2, col3에 q가 있음
cols = [False for _ in range(N)]
# 시간 절약을 위해 col 조건을 따로 만듦
# N=11일 때 1400ms -> 700ms
cnt = 0


dfs(0)
# N*N 보드에 N개의 퀸을 놓아야 하기 때문에
# 어차피 모든 row마다 1개의 퀸이 있어야 함.
# dfs(0)은 0번째 row 속 ?번째 col에 퀸을 놓겠다는 뜻.
# 다음 깊이 dfs(1)로 진입하면 1번째 row에 놓겠다는 뜻.

print(cnt)
