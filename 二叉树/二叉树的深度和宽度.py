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

# 二叉树的深度
# 递归
# 如果二叉树为null,则二叉树的深度为0
# 如果二叉树不为null,则二叉树的深度＝max(左子树的深度，右子树的深度)＋1；

def get_deepth_recur(head):
    if head == None:
        return 0
    deepth_left = get_deepth_recur(head.left)
    deepth_right = get_deepth_recur(head.right)
    return deepth_left + 1 if deepth_left > deepth_right else deepth_right + 1

# 非递归的解法思路和二叉树的层次遍历一毛一样
# 每层完事儿后deep+1

def get_deepth_unrecur(head):
    if head == None:
        return 0
    deepth = 0
    curr_level = Queue()
    next_level = Queue()
    curr_level.enqueue(head)

    while not curr_level.is_empty():
        curr = curr_level.dequeue()
        if curr != None:
            # print(curr.value, '\t')
            next_level.enqueue(curr.left)
            next_level.enqueue(curr.right)

        if curr_level.is_empty:
            # print('\n')
            deepth += 1
            curr, next_level = next_level, curr

    return deepth


# 二叉树的宽度思路和层次遍历也一样
# 不同点是在需要统计一下

def get_wideth_unrecur(head):
    if head == None:
        return None
    curr_level = Queue()
    next_level = Queue()
    curr_level.enqueue(head)
    wideth = 1

    while not curr_level.is_empty():
        curr = curr_level.dequeue()
        if curr != Node:
            # print(curr.value, '\t')
            next_level.enqueue(curr.left)
            next_level.enqueue(curr.right)

        if curr_level.is_empty:
            # print('\n')
            curr, next_level = next_level, curr
            wideth = wideth if wideth >= curr.size() else curr.size()


    return wideth




