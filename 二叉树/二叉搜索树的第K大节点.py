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
def kth_node_recur(head,k):
    global count
    count = 0
    def search(head,k):
        global count
        if head != None:
            node = search(head.left,k)
            # 退出条件
            if node != None:
                return node
            count += 1
            if count == k:
                return head
            if node != None:
                return node


def kth_node_unrecur(head,k):
    if k <= 0 or head == None:
        return None
    count = 0
    stack = Stack()

    while not stack.is_empty() or head != None:
        if head != None:
            stack.push(head)
            head = head.left
        else:
            head = stack.pop()
            count += 1
            if count == k:
                return head
            head = head.right

