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

# 统计二叉树中节点个数
# 递归
def count_nodes_recur(head):
    if head == None:
        return 0
    return count_nodes_recur(head.left) + count_nodes_recur(head.right) + 1

# 非递归
