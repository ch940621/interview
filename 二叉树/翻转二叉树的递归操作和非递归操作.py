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

# 其实就是考的二叉树的遍历,打印节点的位置换成交换就好了,这种题都不能不写好的话面试怕是要翻车哟
def invert_recur(head):
    if head == None:
        return None

    invert_recur(head.left)
    invert_recur(head.right)
    head.left, head.right = head.right, head.left  # 放在哪个位置都可以,类似前中后序的三中遍历


# 层次遍历,先序遍历,中序,后续 ,都可以拿来实现翻转,把打印替换成翻转子树就可以了
# 先序
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

# 中序
def invert_unrecur1(head):
    if head == None:
        return None
    stack = Stack()
    while not stack.is_empty() or head != None:
        if head != Node:
            stack.push(head)
            head = head.left
        else:
            head = stack.pop()
            head.left, head.right = head.right, head.left
            head = head.right

# 后序
# 新的数据结构
class Node1(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.first_visited = False


def pos_order_unrecur(head):
    stack = Stack()

    while head != None or not stack.is_empty():
        while head != None: # 玩命地左子树压倒底
            stack.push(head)
            head = head.left

        if not stack.is_empty():
            tmp = stack.peek() 

            if tmp.first_visited:
                # 左右子树已经访问过了
                tmp = stack.pop()
                print(tmp, '\n')
            else:
                # 还木有访问右子树呢,赶紧补上
                head = tmp.right
                tmp.is_first_visit = True


def invert_unrecur2(head):
    stack = Stack()

    while head != None or not stack.is_empty():
        while head != None:
            stack.push(head)
            head = head.left

        if not stack.is_empty():
            tmp = stack.pop()

            if tmp.is_first_visit:
                tmp = stack.pop()
                tmp.left, tmp.right = tmp.right, tmp.left

            else:
                head = tmp.right
                tmp.is_first_visit = True


# 层序
def invert_unrecur3(head):
    if head == None:
        return None

    queue = Queue()
    queue.enqueue(head)

    while not queue.is_empty():
        head = queue.dequeue()
        head.left, head.right = head.right, head.left

        if head.left != None:
            queue.enqueue(head.left)
        if head.right != None:
            queue.enqueue(head.right)
