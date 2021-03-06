from collections import deque

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

def get_and_remove_last_element(stack):
    # 得到栈底元素并移除,其他元素压会栈
    result = stack.pop
    if stack.is_empty():
        return result
    else:
        last = get_and_remove_last_element(stack)
        stack.push(result)
        return last

def reverse_stack(stack):
    if stack.is_empty():
        return
    
    cur = get_and_remove_last_element(stack)
    reverse_stack(stack)
    stack.push(cur)