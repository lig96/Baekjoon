# https://namu.wiki/w/배낭%20문제#s-3
# https://www.youtube.com/watch?v=uWigKsbo3SU
# 백트래킹(dfs)


N, K = map(int, input().split())
arr = [(int(V)/int(W), int(W), int(V)) for W, V in
       ((input().split()) for _ in range(N))]
arr = sorted(arr, key=lambda x: -x[0])
# 효율 내림차순으로 정렬


def dfs(i, v, w, best):
    if w > K:
        # 이전 i가 무게 초과라면 best 갱신 불가능
        return best
    # 무게 초과가 아니라면 best 갱신 가능
    best = max(v, best)
    if i == N:
        # arr 순회가 끝났다면
        return best
    nowrate, noww, nowv = arr[i]
    if v + (K-w)*nowrate < best:
        # (현재 가치 + 여유 무게*최고의 효율)을 해도 best보다 낮다면
        return best


    for way in [True, False]:
        best = dfs(i+1, v+nowv*way, w+noww*way, best)

    return best


ans = dfs(0, 0, 0, 0)
print(ans)

# 시간 초과가 나서 제출은 못 하였다.
