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


# 二叉搜索树的中序遍历是有序递增的,只有两个数打乱了的话也是有规律的
# 第一次降序的较大值,第二次降序的较小值就是我们要找的target,交换一下就可以了


def in_order_unrecur(head):
    if head != None:
        stack = Stack()
        pre = None
        err1 = None
        err2 = None
        while head != None or not stack.is_empty():
            if head != None:
                stack.push(head)
                head = head.left
            else:
                head = stack.pop()
                print(head.value, '\n')

                if pre != None and pre.value > head.value:
                    if err1 == None:
                        err1 = pre
                    else:
                        err2 = head

                pre = head
                head = head.right

    err1.value, err2.value = err2.value, err1.value
