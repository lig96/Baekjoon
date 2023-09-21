# https://namu.wiki/w/배낭%20문제#s-3
# https://www.youtube.com/watch?v=A8nOpWRXQrs
# DP_2, 재귀

N, K = map(int, input().split())
arr = [(int(W), int(V)) for W, V in ((input().split()) for _ in range(N))]
# ws, vs = zip(*arr)


def rec(i, w):
    wi, vi = arr[i]
    if i == 0:
        if wi > w:
            return 0
        else:  # ws[i] <= w:
            return vi

    if wi > w:
        return rec(i-1, w)
    else:
        left = rec(i-1, w) # 라인 22
        right = arr[i][1]+rec(i-1, w-wi) # 라인 23
        return max(left, right)


ans = rec(N-1, K)
print(ans)

# 2차원 행렬 속에서 반복문을 돌지 않고
# 재귀 속에서 필요한 부분만 찾아나간다.
# 라인 22, 라인 23에서 memoization이 필요한데
# 처리를 해줘도 여전히 시간 초과가 돼서 제출을 못 하였다.
