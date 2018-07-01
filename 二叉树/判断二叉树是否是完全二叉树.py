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


# 判断是不是完全二叉树可以层次遍历二叉树然后检查以下条件
# 1.如果发现当前结点有右孩子没左孩子,直接判断不是
# 2.如果当前结点只有左孩子,那么后续结点必须为叶子节点否则返回不是
# 3.如果遍历完毕没有发现异常则可以返回是
def get_is_CBT(head):
    if head == None:
        return True
    queue = Queue()
    queue.enqueue(head)

    find_first_single_child_node = False  # 标记是否找到了第一个也希望是唯一的那个只有左孩子的那个节点

    while not queue.is_empty():
        head = queue.dequeue()

        if head.left == None and head.right != None:
            return False

        if find_first_single_child_node and (head.left != None
                                             or head.right != None):
            return False

        # 放到前面一个校验的判断之后是因为第一次有赦免呀,不算呐!
        if head.left != None and head.right == None:
            find_first_single_child_node = True

        if head.left != None:
            queue.enqueue(head.left)
        if head.right != None:
            queue.enqueue(head.right)

    return True
