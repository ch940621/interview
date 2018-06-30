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
