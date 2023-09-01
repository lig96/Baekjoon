left = dict()
right = dict()
for char in range(N := int(input())):
    node, leftnode, rightnode = input().split()
    left[node] = leftnode
    right[node] = rightnode


def preorder(start):
    print(start, end='')
    if left[start].isalpha():
        preorder(left[start])
    if right[start].isalpha():
        preorder(right[start])


def inorder(start):
    if left[start].isalpha():
        inorder(left[start])
    print(start, end='')
    if right[start].isalpha():
        inorder(right[start])


def postorder(start):
    if left[start].isalpha():
        postorder(left[start])
    if right[start].isalpha():
        postorder(right[start])
    print(start, end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')