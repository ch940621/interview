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


def invert_recur(head):
    if head == None:
        return None

    invert_recur(head.left)
    invert_recur(head.right)

    head.left, head.right = head.right, head.left


def invert_unrecur(head):
    if head == None:
        return None
    stack = Stack()

    stack.push(head)
    while not stack.is_empty():
        head = stack.pop()

        head.left, head.right = head.right, head.left
        stack.push(head.left)
        stack.push(head.right)
