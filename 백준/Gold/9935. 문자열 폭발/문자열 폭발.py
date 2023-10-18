strings = list(input())
bomb = list(input())


stack = []
len_bomb = len(bomb)
last_bomb = bomb[-1]


for string in strings:
    stack.append(string)
    if (string == last_bomb) and (stack[-len_bomb:] == bomb):
        del stack[-len_bomb:]


print(''.join(stack) if stack else 'FRULA')