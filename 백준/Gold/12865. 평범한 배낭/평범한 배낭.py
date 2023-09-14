# https://namu.wiki/w/배낭%20문제#s-3
# https://www.youtube.com/watch?v=uggO0uzGboY
# DP

N, K = map(int, input().split())
arr = [(int(W), int(V)) for W, V in ((input().split()) for _ in range(N))]


mat = [0 for _ in range(K+1)]


for w, v in arr:
    for row in range(K, -1, -1):
        if (mat[row] != 0) and ((row+w) <= K):
            mat[row+w] = max(mat[row+w], mat[row]+v)
    try:
        mat[w] = max(mat[w], v)
    except:
        pass


print(max(mat))
