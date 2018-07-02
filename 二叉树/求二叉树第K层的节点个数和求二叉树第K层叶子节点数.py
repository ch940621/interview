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
# 第k层节点数
# 递归思路
def get_kth_level_nodes_total_recur(head, kth_level):
    if head == None or kth_level <= 0:
        return 0
    if head != None and kth_level == 1:
        return 1
    return get_kth_level_nodes_total_recur(
        head.left, kth_level - 1) + get_kth_level_nodes_total_recur(
            head.right, kth_level - 1) # 左子树中K-1层的节点个数 和 右子树中K-1层节点个数

# 非递归思路
def get_kth_level_nodes_total_unrecur(head,kth_level):
    if head == None or kth_level <= 0:
        return 0
    if head != None and kth_level == 1:
        return 1
    curr_level = Queue()
    next_level = Queue()
    nodes_total = 0
    curr_level_th = 0
    curr_level.enqueue(head)

    curr_level += 1 #咱们知道第一次遍历完毕的时候第一层已经溜走了,循环判断的对应是从第二层开始生效的
    while not curr_level.is_empty():
        curr = curr_level.dequeue()
        if curr != None:
            # print(curr.value, '\t')
            next_level.enqueue(curr.left)
            next_level.enqueue(curr.right)
        if curr_level.is_empty:
            curr_level_th += 1
            # print('\n')
            curr_level, next_level = next_level, curr_level
            if curr_level_th == kth_level:
                return curr_level.size()


# 第k层叶子节点数
# 递归思路
# 和上面比多一个增加判断是否是叶子节点
def get_kth_level_leaf_nodes_total_recur(head, kth_level):
    if head == None or kth_level <= 0:
        return 0
    if head != None and kth_level == 1:
        if head.left == None and head.right == None:
            return 1
        else:
            return 0
    return get_kth_level_leaf_nodes_total_recur(
        head.left, kth_level - 1) + get_kth_level_leaf_nodes_total_recur(
            head.right, kth_level - 1) # 左子树中K-1层的节点个数 和 右子树中K-1层节点个数

# 非递归思路
def get_kth_level_leaf_nodes_total_unrecur(head,kth_level):
    if head == None or kth_level <= 0:
        return 0
    if head != None and kth_level == 1:
        return 1
    curr_level = Queue()
    next_level = Queue()
    nodes_count = 0
    curr_level_th = 0
    curr_level.enqueue(head)

    curr_level += 1 #咱们知道第一次遍历完毕的时候第一层已经溜走了,循环判断的对应是从第二层开始生效的
    while not curr_level.is_empty():
        curr = curr_level.dequeue()
        if curr != None:
            print(curr.value, '\t')
            next_level.enqueue(curr.left)
            next_level.enqueue(curr.right)
            if curr.left == None and curr.right == None:
                nodes_count += 1
        if curr_level.is_empty:
            curr_level_th += 1
            print('\n')
            curr_level, next_level = next_level, curr_level
            if curr_level_th == kth_level:
                return nodes_count
            nodes_count = 0