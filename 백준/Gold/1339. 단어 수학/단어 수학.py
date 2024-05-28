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
