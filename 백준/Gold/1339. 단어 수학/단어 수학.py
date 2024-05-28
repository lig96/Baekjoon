# 단어의 개수를 N, 알파벳의 종류를 X, 수의 최대 길이를 Y라 하자
#
# 방법 1: 그리디
# O(N * (X + Y)) = O(2e2)
#
# 방법 2: 완전탐색
# O(X! * N * Y) = O(3e8)
# 파이썬에서는 시간 초과지만 C에서는 됨
# dict/map보다 배열이 더 빠름


import sys
input = sys.stdin.readline


N = int(input())
words = []
for _ in range(N):
    word = input().rstrip()
    word = '_'*(8-len(word)) + word
    words.append(word)


alphas = set(''.join(words)) - set('_')
# 세트
# 단어에서 포함된 알파벳의 종류
alphas = {x: 0 for x in alphas}
for i in range(8):
    alphas = {k: v*10 for k, v in alphas.items()}
    for word in words:
        char = word[i]
        if char != '_':
            alphas[char] += 1
# 딕셔너리
# 단어에서 포함된 알파벳들이 최종 변환된 합에 기여하는 배율
alphas = sorted(list(alphas.items()), key=lambda x: -x[1])
# 리스트
# 배율에 따라 내림차순 정렬
numbers = list(range(9, -1, -1))
alphas = {v[0]: numbers[i] for i, v in enumerate(alphas)}
# 딕셔너리
# 배율에 따라 9~0 값을 매핑


ans = 0
for word in words:
    temp = 0
    for char in word:
        if char != '_':
            temp = temp*10 + alphas[char]
    ans += temp


print(ans)
