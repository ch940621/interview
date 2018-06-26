from 翻转单链表 import reverse_linklist1
from 单次遍历返回链表中间节点 import get_middle_node

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

# python没有队列和栈的结构,但是Python已经高度抽象相关的功能,list能实现栈,collections中有deque
# 栈
# stack = [1,2,3]
# stack.append(4)
# stack.pop()
# 队列
# from collections import deque
# queue = deque(["Eric", "John", "Michael"])
# queue.append("Terry")
# queue.popleft()


# 方法1 用栈,将链表中的数据全部push到栈里,然后再迭代一遍链表,取出栈里的值逐个相互比较
# 时间 O(n),空间O(n)

def is_palindrome1(head):
    if head == None or head.next == None:
        return True
    pos = head
    
    stack = []
    while pos:
        stack.append(pos.value)
        pos = pos.next
    
    pos = head
    while pos:
        if pos.value != stack.pop():
            return False
        pos = pos.next
    return True


# 方法2 把后半部分的链表逆序,然后两段分别开始遍历,如果遇到不一样的不是回文结构
# 时间 O(n),空间O(1)

def is_palindrome2(head):
    if head == None or head.next == None:
        return True

    mid_node = get_middle_node(head)# 只遍历一遍获取单链表中间节点的函数
    new_mid = reverse_linklist1(mid_node) # 翻转链表的函数

    pos = head
    while pos:
        if pos.value != new_mid.value:
            return False
        else:
            pos = pos.next
            new_mid = new_mid.next
    return True


    

