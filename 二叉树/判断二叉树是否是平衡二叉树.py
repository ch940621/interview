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


# 如果二叉树为空，返回真
# 如果二叉树不为空，如果左子树和右子树都是AVL树并且左子树和右子树高度相差不大于1，返回真，其他返回假
# 后续遍历时，遍历到一个节点，其左右子树已经遍历  依次自底向上判断，每个节点只需要遍历一次
# 故用后序遍历最为合适


is_AVL = True # 全局变量,状态共享,可以省去重复判断
def get_is_AVL(head):
    get_height(head)
    return is_AVL
def get_height(head):
    if head == None:
        return True
    height_left = get_height(head.left)
    height_right = get_height(head.right)
    if abs(height_left - height_right) > 1:
        is_AVL = False
    return height_left + 1 if height_left > height_right else height_right + 1 # 下层的深度状态共享给上层,避免重复遍历



