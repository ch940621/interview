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


# 两个队列实现栈的思路一就是保持一个队列永远为空,每次入栈入到空的那个,然后那个非空的再一次排过去,模拟了插队 过程也就是有了栈的特点,出栈直接出游元素的那个
class Stack_by_Queue(object):
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, item):
        if not self.queue1.is_empty():
            self.queue2.enqueue(item)
            while not self.queue1.is_empty():
                self.queue2.enqueue(self.queue1.dequeue())
        else:
            self.queue1.enqueue(item)
            while not self.queue2.is_empty():
                self.queue1.enqueue(self.queue2.dequeue())

    def pop(self):
        if self.queue1.is_empty() and self.queue2.is_empty():
            print('erro')
            return None

        elif not self.queue1.is_empty():
            return self.queue1.dequeue()
        else:
            return self.queue2.dequeue()


# 两个队列实现栈的思路二就是保持一个队列永远为空,每次入栈入到不空的那个,出栈先把有元素的那队依次挪到空的那个队留最后一个元素,然后最后一个元素就是出栈的元素,模拟了插队 过程也就是有了栈的特点
class Stack_by_Queue1(object):
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, item):
        if self.queue1.is_empty() and self.queue2.is_empty():
            self.queue1.enqueue(item)
        else:
            if self.queue1.is_empty():
                self.queue2.enqueue(item)
            if self.queue2.is_empty():
                self.queue1.enqueue(item)

    def pop(self):
        if self.queue1.is_empty() and self.queue2.is_empty():
            print('erro')
            return None

        if self.queue1.is_empty():
            while self.queue2.size() > 1:
                self.queue1.enqueue(self.queue2.dequeue)

        if self.queue2.is_empty():
            while self.queue1.size() > 1:
                self.queue2.enqueue(self.queue1.dequeue)


# 两个栈实现队列的思路就是第一栈拿来入队,第二个拿来出队,第一个正常入,第二个出来的时候如果第二个栈不为空直接pop第二个栈就好,如果为空需要把第一个栈清空,依次转移到第二个栈,再执行pop操作
class Queue_by_Stack(object):
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self,item):
        self.stack1.push(item)

    def dequeue(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())

        return self.stack2.pop()



