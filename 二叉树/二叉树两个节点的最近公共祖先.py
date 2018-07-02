

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

# 后续遍历,自底而上

# 如果遍历到的当前节点是两个给定节点中的任意一个之时，那么我们就向父节点汇报此节点，否则递归到节点为空时返回空值
# 当遍历的节点不是两个节点的任意一个之时,判断左右子树的返回结果
# 左子树右子树都返回非空,那么当前节点为所寻节点.即两个节点分居两侧.向父节点返回当前节点
# 左右子树只有一个子树返回非空,那么节点仅存在树的一侧.向父节点返回非空节点
# 左右子树都返回空,说明节点不在这棵树里面.向父节点返回空
def find_lowest_commmon_partent(head,node1,node2):
    if head in [None,node1,node2]:
        return head

    node_left = find_lowest_commmon_partent(head.left,node1,node2)
    node_right = find_lowest_commmon_partent(head.right,node1,node2)
    if node_left != None and node_right != None:
        return head
    if node_left == None and node_right == None:
        return None
    return node_left if node_left != None else node_right