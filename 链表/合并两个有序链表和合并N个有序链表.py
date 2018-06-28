class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def merge_two_linklist(head1,head2):
    if head1 == None or head2 == None:
        return head1 if head1 != None else head2
    new_head = head1 if head1.value <= head2.value else head2
    # head1,head2 为操作指针,tail为新链表的最后一个节点,new_head新链表第一个结点
    if new_head == head1:
        head1 = head1.next
    else:
        head2 =head2.next
    
    tail = new_head

    while head1 != None and head2 != None:
        if head1.value <= head2.value:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    if head1 == None:
        tail.next = head2
    elif head2 == None:
        tail.next = head1
    
    return new_head

# 递归版本
def merge_two_linklist1(head1,head2):
    new_head = None
    if head1 == None:
        return head2
    elif head2 == Node:
        return head1
    else:
        if head1.value < head2.value:
            new_head = head1
            new_head.next = merge_two_linklist1(head1.next,head2)
        else:
            new_head = head2
            new_head.next = merge_two_linklist1(head1,head2.next)
        return new_head


def merge_n_linklist(lists):
    num = len(lists)
    if num == 0:
        return None
    while num > 1:
        for pos in range(num // 2):
            pass
             





# TODO
# 用堆实现的nlogn复杂度的合并