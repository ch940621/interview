class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None # 初始化是空,后面有指向的时候是Node类型


# 非递归头插法
def reverse_linklist1(head):
    if head == None or head.next == None:
        return head

    cur = head
    tmp = None
    new_head = None

    while cur:
        tmp = cur.next
        cur.next = new_head
        new_head = cur
        cur = tmp
    return new_head

# 非递归平移法
def reverse_linklist2(head):
    if head == None or head.next == None:
        return head
    
    pos1 = head
    pos2 = head.next
    tmp = None

    while pos2:
        tmp = pos2.next
        pos2.next = pos1
        pos1 = pos2
        pos2 = tmp

    return pos1

# 递归法
def reverse_linklist3(head):
    if head == None or head.next == None:
        return head
    else:
        new_head = reverse_linklist3(head.next)
        head.next.next = head
        head.next = None
    return new_head







