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


# 节点总数递归
def get_nodes_total_recur(head):
    if head == None:
        return 0

    return get_nodes_total_recur(head.left) + get_nodes_total_recur(head.right) + 1

# 叶子节点总数递归

def get_leaf_nodes_total_recur(head):
    if head == None:
        return 0
    if head.left == None and head.right == None:
        return 1

    return get_leaf_nodes_total_recur(head.left) + get_leaf_nodes_total_recur(head.right)


# 节点总数用任何一个非递归遍历方式就可以实现非递归的函数

# 叶子节点总数也是可以用任何一个非递归遍历方式就可以实现非递归的函数