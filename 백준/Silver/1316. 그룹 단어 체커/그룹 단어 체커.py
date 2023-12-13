def sol(word):
    dic = dict()
    prev = ''
    for char in word:
        if prev != char:
            if char in dic:
                return 0
            else:
                dic[char] = True
        prev = char
    return 1


N = int(input())
words = [input() for _ in range(N)]


ans = 0
for word in words:
    ans += sol(word)


print(ans)
