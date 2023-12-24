def dfs(ind, string):
    if len(string) == L:
        vowel_cnt, consonant_cnt = 0, 0
        for s in string:
            if s in 'aeiou':
                vowel_cnt += 1
            else:
                consonant_cnt += 1
        if vowel_cnt >= 1 and consonant_cnt >= 2:
            print(string)
        return
    if ind == C:
        return

    dfs(ind+1, string+chars[ind])
    dfs(ind+1, string)
    return


L, C = map(int, input().split())
chars = sorted(input().split())


dfs(0, '')
