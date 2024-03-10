N = int(input())
operations = list(input())
dic = dict()
for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:N]:
    dic[char] = input()


stack = []


for i, v in enumerate(operations):
    if v.isalpha():
        stack.append(dic[v])
    else:
        right = stack.pop()
        left = stack.pop()
        temp = str(eval(left+v+right))
        stack.append(temp)


ans = float(stack.pop())
print(f'{ans:.2f}')
