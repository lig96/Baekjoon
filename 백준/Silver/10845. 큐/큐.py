import sys
input = sys.stdin.readline
def print(x): return sys.stdout.write(str(x)+'\n')


class Node():
    def __init__(self, data):
        self.data = data
        self.nxt = None
        return


class LinkedList():
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
        return

    def enqueue(self, data):
        if self.front is None:
            node = Node(data)
            self.front = node
            self.rear = node
        else:
            node = Node(data)
            self.rear.nxt = node
            self.rear = node
        self.size += 1
        return

    def dequeue(self):
        if self.front is None:
            return -1
        else:
            temp = self.front.data
            if self.front is self.rear:
                self.front = None
                self.rear = None
            else:
                self.front = self.front.nxt
            self.size -= 1
            return temp

    def get_size(self):
        return self.size

    def get_empty(self):
        return (1 if self.size == 0 else 0)

    def get_front(self):
        if self.front is None:
            return -1
        else:
            return self.front.data

    def get_back(self):
        if self.rear is None:
            return -1
        else:
            return self.rear.data


N = int(input())
q = LinkedList()
for _ in range(N):
    command = input().split()
    if (t := command[0]) == 'push':
        q.enqueue(command[1])
    elif t == 'pop':
        print(q.dequeue())
    elif t == 'size':
        print(q.get_size())
    elif t == 'empty':
        print(q.get_empty())
    elif t == 'front':
        print(q.get_front())
    elif t == 'back':
        print(q.get_back())
    else:
        raise Exception
