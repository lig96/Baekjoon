# from collections import deque
import sys
input = sys.stdin.readline
sys_print = sys.stdout.write


# back - [0, 1, 2, 3, 4] - front
# appendleft               append
class Node():
    def __init__(self, data, frontward, backward):
        self.data = data
        self.frontward = frontward
        self.backward = backward
        return


class Deque():
    def __init__(self):
        self.front = Node(None, None, None)
        self.back = Node(None, None, None)
        self.front.backward, self.back.frontward = self.back, self.front
        self.len = 0
        return

    def append(self, X):  # front
        node = Node(X, frontward=self.front, backward=self.front.backward)
        node.frontward.backward = node
        node.backward.frontward = node
        self.len += 1
        return

    def appendleft(self, X):  # back
        node = Node(X, frontward=self.back.frontward, backward=self.back)
        node.frontward.backward = node
        node.backward.frontward = node
        self.len += 1
        return

    def pop(self):  # front
        if self.len == 0:
            return -1
        node = self.front.backward
        node.frontward.backward = node.backward
        node.backward.frontward = node.frontward
        self.len -= 1
        return node.data

    def popleft(self):  # back
        if self.len == 0:
            return -1
        node = self.back.frontward
        node.frontward.backward = node.backward
        node.backward.frontward = node.frontward
        self.len -= 1
        return node.data

    def __len__(self):
        return self.len

    def __bool__(self):
        return bool(self.len)

    def __getitem__(self, key):
        if self.len == 0:
            # 현재 코드에서는 이 에러가 뜨기 전에
            # if dq 조건문에 걸리긴 함
            return IndexError
        if key == 0:  # back
            return self.back.frontward.data
        elif key == -1:  # front
            return self.front.backward.data
        else:
            raise NotImplementedError


N = int(input())
opers = [input().split() for _ in range(N)]


dq = Deque()


for temp in opers:
    if len(temp) == 2:
        oper, X = temp[0],  int(temp[1])
    elif len(temp) == 1:
        oper = temp[0]
    else:
        raise Exception

    if oper == 'push_front':
        dq.append(X)
    elif oper == 'push_back':
        dq.appendleft(X)
    elif oper == 'pop_front':
        print(dq.pop())
    elif oper == 'pop_back':
        print(dq.popleft())
    elif oper == 'size':
        print(len(dq))
    elif oper == 'empty':
        if dq:
            print(0)
        else:
            print(1)
    elif oper == 'front':
        if dq:
            print(dq[-1])
        else:
            print(-1)
    elif oper == 'back':
        if dq:
            print(dq[0])
        else:
            print(-1)
    else:
        raise Exception
