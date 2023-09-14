# https://namu.wiki/w/배낭%20문제#s-3
# https://www.youtube.com/watch?v=uggO0uzGboY
# DP
# row가 가능한 무게의 종류, col이 물품의 종류


N, K = map(int, input().split())
arr = [(int(W), int(V)) for W, V in ((input().split()) for _ in range(N))]


mat = [0 for _ in range(K+1)]


for w, v in arr:
    if w > K:
        continue
    for row in range(K, -1, -1):
        if (mat[row] != 0) and ((row+w) <= K):
            mat[row+w] = max(mat[row+w], mat[row]+v)
    mat[w] = max(mat[w], v)

# for w, v in arr:
#     for row in range(K-w, -1, -1):
#         mat[row+w] = max(mat[row+w], mat[row]+v)
# 기본적으로는 동일한 코드

print(max(mat))
