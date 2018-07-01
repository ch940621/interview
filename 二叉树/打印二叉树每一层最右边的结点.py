from collections import deque


class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


class Queue(object):
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def front(self):
        return self.items[0]


# 就是二叉树的层次遍历的变种
# 打印最右边的就可以了


def print_rightest_node(head):
    if head == None:
        return None
    curr_level = Queue()
    next_level = Queue()
    curr_level.enqueue(head)

    while not curr_level.is_empty():
        curr = curr_level.dequeue()
        if curr != Node:
            # print(curr.value, '\t')
            next_level.enqueue(curr.left)
            next_level.enqueue(curr.right)

        if curr_level.is_empty:
            # print('\n')
            print(curr.value,'\n')
            curr_level, next_level = next_level, curr_level