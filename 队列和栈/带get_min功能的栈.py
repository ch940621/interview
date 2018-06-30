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

# 思路一:用两个栈,第一个栈stack存原始数据,第二个栈stack_min存get_min弹出的
# 压入 stack的时候判断stack_min是否为空,若为空则同步压入
# 否则判断当前的值和stack_min栈顶比哪个更小,如果当前更小,当前也压入,否则stack_min不压入
# 弹出的时候判断一下弹出值和stack_min的栈顶值是否一样,若一样同步弹出

class Stack_with_getmin(object):
    def __init__(self):
        self.stack = Stack()
        self.stack_min = Stack()

    def push(self,item):
        if self.stack_min.is_empty():
            self.stack_min.push(item)
        else:
            if item <= self.get_min():
                self.stack_min.push(item)

        self.stack.push(item)

    def pop(self,item):
        if self.stack.is_empty():
            return None

        value = self.stack.pop()

        if value == self.get_min():
            self.stack_min.pop()
        return value

    def get_min(self):
        if self.stack_min.is_empty():
            return None
        return self.stack_min.peek()


# 思路二是在思路一的基础上的修改,主要修改时如果当前数据比stack_min栈顶数据大则重复压入,这样弹出的时候不用做判断    

class Stack_with_getmin1(object):
    def __init__(self):
        self.stack = Stack()
        self.stack_min = Stack()

    def push(self,item):
        if self.stack_min.is_empty():
            self.stack_min.push(item)
        else:
            if item <= self.get_min():
                self.stack_min.push(item)
            else:
                self.stack_min.push(self.stack_min.peek())
        self.stack.push(item)

    def pop(self,item):
        if self.stack.is_empty():
            return None
        self.stack.pop()
        return self.stack_min.pop()

    def get_min(self):
        if self.stack_min.is_empty():
            return None
        return self.stack_min.peek()