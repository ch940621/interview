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




def get_path(head,sum):
    path = []
    res = []
    path_sum1(head,sum,path,res)
    return res
def path_sum1(head,sum,path,res):
    if head == None or head.value > sum: 
        return None
    
    path.append(head.value)
    if head.left == None and head.right == None:
        if head.value == sum:
            res.append(path)
    else:
        path_sum1(head.left,sum - head.value,path,res)
        path_sum1(head.right,sum - head.right,path,res)
    path.pop()


# 如果要路径最长的,把记录的res长度最大的遍历一下取出来,或者改一下res的结构,在搜索的时候就把长度值也就是二叉树的深度一起存一下


# 判断时候存在给定值的累加和路径
# 算是简化版

def exit_path_sum(head,sum):
    if head == None:
        return None
    sum -= head.value
    if head.left == None and head.right == None and sum == 0:
        return True
    return exit_path_sum(head.left,sum) or exit_path_sum(head.right,sum)


