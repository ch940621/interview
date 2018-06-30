# 我们需要排序的栈为stack,然后我们申请一个栈记为help,在stack上面执行pop()操作，弹出的元素记为cur
# 如果cur小于或者等于栈顶元素，则将cur压入help
# 如何cur大于help的栈顶元素，则将help的元素涿步弹出，逐一压入stack，直到cur小于或等于help的栈顶元素、再将cur压入help

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

def sort_stack_by_stack(stack):
    help = Stack()
    while not stack.is_empty():
        cur = stack.pop()
        while not help.is_empty() and cur > help.peek():
            stack.push(help.pop())
        help.push(cur)

    while not help.is_empty():
        stack.push(help.pop())

    return stack

    