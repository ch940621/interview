from collections import deque


class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


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


# 二叉树的层次遍历
# 思路一:用两个队列,第一个队列currentLevel用于存储当前层的结点,第二个队列nextLevel用于存储下一层的结点
# 当前层currentLevel为空时,表示这一层已经遍历完成.
# 然后将第一个空的队列currentLevel与队列nextLevel交换
# 重复直到遍历完毕即可


def level_order_unrecur(head):
    if head == None:
        return None
    curr_level = Queue()
    next_level = Queue()
    curr_level.enqueue(head)

    while not curr_level.is_empty():
        curr = curr_level.dequeue()
        if curr != Node:
            print(curr.value, '\t')
            next_level.enqueue(curr.left)
            next_level.enqueue(curr.right)

        if curr_level.is_empty:
            print('\n')
            curr, next_level = next_level, curr

# 二叉树的蛇形遍历
# 经过多次思考,蛇形遍历最简单的办法还是用两个栈存
# 但奇数行先存左孩子,后存右孩子
# 偶数行先存右孩子,再存左孩子
# 当前层currentLevel为空时,表示这一层已经遍历完成
# 重复直到遍历完毕即可

def zigzag_order_unrecur(head):
    if head == None:
        return None
    stack1 = Stack()
    stack2 = Stack()
    stack1.push(head)
    deep = 1
    while deep % 2 == 1 and not stack1.is_empty():
        curr = stack1.pop()
        if curr != None:
            print(curr.value,'\t')
            stack2.push(curr.left)
            stack2.push(curr.right)
        
        if stack1.is_empty():
            print('\n')
            deep += 1

    while deep % 2 == 0 and not stack2.is_empty():
        curr = stack2.pop()
        if curr != None:
            print(curr.value,'\t')
            stack1.push(curr.right)
            stack2.push(curr.left)

        if stack2.is_empty():
            print('\t')
            deep += 1

    
