S = input()


my_set = set()


for s in range(0, len(S)):
    temp = ''
    for e in range(s, len(S)):
        temp = temp + S[e]
        my_set.add(temp)


print(len(my_set))